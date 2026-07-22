## Fast API
FastApi is an enjoyable tool for building web applications in python. In these videos we demonstrate the main features. FastAPI is a modern, high-performance web framework used for building REST APIs with Python 3.8+. It is widely celebrated in backend development because it matches the speed of Node.js and Go while keeping code production-ready, highly intuitive, and quick to write.

### Features
- **Extreme Performance**: Built on top of the Starlette ASGI framework, it handles asynchronous, non-blocking requests flawlessly
- **Automatic Documentation**: Automatically creates interactive web documentation (such as Swagger UI and ReDoc) directly from your code structure.
- **Data Validation**: Leverages Python type hints and Pydantic models to automatically validate incoming JSON request payloads.
- **Asynchronous Support**: Natively supports async and await structures, making it highly effective for heavy I/O operations like database queries or external API calls.
- **Fewer Bugs**: The strict use of type annotations reduces human development errors by roughly 40%

### Installation 
```bash
    pip install fastapi uvicorn
```
- we will build the code in **app.py**
```python
    from fastapi import FastAPI
    app = FastAPI()
    @app.get(/)
    def root():
        return {"message": "hello world again"}
```
- to start the server
```bash
    uvicorn app:app
```
- to start and restart automatically when there is an uptdate :
```bash
    uvicorn app:app --reload
```


### Routes
- Verifying type of variable we pass through the api routes is important
- we'll use decorators like @get.route("/") to describe the where the request can go while the function that follows describes how it is handled. 
- Note that these functions are typically typed, which means that you can explicitly state what type of variables it should assume.
```python
@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id":user_id}
```

### Json
- You can send json to FastApi. 
- Vrifying the type of the data in the Json is important
- FastApi using the **pydantic** library to help you define the perfect json type.
```python
    from pydantic import BaseModel

    class Item(BaseModel):
        name: str
        price: float
    
    @app.post("/items/")
    def create_item(item:Item) :
        return item
```
- when type send in the json does not match model type we got an error
- when type send match , but not exctaly it can be converted for exemple : int convert to float ( 0 will become 0.0)
- To test api you can use **Insomnia**  and **postman**
- **app.py** :
```python
    from fastapi import FastAPI

    app = FastAPI()

    @app.get("/")
    def root():
        return {"message": "hello world again"}

    @app.get("/users/{user_id}")
    def read_user(user_id: str):
        return {"user_id": user_id}

    from pydantic import BaseModel, validator

    class Item(BaseModel):
        name: str
        price: float

    @app.post("/items/")
    def create_item(item: Item):
        return item

```

### Type Validation
- we can strengten condition we want to add to validate type data
- for exemple we want to make sure the valu is between some range
- so we use the @validator decorator
- we can details error message we send back
```python
    from pydantic import BaseModel, Validator

    class Item(BaseModel):
        name: str
        price: float

        @validator("price")
        def price_must_be_positive(cls, value) :
            if value <= 0:
                raise ValueError(f"we expect price >= 0, we received {value}")
            return value

    @app.post("/items/")
    def create_item(item:Item):
        return item
```


### Documentations
- we can find the docs locally over at **http://127.0.0.1:8000/docs**.
- this will be documentation of our app
- we will also see schema from our items
- we can details documenation directly in the endpoints of fast api by adding doctring under function
```python
@app.get("/users/{user_id}")
def read_user(user_id: str) :
    """
    we accept a `user_id` here and return a json-blob containing it
    """
    return {"user_id": user_id}
```


### Async
- Async improve the speed 
- we can create two new endpoints to test the async
- we will use asyncio
- Asyncio is a built-in Python library used to write concurrent code using the async and await syntax. 
- It is designed specifically for I/O-bound tasks-such as making web API requests, reading/writing files, or querying databases. 
- Instead of wasting CPU time waiting for an external server to respond, asyncio pauses the waiting task and switches to another one, maximizing efficiency inside a single thread

```python
import time
import asyncio

@app.get("/sleep_slow")
def sleep_slow():
    r= time.sleep(1)
    return { "status":"done"}

@app.get("/sleep_fast")
async def sleep_fast():
    r = await asyncio.sleep(1)
    return {"status":"done"}

```

- now we rerun uvicorn to reload the app
```bash
    uvicorn app:app --workers 1 --reload
```

- we will do a benth marking
- for bentchmarking we will use boom, it is a tool that send a lot of request
```bash
    pip install boom
```

- now we will first test the first endpoint
- **-c** specify the number of concurent request
- **-n** the number of total request

```bash
    boom http://127.0.0.1:8000/sleep_slow -c 200 -n 200
```
- then we will run the second endpoint

```bash
    boom http:/127.0.0.1:8000/sleep_fast -c 200 -n 200
```

- async is the fact to not wait for he end of a request but execute another before the ending of the other 



### Testing
```bash
    pip install pytest
```
- for testing api , we will use starlette
- it is a project FastAPI depends on, we will use that project to test app
- client can pretend to be endpoint
- we will test endepoint
```python
from starlette.testClient import TestClient
from app import app
client = TestClient(app)
def test_root_endpoint():
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.json() == {"message":"hello world again"}

def test_users_endpoints():
    resp = client.get("/users/1")
    assert resp.status_code == 200
    assert resp.json() == {"user_id":"1"}

```
- we will test two other post endpoints
```python
def test_correct_items():
    json_blob= {"name":"shampoo","price":1.5}
    resp = client.post("/items/", json = json_blob)
    assert resp.status_code == 200

def test_wrong_items():
    json_blob =  {"name":"shampoo", "price": -1.5}
    resp = client.post("/items/", json = json_blob)
    assert resp.status_code != 200

```