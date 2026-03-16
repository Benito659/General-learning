from functools import wraps

def validate_types(a=int, b=int):
    def validation(f):
        @wraps(f)
        def func(*args,**kwargs):
            for key,val in kwargs.items() :
                if key in expected_types:
                    if type(val) != int
                        raise TypeError("Wrong type")
            print("works")
            results = f(*args,**kwargs)
            return results
        return func
    return validation

@validate_types(a=int,b=int)
def add(a,b):
    return a+b