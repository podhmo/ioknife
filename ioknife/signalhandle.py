import typing as t
import logging
import asyncio
import signal
from functools import partial
from asyncio.subprocess import Process


logger = logging.getLogger(__name__)


class Demux:
    """one signal input (main-process) to multi signal outputs (sub-processes)"""

    def __init__(self, *, loop: asyncio.AbstractEventLoop) -> None:
        self.ps: t.List[Process] = []
        self.loop = loop
        self.on_init()  # xxx:

    def on_init(self) -> None:
        self.loop.add_signal_handler(
            signal.SIGINT, partial(self.send_signal, signal.SIGINT)
        )
        self.loop.add_signal_handler(
            signal.SIGTERM, partial(self.send_signal, signal.SIGTERM)
        )

    def connect(self, p: Process) -> None:
        self.ps.append(p)

    def send_signal(self, sig: int) -> None:
        logger.info("send signal (%s)", sig)
        for p in self.ps:
            try:
                p.send_signal(sig)
            except ProcessLookupError:
                logger.warning(
                    "send signal %s  -- ProcessLookupError -- pid=%s", sig, p.pid
                )

    def terminate(self) -> None:
        for p in self.ps:
            p.terminate()

    def kill(self) -> None:
        for p in self.ps:
            p.kill()
