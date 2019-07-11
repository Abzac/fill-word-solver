.PHONY: all flake mypy isort

all: flake mypy isort

flake:
	flake8 src/

mypy:
	mypy src/

isort:
	@isort setup.py
	@isort -rc src/
