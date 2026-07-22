## API DESIGN

### Flask Vs Django Vs Fast API

|     **Feature**     |          **Fast API**        |             **Flask**          |          **Django**           |
| ------------------- | ---------------------------- | ------------------------------ | ----------------------------- |
|   Primary Use Case  | High-performance, async APIs | Lightweight, simple micro-apps | Large full-stack applications |
|    Async Support    |  Native (Asynchronous/ASGI)  |   Limited/Synchronous (WSGI)   |   Heavy synchronous origins   |
|   Data Validation   |    Automatic via Pydantic    |    Manual or needs plugins     |  Handled via Django Forms/ORM |
|  API Documentation  |   Automated out-of-the-box   |   Requires extra extensions    | Requires third-party packages |