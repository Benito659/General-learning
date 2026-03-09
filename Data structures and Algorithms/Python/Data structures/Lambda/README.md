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
    - 

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