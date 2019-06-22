import typing as t
import logging
import asyncio

try:
    from contextlib import asynccontextmanager
except ImportError:
    from .compat._contextlib_py36 import asynccontextmanager
try:
    from asyncio import run  # noqa
except ImportError:
    from .compat._asyncio_py36 import run  # type: ignore
run  # NOQA

logger = logging.getLogger(__name__)
T = t.TypeVar("T")


async def queue_as_aiter(q: "asyncio.Queue[T]") -> t.AsyncIterator[T]:
    canceled_exc = None
    while True:
        try:
            item = await q.get()
            yield item
        except asyncio.CancelledError as e:
            canceled_exc = e
            break
        finally:
            if canceled_exc is None:
                q.task_done()


@asynccontextmanager
async def consuming(
    q: "asyncio.Queue[T]", ause: t.Callable[[t.AsyncIterator[T]], t.Awaitable[None]]
) -> t.AsyncIterator[t.Callable[[t.AsyncIterator[T]], t.Awaitable[None]]]:
    async def asend(aiter: t.AsyncIterator[T]) -> None:
        async for item in aiter:
            await q.put(item)

    try:
        loop = asyncio.get_event_loop()
        ct = loop.create_task(ause(queue_as_aiter(q)))
        yield asend
        await q.join()
        assert q.empty()
    finally:
        ct.cancel()
