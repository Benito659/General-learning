## Black
Black is a python library that help to do python code style formatting. It is a tool that take the code and ensure it have one and only one  style

### Installation
```bash
python -m pip install black
```

### Usage
- We are working on a file call "code.py".
```python
    list_of_numbers = [
        1,
        2,
        3
    ]

    large_dictionary = {1:2, 3:4, 5:6, 7:8, 9:10, 11:12, 13:14, 15:16, 17:18, 19:20, 21:22, 23:24}
``` 

- To apply the file we use :
```bash
    python -m black copy.py
    black copy.py
```

- Black change functions , list and objects in general 

- Black  dont check evry thing fo exemple **import**

- Black is very opinionated

- Only customisation of black is line lenght 

```python
    black --line-length 100 code.py
```

- we want to ensure black will run before evry commit

- we edit the pre-commit config file  "pre-commit-config.yaml"

```
    repos:
    - repo: https://github.com/psf/black
        rev: stable
        hooks:
        - id: black
            language_version: python3.6
```