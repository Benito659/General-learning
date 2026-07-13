## Entr
Entr automatically run Pytest on File Update. It monitors directories for file changes and automatically runs specified commands, such as reloading a web server or recompiling code every time you save a file.

### Installation
- to install entr on MacOS :
```bash
    brew install entr
```
- to install on linux :
```bash
    sudo apt-get update
    sudo apt-get install entr
```

### Run It
- to run it we retreive all file in folder and we update tests automatically when there are changing
```bash
    ls checking/*.py | entr pytest test.py::test_starts_correctly
```
- This -c flag will clear the screen every time an update happens.
```bash
    ls checking/*.py | entr -c pytest test.py::test_starts_correctly
```