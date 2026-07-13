## Stamina
Stamina is a library that help python program to implement a retry mechanism because sometimes a Python function can fail because of something that is outside of our control. The most typical example of this is a failing request made to an external server. In these cases you don't want an entire program to fail, but you'd like to allow the program to wait for a moment before trying again.

### Installation
```bash
    python -m pip install stamina
```

### Run It
- attemps specify the number of time we want the program to rerun again
```python
    import random
    import stamina

    @stamina.retry(on=ValueError, attempts=7)
    def run(i):
        if random.random() < 0.5:
            raise ValueError("oh no")
        return i

    for i in range(10): 
        run(i)

```

### Good practice 
- if you're sending 100 requests to a server and they all fail. 
- Then you could wait a few seconds and try all the requests again ... 
- but that might hurt the server. 
- If the first 100 requests couldn't be handled immediately you may be better off giving the service a breather.

- That's why stamina takes a principled approach that revolves around combining two concepts.
- **Exponential Backoff**: each time a function fails you wait for for longer before calling the next one. This ensures that if the service is rebooting that you wait for longer each time.
- Randomness: to prevent loads of traffic spiking every time you do another retry you should also add some randomness in the waiting time for each request. That way, you "flatten the curve" a bit for the service that you're polling.


###  Explicit Errors 
- In general, it's a very good practice to be explicit about the errors that you want to catch. You only want to retry the situations that you understand very well and you typically want a program to fail if something unexpected happens. 
- Then again, there are these rare occasions where you may want to catch everything, maybe early on when you're exploring something. For these moments you can also pass a general Exception.
```python
    import random
    import stamina

    @stamina.retry(on=Exception, attempts=7)
    def run(i):
        if random.random() < 0.5:
            raise RuntimeError("oh no")
        return i

    for i in range(10): 
        run(i)
```


### Logging
- we've added a log_retry function that is triggered every time that the retry-mechanic is triggered
- It receives a RetryDetails object that has information that you may be interested in logging.
- The log_retry function is configured via the stamina.instrumentation.set_on_retry_hooks call. 
```python
    import random
    import stamina


    def log_retry(retry_details: stamina.instrumentation.RetryDetails):
        print(f"Retry attempt #{retry_details.retry_num}. Waited sofar={retry_details.waited_so_far}")
        print(f"{retry_details.args=} {retry_details.kwargs=}")

    stamina.instrumentation.set_on_retry_hooks([log_retry])

    @stamina.retry(on=ValueError, attempts=7)
    def run(i):
        if random.random() < 0.5:
            raise ValueError("oh no")
        return i

    for i in range(10): 
        run(i)

```