## GIN
Gin is a system for configuring python code that is still very much in early phases, but very powerful. It can be use to configure general python scripts. It is a lightweight configuration framework based on dependency injection. Developed originally by Google engineers, it allows developers to pass parameter values into functions or classes from a centralized configuration file rather than writing complex, boilerplate code for argument parsing. It is heavily used in machine learning experiments (like those using TensorFlow or PyTorch) to manage hundreds of hyperparameter variations.


### Installation 
- we can install it through pip
```bash
    pip install gin-config
```

### Run it 
- we create a config file call : **config.in**
- exemple :
```gin
    simulate.n_samples = 100
```
- the simulate file in python **simulate.py** 
```python
    import gin
    import random

    @gin.configurable
    def simulate(n_samples):
        return sum(random.random() for i in range(n_samples))

    if __name__ == "__main__":
        gin.parse_config_file("config.gin")
        print(simulate())
```
- it configure parameters in a function
- it use a decorator that allow to make something configurable (**@gin.configurable**)
- we can then tell gin to parse some gin file, **gin.parse_config_file("config.gin")**
- when we will run simulate.py , it will run



### REQUIRED SETTINGS
- We can define a standard value directly into standard python function (like a default value ) 
- We can want something to be configure explicitly (**gin.REQUIRED**)
```python
    import gin
    import random

    @gin.configurable
    def simulate(n_samples=gin.REQUIRED)
        return sum(random.random() for i in range(n_samples))

    if __name__ == "__main__":
        gin.parse_config_file("config.gin")
        print(simulate())

```


### Functions as config
- we can also configure functions in gin. 
- we can chose function that will be pass in parameters
- we can referance object
- we add to function that will be pass and function that is receive gin.configurable
```gin
    simulate.n_samples = 200
    simulate.random_func = @random_triangle

    random_triangle.minval = 0
    random_triangle.maxval = 100
```
```python
    import gin
    import random

    @gin.configurable
    def random_uniform(minval=0, maxval=1):
        return random.uniform(minval, maxval)

    @gin.configurable
    def random_triangle(minval=0, maxval=1):
        middle = (maxval - minval)/2
        return random.triangular(minval, maxval, middle)

    @gin.configurable
    def simulate(random_func, n_samples):
        return sum(random_func() for i in range(n_samples))

    if __name__ == "__main__":
        gin.parse_config_file('config.gin')
        print(simulate())

```


### Blacklist 
- we are able to configure function parameters
- we want to be strict on parameters of a fonction and don't allow someone to overwrite it
- we use blacklist parametters into the decorators
```python
    @gin.configurable(blacklist=["n_samples"])
```
- it wont we configurable in the gin file
```gin
    simulate.random_func = @random_triangle

    random_triangle.minval = 0
    random_triangle.maxval = 100

```
```python
    import gin
    import random

    @gin.configurable
    def random_uniform(minval=0, maxval=1):
        return random.uniform(minval, maxval)

    @gin.configurable
    def random_triangle(minval=0, maxval=1):
        middle = (maxval - minval)/2
        return random.triangular(minval, maxval, middle)

    @gin.configurable(blacklist=["n_samples"])
    def simulate(random_func, n_samples):
        return sum(random_func() for i in range(n_samples))

    if __name__ == "__main__":
        gin.parse_config_file('config.gin')
        print(simulate())

```


### Externals configuration
- It does not make sense to create a function in order to configure something. 
- You may need to make a reference first though. The files below reflect how you might be able to do that.
```gin
    simulate.random_func = @random.uniform

    random.uniform.a = 0
    random.uniform.b = 2
```

```python
    import gin
    import random

    gin.external_configurable(random.uniform)
    gin.external_configurable(random.triangular)

    @gin.configurable(blacklist=["n_samples"])
    def simulate(random_func, n_samples):
        return sum(random_func() for i in range(n_samples))

    if __name__ == "__main__":
        gin.parse_config_file('config.gin')
        print(simulate())

```