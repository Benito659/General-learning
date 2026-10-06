## PyInstrument
Pyinstrument is a profiler for Python. It's a tool that will track how long specific parts of our code run, such that we may learn which parts are slow. Understanding this well can typically inspire us to write faster programs, which is usually a good thing.

### Installation 
```bash
    python -m pip install pyinstrument
```

### Usage
- we can mesure time diretcly in the command line with command **time**
```bash
    time python automator/populate.py
```

-  we can call pyinstrument
```bash
    pyinstrument automator/populate.py
    pthon -m pyinstrument automator/populate.py
```

- we can also observe it into a html file
```bash
    pyinstrument -r html path/script.py
```

- we can also use pyinstrument to generate speedscope files which can be used by speedscope.app to generate interactive flamegraphs
```bash
    pyinstrument -r speedscope -o speedscope.json path/script.py
```

- Pyinstrument can be customised by including it explicitly in your Python scripts. This will give you more control on what to measure. The general syntax for this is shown below.
- Exemple :
```python
    from pyinstrument import Profiler

    profiler = Profiler()
    profiler.start()

    # This is where your custom code goes.

    profiler.stop()
    profiler.print()
```
- Exemple :
```python
    import time
    from pyinstrument import Profiler

    profiler = Profiler()
    profiler.start()

    sleep_time = 0.1

    def start():
        time.sleep(sleep_time)
        do_sleep1()
        do_sleep2()

    def do_sleep1():
        time.sleep(sleep_time)

    def do_sleep2():
        do_sleep1()
        time.sleep(sleep_time)

    start()

    profiler.stop()
    profiler.print()

```

- profiler is a statistical profiler
- we can specify interval at wich it will observe all data