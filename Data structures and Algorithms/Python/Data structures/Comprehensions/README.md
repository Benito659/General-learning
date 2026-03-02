## Comprehensions
In python a comprehension is a short , powerful and readable way to create a new collection (like a list, set, or dictionary) from an existing iterable (list, tuple, range, etc). it allow you to write compact and expressive code instead of using traditinal for loops

    ```python
    #exemple without comprehension
    old_list = [ 1, 2, 3, 4, 5]
    new_list = []
    for i in old_list :
        new_list.append( i * 2 )
    new_list
    #exemple with comprehension
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
