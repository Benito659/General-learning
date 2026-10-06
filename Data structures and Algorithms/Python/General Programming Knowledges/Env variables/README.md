## Env Variables
There are key-value pair stored outside of your application's source code by the underlying operating system. The main reason for this is that we don't want to hardcode the password in the Python file. 

### Definition 
- we can define environment variables directly from the terminal. (linux)
```bash
    export FOOBAR=1 
```
- this is operation system variable setting
- we can access it from python using "os" module
```python
    import os

    print(os.environ["FOOBAR"])
```
- os.environ is a dictionary. This means that there are all sorts of other variables in there and a lots as well.
- we can have a look ourself.

### DotEnv
- Instead of passing environment variables manually beforehand in a session, we can also define them in a **.env** file. 
- This is a file that contains key-value pairs that are loaded into the environment when you start your program.
- exemple of .env file
```bash
# .env
FOOBAR=10000
HELLO="WORLD"
```
- This file should never go to a **git repository**
- we will have secret, they should never go into git repository
- We should verify that the  environment variable is equal to the variable conatin in the .env variable
- We install it by doing :
```bash
    uv pip install python-dotenv
    python -m uv pip install python-dotenv
```
-  but  we will load from the **dotenv** module in Python. 
- The **override=True** argument is optional but it will make sure that the variables in the .env file will overwrite any existing variables in the environment.
- False is the default
- the function that we call that will load env from the .env file is : **load_env**
```python
    import os
    from dotenv import load_dotenv

    load_dotenv(override=True)
    print(os.environ["FOOBAR"])
    print(os.environ["HELLO"])
```


### Gitignore
- the env should never be pass to github
- **.env** should always be pass gitignore 
- it is add by default


### Values
- we can keep the .env values only and not all envriroments values inside a dictionnary
- we can use for that **dotenv_values** functions
- it put evry thing into a single dictionnary
- This way you only have to consider a config dictionary that only has the variables defined in the .env file. 
- It won't have all the other environment variables that are already set in your system.
```python
    import os
    from dotenv import dotenv_values

    config = dotenv_values(".env")
    print(config)

```