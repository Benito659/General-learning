## Github actions
GitHub Actions is a built-in automation platform that allows developers to automate, customize, and execute software development workflows directly inside a GitHub repository. It is primarily used as a continuous integration and continuous delivery (CI/CD) platform to automatically build, test, and deploy code whenever changes are made.

- it helps to ensure code work evry time a person do a pull request

### Configuration
- to add github actions to our project we add a new folder call **.github/worflows/unitest.yml**
- we can specify on wich action it will run ex: **pull request**
- we can specify the branch on wich it will be applied to **main**
- then we specify differents steps we are running for jobs
- the firts job is the job **build**
- the fist steps  **uses** pull the code from the repos
- the second step run python 
- the next step install a python environnement
- the last step run the pytest
```yml
name: Python Unit Tests

on:
  pull_request:
    branches:
    - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.7'
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install -r requirements.txt
        python -m pip install -r dev-requirements.txt
    - name: Test with pytest
      run: |
        pytest --verbose

```


### Prevent merge
- i can, prevent a merge from another branch on github by doing some modifications in github parameters
- Settings > Branches > Branches Protections Rules > Add a rule > require status check before merging > Build (name of job i want to run before to ensure)

### Matrix
- A matrix strategy in GitHub Actions allows you to run a single job multiple times using different variable combinations.
- Instead of copying and pasting the same code to test your application on multiple operating systems or language versions, you define the variables in a "matrix". GitHub Actions will then automatically generate and execute separate, parallel jobs for every possible combination.

- we define the stratgy under the runs-on in github actions
- we then specify matrix and then we can specify differents python version or differents os we wan to test
- ubuntu run quicly than, window ( install step is quiker in ubuntu) 

```yml
name: Python Unit

on:
  pull_request:
    branches:
    - main

jobs:
  build:
    strategy:
      matrix:
        python-version: ['3.7', '3.8', '3.9', '3.10']
        os: [ubuntu-latest, windows-latest]
    runs-on: ${{ matrix.os }}

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install -r requirements.txt
        python -m pip install -r dev-requirements.txt
    - name: Test with pytest
      run: |
        pytest --verbose

```


### Dependencies
- dependencies generally refer to job dependencies, which dictate the execution order of individual tasks in a workflow. By default, multiple jobs within a single workflow file run concurrently. Setting up a dependency ensures that a specific job pauses and waits until its prerequisite jobs successfully finish executing.
- if a previous job fail it following job in dependency won't run
- we add under runs-on anoter option **needs : [style, build]** it specify in a job other dependency job that needs to be run before
```yml
name: Python Unit

on:
  pull_request:
    branches:
    - main

jobs:
  style:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.7"
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install -r requirements.txt
        python -m pip install -r dev-requirements.txt
    - name: Test with pytest
      run: |
        flake8

  build:
    strategy:
      matrix:
        python-version: ['3.7', '3.8', '3.9', '3.10']
        os: [ubuntu-latest]
    runs-on: ${{ matrix.os }}

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install -r requirements.txt
        python -m pip install -r dev-requirements.txt
    - name: Test with pytest
      run: |
        pytest --verbose

  windows:
    strategy:
      matrix:
        python-version: ['3.7', '3.8', '3.9', '3.10']
        os: [windows-latest]
    runs-on: ${{ matrix.os }}
    needs: [style, build]

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install -r requirements.txt
        python -m pip install -r dev-requirements.txt
    - name: Test with pytest
      run: |
        pytest --verbose

```


### Schedule
- It is a workflow trigger that automatically runs a pipeline at specific times using POSIX cron syntax. 
- This allows you to execute jobs routinely—such as nightly builds, weekly dependency updates, or daily code cleanups—independent of repository activity like code pushes or pull requests.
```yml
on:
  schedule:
    - cron: "0 0 * * *"
```

```yml
name: Cron Test Dependencies

on:
  schedule:
    - cron: "0 0 * * *"

jobs:
  cron:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        python-version: [3.7]
        os: [macos-10.15, ubuntu-latest, windows-latest]
        pre-release-dependencies: ["--pre", ""]
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v1
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        python -m pip install wheel
        pip install ${{ matrix.pre-release-dependencies }} scikit-lego
        pip freeze
    - name: Test with pytest
      run: |
        pip install -e ".[test]"
        pytest

```

