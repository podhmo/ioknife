TEE ?= |& tee

defaut: 00 01 02 03

00: dst
	rm -rf dst/$@ && mkdir -p dst/$@
	ioknife too --cmd "python -u src/gen.py" ${TEE} dst/$@/too.output

# with shell
01: dst
	rm -rf dst/$@ && mkdir -p dst/$@
	ioknife too --shell --cmd "python -u src/gen.py | sed 's/0/@/g'" ${TEE} dst/$@/too.output

# many
02: dst
	rm -rf dst/$@ && mkdir -p dst/$@
	ioknife too --cmd "python -u src/gen.py" --cmd "python -u src/gen.py" --cmd "python -u src/gen.py" | sort ${TEE} dst/$@/too.output

# many
03: dst
	rm -rf dst/$@ && mkdir -p dst/$@
	ioknife too --cmd "python -u src/gen.py" --cmd "python -u src/gen.py" --cmd "python -u src/gen.py" --cmd "python -u src/gen.py" --cmd "python -u src/gen.py" --cmd "python -u src/gen.py" --cmd "python -u src/gen.py" --cmd "python -u src/gen.py" --cmd "python -u src/gen.py" --cmd "python -u src/gen.py" --cmd "python -u src/gen.py" --cmd "python -u src/gen.py"  | sort ${TEE} dst/$@/too.output
