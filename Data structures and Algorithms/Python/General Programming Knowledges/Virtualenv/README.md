## Virtualenv
**virtualenv** is the ald school way of separating python project in order to prevent dependency across project

### Mutliple python
- to check python  
```bash
which python # give where python is
```
- differents python will be in differents folders

### Installation 
- From python3.4 and up you should not need to install pip. 
- This now comes pre-installed with python. 
- To install virtualenv : 
```bash
    python3.6 -m pip install virtualenv
    python3.7 -m pip install virtualenv
```
- this command say :
    - explicitly use python3.6
    - **"-m"** run the mainentry point of pip
    - run the command install of pip
    - pick virtualenv package

- To run both virtualenv :
```bash
    python3.6 -m virtualenv venv36
    python3.7 -m virtualenv venv37
```
- this command say : 
    - install a new virtualenv
    - install it in the folder(venv36, venv37)

### Virtual env
- venv36 and venv37 both act like separate vitual environement
- to start using the newly create :
```bash
    source venv36/bin/activate
    source venv37/bin/activate
    # in window 
    venv36\Scripts\activate.bat
```
- **which python** in venv36 refer to python in venv environment
- **which python3.6** give refer also to python in the venv enviroment
- but **which python3.7** in the venv37 refer to the global python3.7 (fallback)
- being careful and explicit about which version of python you use

### Source
- **source** help run the file that is a bash
```bash
    source venv36/bin/activate
```
- to stop it we run deactivate

### Pip
- pip module help to install more dependancies/packages
```bash
    python -m pip install pandas fastapi
```
- to get pip usage 
```bash
    python -m pip
```
- to get all packages that have been install
```bash
    python -m pip freeze
```
- to get all package that have been install in **requirements.txt**
```bash
    python -m pip freeze > requirements.txt
```
- to get only one dependancy
```bash
    python -m pip freeze | grep pandas
```

- to install one dependency 
```bash
    python -m pip install fastapi==0.50.0
```

- to install all requirements :
```bash
    python -m pip install -r requirements.txt 
```

- **Bad Things :**  
    - if we call pip or jupyter from the command line, and pip or jupyter are not install into the the virtuel env, it will try to find it into the superior virtual env which is not good
    - we need to make sur there are install in the  env were in
    - we need to keep the global python as simple as possible, very light this way if anything doesn't exist in the global, it will not be take into account
    - if you install locally(in the virtual env) a package that exist globally , there still a risk that it take the global
    - best way to avoid it is to deactivate and reactive after installation
    - or being explicit using *python - m* command
    