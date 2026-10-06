## YIELD
**yield** keyword pauses a function's execution and returns a value to the caller, turning that function into a generator object. Unlike return, which destroys the function's state and terminates it entirely, yield saves the exact state of the function so it can resume right where it left off when the next value is requested.

### Main Use Cases
- Handling Massive Datasets: Reading gigantic log files or databases line by line without loading the entire file into RAM.
- Infinite Sequences: Creating a continuous stream of data (like a Fibonacci series) without causing memory crashes.
- Performance Optimization: Generating items on demand so you do not waste CPU cycles creating unused data

### Explaination
- The yield keyword turns a function into a function generator.
- The function generator returns an iterator.
- The code inside the function is not executed when they are first called, but are divided into steps, one step for each yield, and each step is only executed when iterated upon.
- Unlike the return keyword which stops further execution of the function, the yield keyword returns the result so far, and continues to the next step.
- The return value will be a list of values, one item for each yield.
```python
    def myFunc():
        yield "Hello"
        yield 51
        yield "Good Bye"

    x = myFunc()

    for z in x:
        print(z) 
```

```python
    y = 0

    def myFunc():
        global y
        y = 10
        yield "Hello"
        y = 20
        yield 51
        y = 30
        yield "Good Bye"

    #The function is called:
    x = myFunc()

    #But y is still 0:
    print("At this point, y is still:", y)

    #Run the first iteration:
    next(x)

    #And y becomes 10:
    print("Now, y is:", y)

    #Run another iteration:
    next(x)

    #And y becomes 20:
    print("Now, y is:", y)

    #Run another iteration:
    next(x)

    #And y becomes 30:
    print("Now, y is:", y) 
```