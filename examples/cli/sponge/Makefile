TEE ?= |& tee

default: 01 02

# cat output, unexpected behaviour
# 00:
# 	rm -rf dst/$@ && mkdir -p dst/$@
# 	cp src/hello.txt dst/$@/broken.output
# 	cat dst/$@/broken.output | sed 's/o/@/g' > dst/$@/broken.output

# ok
01:
	rm -rf dst/$@ && mkdir -p dst/$@
	cp src/hello.txt dst/$@/use-sponge.output
	cp src/hello.txt dst/$@/use-sponge-append.output
	cat dst/$@/use-sponge.output | sed 's/o/@/g' | ioknife sponge dst/$@/use-sponge.output
	cat dst/$@/use-sponge-append.output | sed 's/o/@/g' | ioknife sponge -a dst/$@/use-sponge-append.output
	cat dst/$@/use-sponge.output | sed 's/o/@/g' | ioknife sponge dst/$@/use-sponge.output
	cat dst/$@/use-sponge-append.output | sed 's/o/@/g' | ioknife sponge -a dst/$@/use-sponge-append.output

# use temporary file (with --max-memory-size)
02:
	rm -rf dst/$@ && mkdir -p dst/$@
	cp src/hello.txt dst/$@/use-sponge.output
	cp src/hello.txt dst/$@/use-sponge-append.output
	cat dst/$@/use-sponge.output | sed 's/o/@/g' | ioknife sponge --max-memory-size=1 dst/$@/use-sponge.output
	cat dst/$@/use-sponge-append.output | sed 's/o/@/g' | ioknife sponge --max-memory-size=1 -a dst/$@/use-sponge-append.output
	cat dst/$@/use-sponge.output | sed 's/o/@/g' | ioknife sponge --max-memory-size=1 dst/$@/use-sponge.output
	cat dst/$@/use-sponge-append.output | sed 's/o/@/g' | ioknife sponge --max-memory-size=1 -a dst/$@/use-sponge-append.output
