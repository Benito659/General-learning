## Lambda 
Lambda function are very simple functions. They are really easy to declare.

- Exemple : 
```python
##normal Function
def triple(x):
    return x*3

##with lambda
triple = lambda x:x*3

triple(3)
```

- Python functions are much like **normal variables**
- I can put these two functions in a list.
- These functions have not executed just, but I can keep them around to run later.
- I can put the function in a container to execute them later

```python
def double(x):
    return x*2
def add_one(x):
    return x+1

function_list = [double, add_one]


number = 1
for func in [add_one, double, add_one]:
    number = func(number)
    print(number)

```

- The main utility of lambda function ( anonymous function ) is that :
    - no need to declare it with a name
    - we create it when the function is going to be use once
    ```python
    number = 1
    for func in [lambda x:x+1, lambda x:x*2, lambda x:x+2]:
        number = func(number)
        print(number)
    ```

- Lambda without assigning it : 
    - no need to declare it with a variable
    - create the function
    - sometime it create the function and run it immediatly
    - exemple
    ```python
    print((lambda x : x + 3)(5))
    output : 
    8
    ```


- Reduce case :
    - The **functools** library contains many items that allow you to make the most out of lambda functions
    - A common example is the **reduce** function
    - **Reduce** tells us **what** we are doing while the **lambda** function tells us **how** we are doing it and **numbers** tells us to what **data** we are doing it
    ```python
    from functools import reduce
    numbers = [1, 2, 3, 4, 5]
    #normal product
    prod(numbers)
    #sum via reduce
    reduce(lambda x,y: x+y, numbers)
    #product via reduce
    reduce(lambda x,y: x*y, numbers)
    ```

- Map case : 
    - map() applies a function to every element in a list.
    ```python
    numbers = [1,2,3,4,5]
    result = map(lambda x: x*x, numbers)
    print(list(result))

    output:
    [1,4,9,16,25]
    ```


- Filtering case : 
    - filter() keeps elements that satisfy a condition.
    ```python
    numbers = [1,2,3,4,5,6]
    results = filter(lambda x:x%2==0, numbers)
    print(list(results))

    output:
    [2,4,6]
    ```

- Soting case : 
    - Lambda is very useful for sorting complex data.
    - for sorting a list of dict , it take each element → use age as sorting key
    ```python
    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 20},
        {"name": "Charlie", "age": 30}
    ]
    sorted_people = sorted(people, key=lambda x: x["age"])
    print(sorted_people)

    output :
    Bob, Alice, Charlie
    ```

- Lambda With Multiple Arguments :
    ```python
    add = lambda a,b,c: a + b + c
    print(add(1,2,3))

    output :
    6
    ```

- Lambda With Conditional Logic :
    ```python
    check = lambda x: "Even" if x % 2 == 0 else "Odd"
    print(check(4))
    print(check(7))

    output:
    Even
    Odd
    ```

- Lambda Inside List Comprehension :
    ```python
    numbers = [1,2,3,4]
    result = [(lambda x : x+3)(n) for n in numbers]
    ```

- Real Data Engineering / Data Science Use Case :
    ```python
    employees = [
        ("Alice", 5000),
        ("Bob", 3000),
        ("Charlie", 7000)
    ]
    sorted_emp = sorted(employees, key=lambda emp: emp[1])
    print(sorted_emp)
    ```

- Dataframe (**Pandas**) :
    - we're going to be taking a subset of the original dataframe with the lambda
    ```python
    import numpy as np
    import pandas as pd
    df = pd.DataFrame(np.random.normal(0,1,(10,2)))
    df.columns = ['column_a','column_b']
    df.loc[lambda d: d['column_b']>0]
    ```
    - the **loc** tells us what we're going to be taking
    - the lambda function tell us how we're going to select which rows can stay
    - lamda allow us to be flexible without having to write a lot of code 


- When NOT to Use Lambda :
    - Lambda should not be use for complex logic
    - lambda should not be use when the function is very long
    - lambda should not be use when when the function will be use multipple time (more than once)

- Lambda as a Key Function (Very Important) :
    - Many Python functions accept a key parameter
    ```python
    students = [
        ("Alice", 85),
        ("Bob", 72),
        ("Charlie", 90)
    ]

    sorted_students = sorted(students, key=lambda student: student[1])

    print(sorted_students)
    ```

- Lambda with max() and min() :
    ```python
    employees = [
        {"name":"Alice", "salary":5000},
        {"name":"Bob", "salary":7000},
        {"name":"Charlie", "salary":4000}
    ]
    highest = max(employees, key=lambda e: e["salary"])
    print(highest)
    ```

- Lambda for Multi-Level Sorting :
    - first sort by age, then by name
    ```python
    people = [
        ("Alice",25),
        ("Bob",20),
        ("Charlie",20),
        ("David",30)
    ]
    sorted_people = sorted(people, key=lambda x: (x[1], x[0]))
    print(sorted_people)

    output : 
    [('Bob',20), ('Charlie',20), ('Alice',25), ('David',30)]
    ```

- Lambda Returning a Lambda (Closures) :
    - Very powerful pattern 
    - used in functional programming and decorators.
    ```python
    adder = lambda x: lambda y: x + y
    add5 = adder(5)
    print(add5(10))

    output : 
    15
    ```

- Lambda in Dictionaries (Strategy Pattern) : 
    -   use in **calculators**, **API routing**, **command systems**
    ```python
    operations = {
        "add": lambda a,b: a+b,
        "sub": lambda a,b: a-b,
        "mul": lambda a,b: a*b
    }

    print(operations["mul"](3,4)) 
    ```

- Lambda for Custom Object Sorting : 
    ```python
    class Product:
        def __init__(self,name,price):
            self.name = name
            self.price = price
        
    products = [
        Product("Laptop",1000),
        Product("Phone",500),
        Product("Tablet",700)
    ]

    sorted_products = sorted(products, key=lambda p: p.price)
    ```

- Lambda vs List Comprehension :
    - List comprehension is usually more readable.
    ```python
    list(map(lambda x: x*x, numbers))

    [x*x for x in numbers]
    ```



- **Golden Rule** :
    - use lambda for keys=
    - use lambda for map()
    - use lambda for filter()
    - use lambda for reduce()
    - use lambda  for small transformation or function use only once