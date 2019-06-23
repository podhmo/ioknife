import typing as t
import sys
import contextlib
import logging

logger = logging.getLogger(__name__)


def rest(*, n: int = 1, debug: bool) -> None:
    """first n lines, write to stderr, rest, write to stdout"""
    for i, line in zip(range(n), sys.stdin):
        sys.stderr.write(f"\x1b[90m{line}\x1b[0m")
    for line in sys.stdin:
        sys.stdout.write(line)


def sponge(
    *,
    filename: str,
    append: bool = False,
    tee: bool = False,
    max_memory_size: int,
    debug: bool,
) -> None:
    """soak up all input from stdin and write it to"""
    from tempfile import SpooledTemporaryFile

    with contextlib.ExitStack() as s:
        tmpio = SpooledTemporaryFile(
            max_size=max_memory_size, mode="w+", prefix="sponge."
        )
        for line in sys.stdin:
            tmpio.write(line)

        has_file = bool(tmpio.name is not None)
        if has_file:
            logger.info("sponge: using temporary file (%s)", tmpio.name)
            tmpio = s.enter_context(tmpio)

        mode = "a" if append else "w"

        with open(filename, mode) as wf:
            tmpio.seek(0)
            if tee:
                for line in tmpio:
                    wf.write(line)
                    sys.stdout.write(line)
            else:
                for line in tmpio:
                    wf.write(line)


def too(*, cmds: t.List[str], shell: bool, dump_context: bool, debug: bool) -> None:
    """combine multiple commands' stream, keep all foreground and kill all in one Ctrl+C"""
    import shlex
    from ioknife.too import too as run_too

    if cmds:
        commands = [shlex.split(cmd) for cmd in cmds]
    else:
        commands = [
            shlex.split(line.rstrip())
            for line in sys.stdin
            if line.strip() and not line.startswith("#")
        ]

    if dump_context:
        for cmd in commands:
            print(cmd)
        sys.exit(0)
    run_too(commands, debug=debug, shell=shell)


def grepo(pattern: str, filename: t.Optional[str] = None, *, debug: bool) -> None:
    """grep -o <pattern> and write matched line to stderr"""

    # TODO: optimization (use native grep command, or rg or ag)
    import re

    rx = re.compile(pattern)

    with contextlib.ExitStack() as s:
        rf = sys.stdin
        if filename is not None:
            rf = s.enter_context(open(filename))
        for line in rf:
            m = rx.search(line)
            if m is not None:
                print(f"\x1b[90mmatched: {line.rstrip()}\x1b[0m", file=sys.stderr)
                print(m.group(0))
                sys.stderr.flush()
                sys.stdout.flush()


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser()
    parser.print_usage = parser.print_help  # type: ignore
    parser.add_argument(
        "--logging",
        choices=list(logging._nameToLevel.keys()),
        default="INFO",
        dest="log_level",
    )
    parser.add_argument("--debug", action="store")

    subparsers = parser.add_subparsers(dest="subcommand")
    subparsers.required = True

    # rest
    fn = rest
    sparser = subparsers.add_parser(fn.__name__, description=fn.__doc__)
    sparser.set_defaults(subcommand=fn)
    sparser.add_argument("-n", required=False, default=1, type=int, help="(default: 1)")

    # grepo
    fn = grepo  # type: ignore
    sparser = subparsers.add_parser(fn.__name__, description=fn.__doc__)
    sparser.set_defaults(subcommand=fn)
    sparser.add_argument("pattern")
    sparser.add_argument("filename", nargs="?")

    # sponge
    fn = sponge  # type: ignore
    sparser = subparsers.add_parser(fn.__name__, description=fn.__doc__)
    sparser.set_defaults(subcommand=fn)
    sparser.add_argument("-a", "--append", action="store_true")
    sparser.add_argument("--tee", action="store_true")
    sparser.add_argument(
        "--max-memory-size",
        type=int,
        default=24 * 1024 * 1024,
        help="default: 24 * 1024 * 1024 bytes",
    )
    sparser.add_argument("filename")

    # too
    fn = too  # type: ignore
    sparser = subparsers.add_parser(fn.__name__, description=fn.__doc__)
    sparser.set_defaults(subcommand=fn)
    sparser.add_argument("--cmd", action="append", dest="cmds")
    sparser.add_argument("--shell", action="store_true")
    sparser.add_argument("--dump-context", action="store_true")

    args = parser.parse_args()
    params = vars(args).copy()
    logging.basicConfig(level=getattr(logging, params.pop("log_level")))
    params.pop("subcommand")(**params)
