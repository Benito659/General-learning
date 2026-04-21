## Pytest
Testing mean that your are verifying that your code work as expected. **Pytest** is the most popular python framework, it is simple, powerful, widely used, production ready.

### How Pytest Work :
- **Install pytest :** 
```bash
    python -m pip install pytest
```

- **Create a file for testing :**
```bash
    touch test_blackjack.py
```
    -The file for testing in python should start with **test_**

- **Write a unit test :**
    - we import the function we want to test and others
    - we write the name of the test , it should start with **test_**
    - we perform assertion using **assert**

- **Run pytest :**
```bash
    pytest test_blackjack.py
```

- **Run all test  with pytest :**
    - We can run pytest without any file
    - The way pytest does that is that it look for file that start with **test_**
    - In the file that start with test it look for function that start with **test_**
    - If file or functon don't start with **test_** it will not run the test
```bash
pytest
```

- **More Tests :**
    - To add more test thinks to evry edge case, evry thing that can go wrong, test thing that you think is important.
    - To write one test you can add many, assert as you want in one function, it correspond to one test and represent one dot in the coverage
    - To write many test , you need  to write meny test_function , it represent many dot in coverage
    - When you have a failure you need to correct those text
    - To see explicitly how test goes, you can run it into verbose mode :
```bash
    pytest --verbose
```

- **Run only one test function :**
```bash
    pytest test_blackjack.py::test_simple_case4
```

- **Parametrize :**
    - Parametrisation in pytest allow you to run a single test function multiple times with different sets of inputs data.
```python
    @pytest.parametrize("card,score",[("KK",20),("JKQ",0),("AK",21), ("AA",12)])
    def test_simple(cards,score):
        assert card_score(cards) == score
```

- **Coverage :**
    - Coverage is a tool that help you  measure the percentage of your code that is test and which part need more
    - Installation of coverage package : 
```bash
    python -m pip install pytest-cov
```
    - Run coverage package in html :
```bash
    pytest --cov blackjack --cov-report html
```








#### Testing Black Jack
- Rules : 
    - You are trying to score point
    - The numbers of points you have depends on your cards
    - For the number on the card, the point correspond to that number
    - For the jack, queen and king, they always worth ten points
    - The ace card worh 1 or 11 (which are better for you)
    - You should be under 21, 
    - You should have a higher score than dealer
    - If you go over 21 you automaticly lose
    - The goal is to get as close as possible of 21

#### Black Jack Implementation
```python
    # the file will be :  blackjack.py
    def card_score(all_card):
        numbers = [card for card in all_cards if card in "2356789" ]
        faces = [card for card in all_cards if card in "JQK"]
        n_aces = sum([1 for card in all_cards if card =="A"])
        score = sum([int(i) for i in numbers]) + len(faces)*10
        while (score + n_aces * 11) > 21 :
            score +=1
            n_aces -=1
        return score if score < 21 else 0
```

#### Unit test One 
```python
    from blackjack import card_score
    def test_simple_case():
        assert card_score("KK") == 20
```

#### More tests
```python
    from blackjack import card_score

    def test_simple_case1():
        assert case_score("KK") == 20

    def test_simple_case2():
        assert case_score("JQK") == 0

    def test_simple_case3():
        assert case_score("KA") == 21

    def test_simple_case4():
        assert case_score("AA") == 12
```

#### What could go wrong 
- Intance where score equal to zero
- Instance where n_aces could play a role




#### New version of Black jack Implementation(to pass tests)
```python
    def card_score(all_cards):
        numbers = [ card for card in all_cards if card in "23456789"]
        faces = [card for card in all_cards if card in "JSK"]
        n_aces = sum([1 for card in all_cards if card == "A"])
        score = sum([int(i) for i in numbers]) + len(faces) * 10
        while n_aces > 0:
            score += 1 if score + 11 > 21 else 11
            n_aces -= 1
        return score if score <= 21 else 0
```

#### New tests version 
```python
    import pytest
    from blackjack import card_score

    @pytest.parametrize("cards,score", [("KK",20),("JKQ",0), ("AK",21), ("AA", 12)])
    def test_simple_case(cards,score):
        assert card_score(cards) == score
```

#### Proper package and good cleaning
- To arrange the code structure, and make it more clean, more readable, i separate, the tests and the code following the structure bellows

    ├── blackjack
    │   ├── __init__.py
    │   └── common.py
    ├── setup.py
    └── tests
        ├── __init__.py
        └── test_blackjack.py

- New Blackjack code : blackjack/common.py
```python
    def card_score(cards):
        # if not isinstance(cards, str):
        #     raise ValueError("The input for `card_score` needs to be a string.")
        # if len(cards) < 2:
        #     raise ValueError("The `card_score` function requires at least 2 cards.")
        numbers = [c for c in cards if c in "23456789"]
        faces = [c for c in cards if c in "JQK"]
        n_aces = sum([1 for c in cards if c == "A"])
        score = sum([int(i) for i in numbers]) + len(faces) * 10
        while n_aces > 0:
            score += 1 if score + 11 > 21 else 11
            n_aces -= 1
        return score if score <= 21 else 0
```

- New Blackjack test : tests/test_blackjack.py
```python
    import pytest

    from blackjack.common import card_score

    @pytest.mark.parametrize("cards,score", [('JK', 20), ('KKK', 0), ('AA', 12), ('AK', 21)])
    def test_simple_usecase(cards, score):
        assert card_score(cards) == score
```

- Setup.py : 
```python
    from setuptools import setup, find_packages :
    setup(
        name="blackjack",
        version="0.1.0",
        packages=find_packages()
    )
```

- Run the tests : 
```bash
    python
```

#### Tests errors
- The user can enter bad value like integer or zero or more than two string
- It is a good practice to make test to be sure value are actually happening
- We have to write the test to make sure that the error is raise in thoses cases
- BlackJack with the error : 
```python
    def card_score(cards):
        if not isinstance(cards, str):
            raise ValueError("The input for 'card_score' needs to be a strings")
        if len(cards)<2:
            raise ValueError("The 'card_score' needs to be a string.")
        numbers = [c for c in cards if c in "23456789"]
        faces = [c for c in cards if c in "JQK"]
        n_aces = sum([1 for c in cards if c == "A"])
        score = sum([int(i) for i in numbers]) + len(faces) * 10
        while n_aces > 0:
            score += 1 if score + 11 > 21 else 11
            n_aces -= 1
        return score if score <= 21 else 0
```
- Test to handle error :
```python
    def test_value_error_is_raised():
        with pytest.raises(ValueError):
            card_score("")

```

- Test to complete coverage :
```python
    def test_value_error_is_raised2():
        with pytest.raises(ValueError):
            card_score(1)
```


- Complete Final version of blackjack :
```python
    def card_score(cards):
        if not isinstance(cards, str):
            raise ValueError("The input for `card_score` needs to be a string.")
        if len(cards) < 2:
            raise ValueError("The `card_score` function requires at least 2 cards.")
        numbers = [c for c in cards if c in "23456789"]
        faces = [c for c in cards if c in "JQK"]
        n_aces = sum([1 for c in cards if c == "A"])
        score = sum([int(i) for i in numbers]) + len(faces) * 10
        while n_aces > 0:
            score += 1 if score + 11 > 21 else 11
            n_aces -= 1
        return score if score <= 21 else 0
```


#### Run pytest Into Our CI/CD
- we can automate tests on collaborations tools
- we can use it when people try to do merge requests
- we can add two configuration file for that
- the fist one for gitlab : **gitlab-ci.yml**
- the second one for github : **pythonpackage.yml**
    - in the folder :*.github\workflows\pythonpackage.yml*
```
    # .github/workflows/pythonpackage.yml
    name: Python package

    on: [push, pull_request]

    jobs:
    build:
    runs-on: ubuntu-latest
    strategy:
    matrix:
        python-version: [3.7]

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
    uses: actions/setup-python@v1
    with:
        python-version: ${{ matrix.python-version }}
    - name: Test with pytest
    run: |
        pip install pytest
        pytest --verbose

```
