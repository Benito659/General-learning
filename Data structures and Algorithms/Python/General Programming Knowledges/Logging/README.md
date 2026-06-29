## Logging
Logging is a python library that we need to improve python debugging in production. Print statements can only do so much. You also need to log to files if you want to debug something that is in production. 

### Format
- We import logging librabry
- Handler descrbe where the log will go
- Formatter tell us what our logs will look like
- logger.py
```python
    import logging

    logger = logging.getLogger(__name__)

    # the handler determines where the logs go: stdout/file
    handler = logging.StreamHandler()

    # the formatter determines what our logs will look like
    fmt = '%(levelname)s %(asctime)s %(filename)s %(funcName)s %(lineno)d %(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.setLevel(logging.WARNING)

```
- job.py :
```python
    import sys

    from logger import logger
    from summarise import summary

    if __name__ == "__main__":
        ticker = sys.argv[1]
        logger.warning(f"Will find summary for {ticker}")
        print(f"The average stock price is {summary(ticker)}")

```
- summarize.py : 
```python
    from fetch import download_data
    from logger import logger

    def summary(ticker):
        logger.warning("About to download data.")
        dataf = download_data()
        logger.warning("Dataset downloaded.")
        return dataf[ticker].mean()

```
- fetch.py :
```python
    import pandas as pd
    from logger import logger

    def download_data():
        url = 'https://calmcode.io/static/data/stocks.csv'
        logger.warning(f"Fetching from {url}")
        return pd.read_csv(url)
```


### Log Level
- help to indicate some line are more critical than other
- the more i move down, the more critical, the message become :
- we can specify the level we want to start with
- Important: do not name this file logging.py.
- One thing to remember is that there is an order to the loglevels. If the loglevel is set to INFO then it will show all the INFO-level logs as well as all the logs that are more critical (WARNING, ERROR and CRITICAL). If you want to show everything then it's best to set the level to DEBUG.
- exemple :
```python
    import logging

    logger = logging.getLogger(__name__)

    # the handler determines where the logs go: stdout/file
    handler = logging.StreamHandler()

    # the formatter determines what our logs will look like
    fmt = '%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s'
    formatter = logging.Formatter(fmt)
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    # you can change this line to see different lines being logged
    logger.setLevel(logging.WARNING)

    logger.debug('this is a debug statement')
    logger.info('this is a info statement')
    logger.warning('this is a warning statement')
    logger.error('this is a error statement')
    logger.critical('this is a critical statement')
```


### Files logging
- we can split our logs into streamhandler(command line printing) and a file handler(logs into file)
- both communicate with base logger
- allow to have a fine grain view in our logging file but not over load by logging in cli
- be sure the logger have access to the logger info , the logging file want to have access to
- we can have different format for shell and file
- all our logging concern an be separate from the logic of our app
- logger.py:
```python
    import logging

    logger = logging.getLogger(__name__)

    # the handler determines where the logs go: stdout/file
    shell_handler = logging.StreamHandler()
    file_handler = logging.FileHandler("debug.log")

    logger.setLevel(logging.DEBUG)
    shell_handler.setLevel(logging.WARNING)
    file_handler.setLevel(logging.DEBUG)

    # the formatter determines what our logs will look like
    fmt_shell = '%(levelname)s %(asctime)s %(message)s'
    fmt_file = '%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s'

    shell_formatter = logging.Formatter(fmt_shell)
    file_formatter = logging.Formatter(fmt_file)

    # here we hook everything together
    shell_handler.setFormatter(shell_formatter)
    file_handler.setFormatter(file_formatter)

    logger.addHandler(shell_handler)
    logger.addHandler(file_handler)
```
- job.py :
```python
    import sys

    from logger import logger
    from summarise import summary

    if __name__ == "__main__":
        logger.debug("Program started.")
        try:
            ticker = sys.argv[1]
            logger.info(f"Will find summary for {ticker}.")
            print(f"The average stock price is {summary(ticker)}")
            logger.debug("Program ended with success.")
        except BaseException:
            logger.error("Error happened!", exc_info=True)

```
- summerize.py:
```python
    from fetch import download_data
    from logger import logger

    def summary(ticker):
        logger.info(f"About to download data.")
        dataf = download_data()
        logger.debug(f"Dataset downloaded. shape={dataf.shape}")
        logger.debug(f"Dataset downloaded. columns={dataf.columns}")
        return dataf[ticker].mean()

```

- fetch.py :
```python
import pandas as pd

from logger import logger

def download_data():
    url = 'https://calmcode.io/static/data/stocks.csv'
    logger.debug(f"Fetching from {url}.")
    df = pd.read_csv(url)
    logger.info(f"File downloaded from {url}.")
    return df


```


### Errors:
- to catch the error in the logs we need to raise the exception
- job.py:
```python
    import sys

    from logger import logger
    from summarise import summary

    if __name__ == "__main__":
        logger.debug("Program started.")
        try:
            ticker = sys.argv[1]
            logger.info(f"Will find summary for {ticker}.")
            print(f"The average stock price is {summary(ticker)}")
            logger.debug("Program ended with success.")
        except BaseException:
            logger.error("Error happened!", exc_info=True)


```

### RichHandler
- He make the logs pretty
- we replace stream handler with it
- he already handle a lot of formatting
- logger.py:
```python
    import logging

    from rich.logging import RichHandler

    logger = logging.getLogger(__name__)

    # the handler determines where the logs go: stdout/file
    shell_handler = RichHandler()
    file_handler = logging.FileHandler("debug.log")

    logger.setLevel(logging.DEBUG)
    shell_handler.setLevel(logging.DEBUG)
    file_handler.setLevel(logging.DEBUG)

    # the formatter determines what our logs will look like
    fmt_shell = '%(message)s'
    fmt_file = '%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d] %(message)s'

    shell_formatter = logging.Formatter(fmt_shell)
    file_formatter = logging.Formatter(fmt_file)

    # here we hook everything together
    shell_handler.setFormatter(shell_formatter)
    file_handler.setFormatter(file_formatter)

    logger.addHandler(shell_handler)
    logger.addHandler(file_handler)

```

- Log Early and log often