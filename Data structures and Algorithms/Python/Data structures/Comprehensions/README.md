## Comprehensions
In python a comprehension is a short , powerful and readable way to create a new collection (like a list, set, or dictionary) from an existing iterable (list, tuple, range, etc). it allow you to write compact and expressive code instead of using traditinal for loops
```python
old_list = [ 1, 2, 3, 4, 5]
new_list = []
for i in old_list :
    new_list.append( i * 2 )
new_list
[i*2 for i in old_list]
```
- if statement for filtering :
    ```python
    [i*2 for i in old_list if i%2 == 0 ]
    ```
- if statement for iterative value calculation
    ```python
    [i*2  if i >2  else i>3 for i in old_list ]
    ``` 
- enumerate :
    - **enumerate()** is a generic function that transform an iterable(string, list, dict, set)  by looping over all item of the itarable and give an object that is compose of many tuple that correspond to each item of the iterable with they index.
    ```python
    for tup in enumerate('abcde') :
        print(tup)
    
    output :
    (0, 'a')
    (1, 'b')
    (2, 'c')
    (3, 'd')
    (4, 'e')
    ``` 
    - unpack tup element of enumerate :
    ```python
    for idx, char in enumerate('abcde') :
        print(idx, char)
    ``` 

    - unpacking and filtering from a list comprehension :
    ```python
    [char for idx, char in enumerate('abcde') if idx%2 == 0]
    ``` 

    - exemple :
    ```python
    [
        char.upper() if char in 'aeuio' else char 
        for idx, char in enumerate('abcde') 
        if idx%2 == 0
    ]
    ```

- nested for loop (double for loop)
    ```python
    for i in range(5):
        for j in range(i):
            print((i,j))
    output :
    (1,0)
    (2,0)
    (2,1)
    (3,0)
    (3,1)
    (3,2)
    (4,0)
    (4,1)
    (4,2)
    (4,3)
    ```
    - with comprehension :
        ```python
        [(i,j) for i in range (5) for j in range (i)]
        #the output i a list
        ```
    - with comprehension and an if statement in fist loop :
        ```python
        [(i,j) for i in range(5) if i>2 for j in range (i)]
        ```
    - with comprehension and an if statement in two loops :
        ```python
        [(i,j) for i in range(5) if i>2 for j in range (i) if j > 2]
        ```

- Get a **set** with comprehension :
```python
{ c for c in 'abceabce'}

output :
{'a', 'b', 'c', 'e'}
```

- Get a tuple with comprehension :
```python
tuple(c for c in 'abceabce')

output :
( 'a', 'b', 'c', 'e', 'a', 'b', 'c', 'e')
```

- Create an dictionary :
    ```python
    {idx:char for idx,char in enumerate('abceabce')}

    output :
    ( 0: 'a', 1: 'b', 2: 'c', 3: 'e', 4: 'a', 5: 'b', 6: 'c', 7: 'e')
    ```
    - Dictionary Key are unique not like value
    - Create an dictionary with filtering :
        ```python
        {idx:char for idx,char in enumerate('abceabce') if char in 'abc'}

        output :
        ( 0: 'a', 1: 'b', 2: 'c', 3: 'a', 4: 'b', 5: 'c')
        ```


- unpacking a complex structure(double nested) like a list of tupple :
    ```python
    arr = [('a',1), ('b',2), ('c',2)]
    for idx, (char, i) in enumerate(arr) :
        print(idx, char, i)
    
    output :
    0 a 1
    1 b 2
    2 c 2
    ```
    - Create a list of dictionnary from this structure :
        ```python
        [{key: value, 'i' : idx} for idx , (key, value) in enumerate(arr)]
        ```

- d.keys : get keys value of a dictionary
- d.values : get differents values of a dictionary
- d.items help get both

- zip help to repackage in python,  It allows you to "zip" lists together like a zipper.
    - exemple : 
        ```python
        [(a,b) for a,b in zip([1,2,3], [4,5,6])]
        
        output :
        [(1,4), (2,5), [3,6]]
        ```
    - exemple : 
        ```python
        [(a,b,c) for a,b,c in zip([1,2,3], [4,5,6], [7,8,9])]
        ```



