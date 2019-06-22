# too

python version of [too.js](https://github.com/otiai10/too.js)

Combine multiple commands' stream, keep all foreground and kill all in one Ctrl+C.

[![asciicast](https://asciinema.org/a/1CrUUxYyi5oLwalkjK0XRgLAl.svg)](https://asciinema.org/a/1CrUUxYyi5oLwalkjK0XRgLAl)

## examples

```console
$ ioknife too --cmd "python -u gen.py"  --cmd "python -u gen.py"  --cmd "python -u gen.py"
[2] python   0 1561210357.4283853
[0] python   0 1561210357.4445136
[1] python   0 1561210357.4460835
[1] python   1 1561210357.6947668
[0] python   1 1561210357.9946055
[2] python   1 1561210358.0169775
  C-c C-cINFO:ioknife.too:send signal (Signals.SIGINT)
[0] python   Traceback (most recent call last):
[0] python     File "gen.py", line 6, in <module>
[0] python       time.sleep(random.random())
[0] python   KeyboardInterrupt
[1] python   Traceback (most recent call last):
[1] python     File "gen.py", line 6, in <module>
[1] python       time.sleep(random.random())
[1] python   KeyboardInterrupt
[2] python   Traceback (most recent call last):
[2] python     File "gen.py", line 6, in <module>
[2] python       time.sleep(random.random())
[2] python   KeyboardInterrupt
```

then, gen.py

```python
import time
import random

for i in range(5):
    print(i, time.time())
    time.sleep(random.random())
```
