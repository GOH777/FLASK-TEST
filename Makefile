install:
     poetry install

selfcheck:
    poetry check

build: check
    poetry build

run: start
    python hello.py
	
 PHON   