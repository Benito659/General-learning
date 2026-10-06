## Bandit 
Bandit is a python library that help write secure python code. Bandit look at your code and see if there is security risque that you want to adress.

### Installation 
```bash
    pip install bandit 
```

### Run It 
- We can run it against one file
```bash
    bandit bad.py
```

- We can run it against all the file in a folder called **clumper** recursively
```bash
    bandit -r clumper
    python -m bandit -r clumper
```

### No security check
- Sometimes bandit will notice a security risk when there is none.
- If you re-run the bandit command with the nosec comment then it will no longer complain about it.
```python
    if path.startswith(("https:", "http:")):
    with urllib.request.urlopen(path) as resp:  # nosec
        ...
```

### Pre - commit hook
- Bandit can also be configured as a pre-commit hook.
- Can be add in continuous integration.