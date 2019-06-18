test:
	python setup.py test

format:
#	pip install -e .[dev]
	black ioknife setup.py

build:
#	pip install wheel
	python setup.py bdist_wheel

upload:
#	pip install twine
	twine check dist/ioknife-$(shell cat VERSION)*
	twine upload dist/ioknife-$(shell cat VERSION)*

.PHONY: test format build upload
