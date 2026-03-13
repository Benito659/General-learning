

def stats(*args, **kwargs):
    operator={
        "mean" : lambda listes : sum(listes)/len(listes),
        "max" : lambda listes :max(listes),
        "min" : lambda listes : min (listes)

    }
    return {
        key : operator[key](args) 
        for key, value in kwargs.items()
        if value
    }
