## Decorators 
Decorators are functions that make other functions better. They add behaviors to other functions

- Functions
    - Functions can receive funtions as input
    - exemple : 
    ```python
    def apply(func,a,b):
        func(a,b)

    def add(a,b):
        return a+b
    
    def sub(a,b):
        return a-b
    
    apply(add, 1, 2), apply(sub, 1, 2)
    ```
    - Function can return function as output
    - exemple : 
    ```python 
    def power(n):
        def func(number):
            return number**n
        return func
    
    pow2 = power2(2)
    pow3 = power3(3)
    pow2(3), pow3(3)

    output : 
    (9, 27)
    ```

- Behavior : 
    - we will combine it two idea to create two functions that have close behaviour
    - a function is pass as input
    - we declare inside this function a new function that is being return with additional behavior
    ```python
    import time
    import random
    def stopwatch(f):
        def func():
            tic = time.time()
            result = f()
            print(f"this function took :{time.time() - tic}")
            return result
        return func
    
    def sleep_random():
        time.sleep(random.random())
        return "Done !"

    time_sleep = stopwatch(sleep_random)

    sleep_random()
    time_sleep()
    ```
    - we will allow both to have similar inputs
    ```python
    import time
    import random
    def stopwatch(f):
        def func(*args, **kwargs):
            tic = time.time()
            result = f(*args,**kwargs)
            print(f"this function took :{time.time() - tic}")
            return result
        return func
    
    def sleep_random(s=1):
        time.sleep(s+ random.random())
        return "Done !"

    time_sleep = stopwatch(sleep_random)

    sleep_random(s=2)
    time_sleep(s=2)
    ```

- Decorate : 
    - it is better for use the function that decorate in multiple place of the code base
    - we use "@" for the new fontion to add behavior to the new function
    - the new function (sleep_random will have all behavior)
    ```python
    import time
    import random
    def stopwatch(f):
        def func(*args, **kwargs):
            tic = time.time()
            result = f(*args,**kwargs)
            print(f"this function took :{time.time() - tic}")
            return result
        return func
    
    @stopwatch
    def sleep_random(s=1):
        time.sleep(s+ random.random())
        return "Done !"
    
    sleep_random(1) , sleep_random(2)
    ```

- Wraps : 
    - When we wrap a function with a decorator we might loose information from the original function. One of the things we miss out on is the docstring.
    - we can make sure that the docstring is kept intact by using @wraps.
    - wrap is internally propagating extra informations from original function to func including doc
    -  it is receiving original function f
    ```python
    import time
    import random
    from functools import wraps
    def stopwatch(f):
        @wraps
        def func(*args, **kwargs):
            tic = time.time()
            result = f(*args,**kwargs)
            print(f"this function took :{time.time() - tic}")
            return result
        return func
    
    @stopwatch
    def sleep_random(s=1):
        """ thi function sleep for a least 's' seconds"""
        time.sleep(s+ random.random())
        return "Done !"
    
    help(sleep_random)

    ?sleep_random
    ```


- Stack :
    - when we have to or more decoratore , we can stack them on top of each other
    - the order in wich we call is important
    - it's prefarable to have general decorator so that the order we put here does not matter
    ```python
    import time
    import random
    from functools import wraps

    def print_call1(f):
        @wraps(f)
        def func(*args, **kwargs):
            print(f"print-call 1 args: {args}")
            result = f(*args, **kwargs)
            return result
        return func


    def print_call2(f):
        @wraps(f)
        def func(*args, **kwargs):
            print(f"print-call 2 args: {args}")
            result = f(*args, **kwargs)
            return result
        return func

    @print_call2
    @print_call1
    @print_call2
    @print_call1
    def sleep_random(s):
        """This function sleeps at least for `s` seconds."""
        return time.sleep(s + random.random()/100)

    sleep_random(1.5)

    ```

- Inputs
    - We can also have decorators that accept inputs. This makes for even more expressiveness. You do need to pay attention when you're declaring them though.
    ```python
    import time
    import random
    from functools import wraps

    def loggg(show_name=True, show_time=True):
        def stopwatch(f):
            @wraps(f)
            def func(*args, **kwargs):
                tic = time.time()
                result = f(*args, **kwargs)
                log_text = "call"
                if show_name:
                    log_text = f"{log_text} {f.__name__}"
                if show_time:
                    log_text = f"{log_text} time:{time.time() - tic}"
                print(log_text)
                return result
            return func
        return stopwatch

    @loggg(show_name=False, show_time=True)
    def sleep_random(s):
        """This function sleeps at least for `s` seconds."""
        return time.sleep(s + random.random()/100)

    sleep_random(1)

    ```

