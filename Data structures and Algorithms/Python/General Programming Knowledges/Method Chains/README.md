## Methods Chains
Method chaining is a programming technique where you call multiple methods sequentially on a single object in a single line of code. Instead of saving intermediate results in temporary variables, the output of one method automatically becomes the context (the calling object) for the next method.For method chaining to work, each intermediate method must return an object (either the modified original object, a new copy, or a completely new object). If a method returns None (like the built-in list.append()), the chain breaks and throws an error.

### Data
- it can be use especially when we want to handle nested structure that are not row and columns for exemple
- We will make a pandas like api
```python
    import json
    import pathlib
    poke_dict = json.loads(pathlib.Path("pokemon.json").read_text())
    poke_dict[:3]
```
```json
    [
        {
            'name': 'Bulbasur',
            'type': ['Grass', 'Poison'],
            'total': 318,
            'hp':45,
            'attack':49,
        },
        {
            'name': 'Ivysaur',
            'type': ['Grass', 'Poison'],
            'total': 405,
            'hp':60,
            'attack':62,
        },
        {
            'name': 'Venusaur',
            'type': ['Grass', 'Poison'],
            'total': 525,
            'hp':80,
            'attack':82

        }
    ]
```
### Keep
- we are implementing a way to  Implementing a filter for data. 
- we will create the class that will allow us to apply a filter function 
```python
    class Clumper:
        def __init__(self, blob):
            self.blob = blob
        
        def keep(self, func):
            return [d for d in self.blob if func(d)]
```
- we will then filter base on object that contains 'Grass'
```python
    Clumper(poke_dict).keep(lambda d: 'Grass' in d['type'])
```

### Chains
- we want now to chains commands together.
- we will return at each keep method The Clumper and then we will call back
```python
    class Clumper:
        def __init__(self, blob):
            self.blob = blob
        def keep(self, func):
            return Clumper([d for d in self.blob if func(d)])

```

```python
    (Clumper(poke_dict)
        .keep(lambda d: 'Grass' in d["type"])
        .keep(lambda d: d['hp']<60)
        .blob)
```


### Args 
- we will change the functions as we can take into account many functions
```python
    class Clumper:
        def __init__(self, blob):
            self.blob = blob
        
        def keep(self, *funcs):
            data = self.blob
            for func in funcs: 
                data = [ d for d in data if func(d)]
            return Clumper(data)

```
```python
    Clumper(poke_dict)
        .keep(lambda d: 'Grass' in d['type'], lambda d: d['hp']<60)
```
- both chain and multiple functions are still valable


### Head , Tail
- we will implement a method that return top elements of a dataset
```python
class Clumper:
    def __init__(self, blob):
        self.blob = blob
    
    def keep(self, *funcs):
        data = self.blob
        for func in funcs :
            data = [d for d in data if func(d)]
        return Clumper(d)
    
    def head(self, n)
        return Clumper([self.blob[i] for i in range(n)])
    
    def tail(self, n)
        return Clumper([self.blob[-i]] for i in range(1, n+1))
```

```python
    Clumper(poke_dict).tail(10).blob
    Clumper(poke_dict).head(10).blob

```


### Select 
- we want to build function that allow us to select functions
```python
def select(self, *keys):
    return Clumper([{k:d[k] for k in keys} for d in self.blob])
```

### Mutate
- we want to update or add a new value in our data
```python
def mutate(self, **kwargs):
    data = self.blob
    for key, func in kwargs.items():
        for i in range(len(data)):
            data[i][key] = func(data[i])
            return Clumper(data)
```
```python
Clumper(poke_dict)
    .mutate(
        hp = lambda d: d['hp']*2,
        hp4 = lambda d: d['hp4']*4
    )
```

### Sorted
```python
def sort (self, key, reverse = False):
    return Clumper(sorted(self.blob, key = key, reverse=reverse))
```
```python
Clumper(poke_dict)
    .sort(lambda d : d['hp'], reverse = True)
```


### Bliss
- very preferable for manipulate data
- It's easy to make changes to the analysis here because the reading is from left to right top to bottom. 
- We can change the order of lines which will change the order of the code which makes it easy to reason about the steps that are being applied to our data.
- This is not the case in general with python for loops. It can get messy quite fast. It is exactly this what makes method chains so powerful and like-able.
