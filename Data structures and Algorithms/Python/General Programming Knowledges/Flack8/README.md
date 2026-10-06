## Flake8
Flake8 is a python style checker that automatically check for python style formatting.

### Install it 
```bash
    python -m pip install flack8
```

### Run It
```bash
    flake8 code.py
    python -m flake8 code.py
```


### Ignore Some error 
- Sometimes you want to override the standards that flake8 is shipped with.

- In these scenarios you want to tell flake8 to ignore certain errors by passing them along on the terminal.

```bash
    flake8 code.py --ignore W291
    flake8 code.py --ignore W291,E302
    flake8 *.py
```

### Config files
- Instead of passing everything on the command line you may also choose to have a config file. You can configure errors to ignore but also files to exclude.

- We create a **.flake8** file

It will look like

```
[flake8]
#W291 - we don't care about trailling whitespace
#E302 - one line between function is fine
ignore = W291,E302
exclude = ignore_this.py
```


### Line width and complexity
- Something specific to evry team
- Code complexity refere to for loop 
- It is a good thing to limit it
- Line width refer to maximum line lenght
```bash
    [flake8]
    # W291 - we dont care about trailing whitespace
    # E302 - one line between functions is fine
    ignore = W291,E302
    exclude = ignore_this.py
    max-complexity = 10
    max-line-length = 70
```


### Extensions

- Flake8 can be configure but it can also be extended 
- There are many plugins for it
- There is a whole small ecosytem in flake8 compatible 
- Flake8 can be configurable
- To see which version are active you use : 
```bash
    flake8 --version
```
- Let's install a plugin as an example :
```bash
python -m pip install pep8-naming
```

- Looks for flake8 compatible package
- Go to package and see compatible packages


- We can add it into the pre-commit hooks or ci pipeline
- In order to have more maintaionable code