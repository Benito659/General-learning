from functools import reduce
def sum_1(*args) : 
    total = 0
    for arg in args:
        total+=arg
    return total

def sum_2(*args):
    return reduce(lambda x,y: x+y, args)

def sum_3(*args):
    return reduce(lambda x, y: x + y, args, 0)