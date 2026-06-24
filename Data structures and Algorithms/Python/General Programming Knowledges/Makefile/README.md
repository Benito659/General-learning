## Makefile
Make is a python library that help you automate a bash commands. 
Especially the one you are using many times

### Create Makefile
```bash
    touch Makefile
```

### Makefile :
- i write all the command i want to excute in it
```
    test:
        pytest test.py
    clean:
        rm -rf __pycache__ .pytest_cache
```

### Run it
```bash
    make clean
    make test
```

### Chain command
- we can chain command together so we don't need to call one command and then the other one
- we can call them all at once 
```
test:
    pytest tests.py

clean:
    rm -rf __pycache__ .pytest_cache

flake:
    flake8 common.py tests.py

check: flake test clean

```


### Phony pholder
- when there is already a folder that have the same name as a make command, we get message thatevry thing is up to date
- to avoid it we creat a **.PHONY** variable 
```
.PHONY: docs

test:
    pytest tests.py

clean:
    rm -rf __pycache__ .pytest_cache

flake:
    flake8 common.py tests.py

check: flake test clean

docs:
    pdoc --html --force --output-dir docs common

```


### Projects
- some command we can add to start a project with 
```
install:
    pip install -r requirements.txt

dev: install
    pip install -r dev-requirements.txt
```

- separate dev and normal packages

- tell in the readme how to start it with make command

### Keep it clean, can have some problem on windows

### Helps commands
- print some helpfull infomation
```bash
    make help
```
- in the makefile
```
    help:
    @echo "available commands"
    @echo " - install    : installs all requirements"
    @echo " - dev        : installs all development requirements"
    @echo " - test       : run all unit tests"
    @echo " - clean      : cleans up all folders"
    @echo " - flake      : runs flake8 style checks"
    @echo " - check      : runs all checks (tests + style)"
    @echo " - docs       : generate docs locally in /docs folder"
```