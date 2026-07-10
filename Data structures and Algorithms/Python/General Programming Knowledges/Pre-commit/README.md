## Pre-commit
Pre-commit is a python package that helps prevent wrong code getting into a commit. It automates the checking such that small bugs are caught early. It can also be customised

### Installation
- we need to ensure we are in a git repository
```bash
    git init
```
- we install pre-commit
```bash
    pip install pre-commit

```
- we confirm it have been well installed
```bash
    pre-commit --help
```

- we generate a simple config command , the name of the file should be  : **.pre-commit-config.yaml**
```bash
    pre-commit sample-config > .pre-commit-config.yaml
```

- we install the hooks :
```bash
    pre-commit install
```

- we add json check and install
```yaml
    # See https://pre-commit.com for more information
    # See https://pre-commit.com/hooks.html for more hooks
    repos:
    -   repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v2.4.0
        hooks:
        -   id: trailing-whitespace
        -   id: end-of-file-fixer
        -   id: check-yaml
        -   id: check-added-large-files
        -   id: check-ast
        -   id: check-json

```

- we can add some ckecking from another repos
```yaml
    # See https://pre-commit.com for more information
    # See https://pre-commit.com/hooks.html for more hooks
    repos:
    -   repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v2.4.0
        hooks:
        -   id: trailing-whitespace
        -   id: end-of-file-fixer
        -   id: check-yaml
        -   id: check-added-large-files
        -   id: check-ast
        -   id: check-json
    -   repo: https://gitlab.com/pycqa/flake8
        rev: 8f9b4931b9a28896fb43edccb23016a7540f5b82
        hooks:
        -   id: flake8
```

- we can add the spelling error : 
```yaml
    # See https://pre-commit.com for more information
    # See https://pre-commit.com/hooks.html for more hooks
    repos:
    -   repo: https://github.com/pre-commit/pre-commit-hooks
        rev: v2.4.0
        hooks:
        -   id: trailing-whitespace
        -   id: end-of-file-fixer
        -   id: check-yaml
        -   id: check-added-large-files
        -   id: check-ast
        -   id: check-json
    -   repo: https://gitlab.com/pycqa/flake8
        rev: 8f9b4931b9a28896fb43edccb23016a7540f5b82
        hooks:
        -   id: flake8
    -   repo: https://github.com/codespell-project/codespell
        rev: v1.16.0
        hooks:
        -   id: codespell
            name: codespell
            description: Checks for common misspellings in text files.
            entry: codespell --ignore-words ignore-spelling-words.txt readme.md code.py
            language: python
            types: [text]

```


- it is a bad idea to check pytest in pre-commit
- we can easil keep them up date using :
```bash
    pre-commit autoupdat
```