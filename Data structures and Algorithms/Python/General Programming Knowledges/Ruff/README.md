## Ruff
Ruff is an extremely fast Python linter and code formatter written in the Rust programming language. Created by Astral, it replaces multiple slower Python tools (such as Flake8, Black, isort, and pyupgrade) with a single, highly efficient binary. It checks for potential bugs, fixes issues automatically, and formats code for consistency.

### Installation 
```bash
    python -m pip install ruff
```

### Run It
```bash
    ruff check script.py
```
```bash
    ruff check --fix script.py
```
- It was able to fix three of the errors, but one error requires manual intervention.

### Configure ruff
- Ruff may lets some things in the code that it isn't complaining about
- it is due to a limited set of rules to check 
- To configure it we create a **ruff.toml** file
- here is one :
```toml
    [lint]
    select = ["D"]
```
- to configure you can use linting rules here : https://docs.astral.sh/ruff/rules/
- we can get incompatibility warning when we get many rules
- to correct it we can ignore some rule
```toml
    [lint]
    select = ["D"]
    ignore = ["D211", "D213"]
```


### Unsafe Fix
- sometimes ruff want to make unsafe fixes
- in this case need to add :
```bash
    ruff check --fix --unsafe-fixes demo.py
```
- we can configure ruff to ignore a specific line over a rules by adding a **#noqa** comment.
- 