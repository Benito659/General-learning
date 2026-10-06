from functools import wraps

def logger(f):
    @wraps(f)
    def func(*args,**kwargs):
        print("Fonction {} called".format(f.__name__))
        print("Arguments", *args)
        result=f(*args,*kwargs)
        return result
    return func

@logger
def multiply(a,b):
    return a*b
