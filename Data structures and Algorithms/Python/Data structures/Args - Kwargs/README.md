## Args
```python
def my_function(a, b, *args):
    print(args)
```

- ***args** : the * before args tells Python to collect all the extra positional arguments into a tuple named args
- **args** is a tuple 
- **args** is a convention can be name with another name
- It’s using a special Python syntax called **arguments unpacking**
- It's also called **variadic positional arguments**
- **\*** in ***args** is called the **splat operator**, or more formally, **iterable unpacking**
- It take all extra positional arguments passed to this function and pack them into a tuple
- Types that can be unpacked with *: List , Tuple, Set, Strings (each character is treated as an element), Any iterable (even generators!)
- Can be use In function definitions (packing) : The * in *args packs any number of positional arguments into a tuple.
    ```python
    def print_items(*args):
        print(args)

    print_items(1, 2, 3)          # ints
    print_items("a", "b", "c")    # strings
    print_items([1,2], [3,4])     # lists
    print_items({"x":1}, {"y":2}) # dictionaries
    ```
- Can be use in function calls (unpacking) :
    ```python
    def add(a, b, c):
        return a + b + c

    numbers = [1, 2, 3]
    print(add(*numbers))  # unpacks list as a=1, b=2, c=3 
    ```
- Unpacks the lists
    ```python
    print_items(*[1,2], *[3,4])  
    (1, 2, 3, 4)
    ```
- Can be use for Merging Lists :
    ```python
    list1 = [1, 2]
    list2 = [3, 4]
    list3 = [5, 6]

    merged = [*list1, *list2, *list3]
    print(merged)
    ```
- Can be use for Merging sets:
    ```python
    s = {*a, *b}  # {1, 2, 3, 4}
    ```

- Can be use for Copying:
    ```python
    new_list = [*old_list]
    ```

- Positional argument must follow keywords argument and not inverse


## Kwargs
```python
def my_function(a, b, *args, keyword=True, **kwargs):
    print(args)

def greet(**kwargs):
    print(kwargs)

greet(name="Junior", country="Senegal", role="Data Engineer")

Output :
{'name': 'Junior', 'country': 'Senegal', 'role': 'Data Engineer'}
```

- **Keyword argument** is an argument that have both a name as well as a value attached immediatly
- **kwargs** = keyword arguments, ** = tells Python to collect them into a dictionary
- it will pick up any named argument while ***args** pick up any unamed argument
- Accessing values inside kwargs :
```python
def greet(**kwargs):
    if "name" in kwargs:
        print(f"Hello {kwargs['name']}")
greet(name="Junior")

Output :
Hello Junior
```
- Usage of **kwargs :
    - Don’t know in advance how many keyword arguments will be passed
    - Build frameworks, APIs, decorators, or reusable utilities
    - Build flexible functions
     ```python
    def create_user(**kwargs):
        user = {}
        for key, value in kwargs.items():
            user[key] = value
        return user
    u = create_user(name="Junior", stack="Data", level="Mid")
    print(u)
    ```
- Order in function definition :
    When combining:
    ```python
    def func(positional, *args, **kwargs):
        pass
    ```
    The correct order is:
    - Normal parameters
    - *args
    - **kwargs

- Unpacking with ** :
    Python converts the dictionary into keyword arguments.
    ```python
    def greet(name, country):
        print(name, country)
    data = {"name": "Junior", "country": "Senegal"}
    greet(**data)
    ```

- Real-world example (As Data Engineer you build configurable pipelines) :
    ```python
    def load_data(source, **options):
        print("Source:", source)
        print("Options:", options)

    load_data(
        "postgres",
        host="localhost",
        port=5432,
        schema="analytics"
    )
    ```

- Accepting Flexible Parameters (User profiles, Config objects, Dynamic metadata) : 
    - Don’t know in advance what parameters will be passed
    ```python
    def create_profile(**kwargs):
        return kwargs

    user = create_profile(name="Junior", role="Data Engineer", country="Senegal")
    print(user)
    ```

- Passing Configuration Options ( common in data engineering and machine learning) (Database connections, API clients, Spark configurations, ETL jobs): 
    ```python
    def connect_database(**config):
        print("Connecting with:", config)

    connect_database(
        host="localhost",
        port=5432,
        database="analytics",
        ssl=True
    )
    ```

- Forwarding Arguments to Another Function (Wrappers, Middleware, Decorators, Inheritance) :
    ```python
    def wrapper(**kwargs):
        return process(**kwargs)

    def process(name, age):
        return f"{name} is {age}"

    print(wrapper(name="Benito", age=25))
    ```

- Default Values with Override Capability (Systems where you have default configs but allow overrides) :
    ```python
    def send_email(**kwargs):
        defaults = {
            "sender": "admin@company.com",
            "priority": "normal"
        }
        defaults.update(kwargs)
        return defaults

    print(send_email(priority="high"))
    ```

- Validation of Dynamic Fields (Form validation, API request validation, Data ingestion pipelines) :
    ```python
    def register_user(**kwargs):
        required = ["username", "password"]

        for field in required:
            if field not in kwargs:
                raise ValueError(f"{field} is required")

        return "User registered"

    register_user(username="Junior", password="1234")
    ```

- Used in Class Constructors (ORM models, Dynamic objects, Data models) :
    ```python
    class User:
        def __init__(self, **kwargs):
            for key, value in kwargs.items():
                setattr(self, key, value)

    u = User(name="Junior", role="Engineer")
    print(u.name)
    ```

- Used in Inheritance (Advanced OOP) (Framework development, Extensible architectures) :
    ```python
    class Base:
        def __init__(self, **kwargs):
            print("Base init", kwargs)

    class Child(Base):
        def __init__(self, name, **kwargs):
            super().__init__(**kwargs)
            self.name = name

    Child(name="Junior", age=25)
    ```

- Decorators (Advanced & Powerful) (Logging, Authentication, Monitoring, Performance tracking) : 
    ```python
    def logger(func):
        def wrapper(*args, **kwargs):
            print("Arguments:", kwargs)
            return func(*args, **kwargs)
        return wrapper

    @logger
    def greet(name):
        return f"Hello {name}"

    greet(name="Junior")
    ```

- Dictionary Unpacking (API responses, JSON data, Database rows) :
    ```python
    data = {"name": "Benito", "country": "Senegal"}

    def greet(name, country):
        print(name, country)

    greet(**data)
    ```

- Framework-Level Usage :
    It allows libraries to:
    - Add new parameters without breaking code
    - Maintain backward compatibility
    - Build scalable APIs


- Unpacking ( dictionaries for Kwargs and  list for args) : 
    ```python
    def function(a, b , *args, keyword=True, **kwargs):
        print(a,b)
        print(args)
        print(keyword)
        print(kwargs)
    
    d = {'param_a': 43,'param_b':56}
    function(1,2, *[5,4,6], param=42,**d)

    output :
    1 2
    (5,4,6)
    True
    {'param': 42, 'param_a':43, 'param_b':56}
    ```
    - 
