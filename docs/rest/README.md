# rest

Output first nth lines to stderr, and rest to stdout.

```console
$ ps aux | ioknife rest -n 1 | grep bash | sed "s@$USER@ME@g" | head -n 3
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
ME        759  0.0  0.0   9276  5028 pts/10   Ss+   6月12   0:00 /bin/bash
ME       1882  0.0  0.0   9144  5112 pts/0    Ss    6月09   0:00 bash
ME       4435  0.0  0.0  10052  6300 pts/1    Ss+   6月09   0:04 /bin/bash
```
