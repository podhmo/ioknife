[![Build Status](https://travis-ci.org/podhmo/ioknife.svg?branch=master)](https://travis-ci.org/podhmo/ioknife)

# ioknife

knives for io.

```console
$ ioknife -h
usage: ioknife [-h] [--logging {CRITICAL,FATAL,ERROR,WARN,WARNING,INFO,DEBUG,NOTSET}]
               [--debug DEBUG]
               {rest,grepo,too} ...

positional arguments:
  {rest,grepo,too}

optional arguments:
  -h, --help            show this help message and exit
  --logging {CRITICAL,FATAL,ERROR,WARN,WARNING,INFO,DEBUG,NOTSET}
  --debug DEBUG
```

## subcommands

see [docs](https://github.com/podhmo/ioknife/tree/master/docs)

## Changes

0.2.0

- `ioknife grepo` command is added.
- `ioknife too`, reading commands setting from stdin. (and add --dump-context)

0.1.0

- `ioknife too` command is added.

0.0.0

- `ioknife rest` command is added.
