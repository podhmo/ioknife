TEE ?= |& tee

00: dst
	rm -r dst/$@ && mkdir -p dst/$@
	(cat src/00* | grep bash) ${TEE} dst/$@/grep.out
	(cat src/00* | ioknife rest -n 1 | grep bash) ${TEE} dst/$@/rest.out 2>&1
