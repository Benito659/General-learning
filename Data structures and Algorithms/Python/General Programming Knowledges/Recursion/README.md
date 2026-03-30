## Recursion
Recursion in Python is a programming technique where a function calls itself to solve a problem step by step until it reaches a stopping point. You solve a big problem by solving a smaller version of the same problem, again and again, until it becomes very simple.


### Simple : Counting Down
- Count numeral in reverse order to zero

```python
    def countdown(n):
        if n == 0:          
            print("Done")
        else:
            print(n)
            countdown(n - 1)  
```
- In this case we will

### Classic : Factorial
- Factorial is a mathematical operation where a positive integer is multiplied by every whole number below it down to 1.

```python
    def factorial(n):
        if n == 0:       
            return 1
        else:
            return n * factorial(n - 1)
```

### Classic : Fibonacci
The Fibonacci problem involves finding the n-th number in a sequence where each number is the sum of the two preceding ones

```python
    def fibonaci(n):
        if n <= 1 :
            return O
        else :
            return fribonaci(n-1) +fibonaci(n-2)
```

### Complex :  Frog Jump puzzle
We want to calculate how many way are they for a  frog to jump from one lily pad, taking into account we want to vary the number of lily pads, and vary the number of lily pads it can jumps
- It ressemble to a graph or three problem
- First approach :
```python
    def n_paths(start=1, end=5):
        if start > end :
            return 0
        if start == end :
            return 1
        return n_paths(start = start+1, end = end) + n_paths(start=start+2, end=end)
```

- Second approach : Improve time performance with cache
    - Measure time as the number of jump pads increase :
    ```python
        for e in [10, 30, 31, 32, 33]:
            tic=time.time()
            n_paths(start=1, end=e)
            print(f"end={e} took {time.time() - tic}")
    ```
    - Reduce time with cache :
    ```python
        from functools import lru_cache
        @lru_cache(1000)
        def n_path(start=1, end=5):
            if start > end :
                return 0
            if start == end :
                return 1
            return n_paths(start=start+1, end=end)+ n_paths(start=start+2, end=end)
    ```
    - e can use another parameters that will list all type of jumps it can make :
    ```python
        from functools import lru_cache

        @lru_cache(1000)
        def n_paths(start=1, end= 5, jumps = (1,2)):
            if start> end :
                return 0
            if start == end :
                return 1
            return sum([n_paths(start=start +j , end = end) for j in jumps])

    ```


### When to Use Recursion
- The hard part is not writing down the function, it is recognising that you are dealing with a problem that is well suit for recursion.
- Being good at rephrasing problem
- Recursion is best for problems that are naturally divide-and-conquer problems, such as:
    - Tree traversal
    - File system navigation
    - Searching algorithms
    - Sorting algorithms
    - Mathematical sequences
    - Backtracking problems
    - Graph algorithms
    
    Very common in:
    - Data structures
    - Algorithms
    - Techncal interviews
    - Competitive programming