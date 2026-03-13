import time

def execution_time(f):
    def func(*args,**kwargs):
        start_time=time.time()
        result=f(*args,**kwargs)
        print("Execution time :",time.time()-start_time)
        return result
    return func


@execution_time
def multiply(a,b):
    return a*b