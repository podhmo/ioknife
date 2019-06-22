TEE ?= |& tee

00: dst
	rm -r dst/$@ && mkdir -p dst/$@
	(cat src/00* | ioknife grepo '[^ ]+/bash' ) ${TEE} dst/$@/grepo.out 2>&1

