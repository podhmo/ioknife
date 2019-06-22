import typing as t
import asyncio

T = t.TypeVar("T")


def run(coro: t.Awaitable[T], *, debug: bool = False) -> T:
    loop = asyncio.get_event_loop()
    if debug:
        loop.set_debug(debug)
    return loop.run_until_complete(coro)
