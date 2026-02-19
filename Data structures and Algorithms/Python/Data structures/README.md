# Python Data Structures
This folder list all differents data structures that we can find in python. 

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
    def add(a, b, c):
        return a + b + c

    numbers = [1, 2, 3]
    print(add(*numbers))  # unpacks list as a=1, b=2, c=3
    ```
- Can be use for Merging sets:
    ```python
    s = {*a, *b}  # {1, 2, 3, 4}
    ```

- Can be use for Copying:
    ```python
    new_list = [*old_list]
    ```



## Kwargs
