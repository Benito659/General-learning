from functools import wraps

ALREADY_USE={}

def cache(f):
    @wraps(f)
    def func(n,*args,**kwargs):
        if n in ALREADY_USE:
            print("Cache hit")
            print("Previous value" : ALREADY_USE[n])
        else:
            result=f(n,*args,kwargs)
            ALREADY_USE[n]=result
        return result
    return func


@cache
fibonacci(n)      

