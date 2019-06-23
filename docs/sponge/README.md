# sponge

moreutils's one.

```console
# ng
$ cat hello.txt | sed 's/o/@/g' > hello.txt

# ok
$ cat hello.txt | sed 's/o/@/g' | python sponge hello.txt

# tee
$ cat hello.txt | sed 's/o/@/g' | python sponge --tee hello.txt
hell@
```

hello.txt

```
hello
```
