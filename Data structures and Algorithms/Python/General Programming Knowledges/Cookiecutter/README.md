## Cookiecutter
Cookiecutter is an opensource, cross-platform comand-line utility written in python that automaticly create projects from predefined projects templates. It serve as a scaffolding tool, allowing software engineers and data scientists to skip the tedious, repetitive tasks of setting up file structures, configurations, and boilerplate code.

### Installation
```bash
    pip install cookiecutter
```

### The JSON FILE
- To install cookiecutter
- Cookiecutter is defined with a json file **cookiecutter.json**. You can use it to define variables which will be used later in the project that is created.
- The folder name of project that serve  as a boilerplate is **{{cookiecutter.project}}**. When we will run cookie cutter, the base project we will create will have *cookiecutter.project* value in the JSON file.
- Content of the **cookiecutter.json** file:
```json
    {
    "project": "project"
    }
```
- Content of the **{{cookiecutter.project}}** folder :  **readme.md**
- Content of the **readme.md** folder : # readme of {{cookiecutter.project}}
- to run cookiecutter you type this command :
```bash
    cookiecutter .
    python -m cookiecutter .
```
- Diagram of how cookiecutter work : 
![cookie cutter diagram](/Data%20structures%20and%20Algorithms/Python/General%20Programming%20Knowledges/Cookiecutter/Assets/diagram-cookiecutter.png)


### Author of a CoockieCutter
- we can define an author by adding an "author" line in the json file
```json
    {
    "project": "project",
    "author": "author"
    }
```
- exemple of readme that use it 
```md
    # readme of {{cookiecutter.project}}

    This package was made by {{cookiecutter.author}}.
```
- all this variable can be reset when we run cookiecutter 
- when not running that we can use the default value define in the json


### Adding Folders
- You can add folders in cookiecutter as well to give your project even more structure. 
- you simply add a new folder in your project
- the name of the folder is : **{{cookiecutter.project_slug}}**
- i'll define it in the json file :
- we can get rid of space in those file
```json
    {
        "project":"project",
        "author":"author",
        "project_slug":"{{cookiecutter.project.lower().replace(" ","_")}}"
    }
```

### Conditionals and Sets
- You can also run logic inside of variable definitions 
- you can then run if and else
- **cookiecutter.json**
```json
    {
        "project": "project",
        "author": "author",
        "project_slug": "{{cookiecutter.project.lower().replace(' ', '_')}}",
        "license": ["MIT", "BSD"]
    }
```

- **readme**
```md
    # readme of {{cookiecutter.project}}
    
    This package was made by {{cookiecutter.author}}.

    {%- if cookiecutter.licence== "MIT" -%}
    This is a MIT License

    {%- elif cookiecutter.licence=="BSD" -%}
    This is a BSD Licence

```


### Define a python file
- Let's consider adding a **setup.py** file to our project with cookiecutter.
- we define the file in the folder 
```python
    from setuptools import setup
    setup(
        name=""{{cookiecutter.project_slug}}"",
        version="0.0.1"
    )
```


### Share it with people
- when we run **cookiecutter** command, following specify location
- when we have this : cookiecutter git@gitlab.com:koaning/super-basic-cookie.git
- we can run it directly from gitlab
- we can store cookiecutter on github and gitlab to share it
