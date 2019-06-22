import typing as t
import logging
import contextlib
import asyncio

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


@contextlib.asynccontextmanager
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
