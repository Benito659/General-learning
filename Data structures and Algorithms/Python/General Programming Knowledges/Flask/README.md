## FLASK
Flask is a lightweight Python web framework used to build websites, web apps, and APIs. It is called a "microframework" because it gives you the core tools to run a server without forcing a specific file layout or database choice, letting you pick the parts you want

- Flask is a lightweight web framework used to build web applications and APIs. It follows a minimal design and provides core features like routing, request handling and template rendering while allowing developers to add extensions as needed. It is widely used for building small to medium web applications due to its simplicity and flexibility.

- Microframework: Lightweight framework with minimal dependencies, giving developers full control over application structure.
- Werkzeug & Jinja2: Uses Werkzeug for request/response handling and Jinja2 for dynamic HTML templating.
- Routing: Maps URLs to Python functions using simple decorators.
- Flexible Database Choice: No built-in ORM, allowing use of tools like SQLAlchemy or raw SQL.
- API Development: Well-suited for building RESTful APIs and backend services.
- Development Server: Includes a built-in server for local testing during development.

- Built-in Development Server: Allows to run and test applications locally without extra setup.
- Routing Support: Easily maps URLs to specific functions using decorators.
- Template Engine (Jinja2): Helps create dynamic HTML pages with reusable templates.
- Extension Support: Integrates with extensions like Flask-SQLAlchemy for added functionality.
- RESTful Request Handling: Provides tools to handle HTTP methods like GET, POST, PUT and DELETE.
- Debug Mode: Automatically reloads the server and shows errors during development.

### Setting Up Environments
- Install Virtual environnements :
```bash
    pip install virtualenv
    virtualenv venv
    \venv\Scripts\activate.bat
    pip install flask flask-sqlalchemy
```
- app.py :
```python
    from flask import Flask
    app = Flask(__name__)
    @app.route("/")
    def index():
        return "hello world"

    if __name__ == "__main__":
        app.run(debug==True)
```

- to start the app :
```bash
    python app.py
    flask --app app.py run
```
- With debug mode on, Flask automatically detects errors and shows a detailed traceback, helping developers quickly find and fix issues. 


### Render Html page
- Application Structure : 
```text
    flask_app/
    |—— venv/
    |—— static/
    |—— templates/index.html
    |—— app.py
```
- static contains css and javascrits
- we have template inheritence
- we create a master template of what master template look like and it will inherit from other template page


### Simple Html Form
- simple html file
```html
    <!DOCTYPE html>
    <html>
    <body>
        <h3>Enter Your Name</h3>
        <form method="post">
            <input type="text" name="username" required>
            <br><br>
            <input type="submit" value="Submit">
        </form>
    </body>
    </html>
```
- The form uses method="post" to send data securely
- The input field sends the value using the name username
- Clicking Submit sends the data to the Flask server
- app.py
```python
    from flask import Flask, render_template, request
    app = Flask(__name__)

    @app.route("/login", methods=["POST","GET"])
    def login():
        if request.method == "POST":
            name = request.form["username"]
            return f"Hello {name}, POST request received"
        return render_template("index.html")

    if __name__ == "__main__":
        app.run(debug=True)
```

### Routing
- Flask App Routing is the process of mapping URLs to specific functions in a web application. 
- When a user enters a URL in the browser, Flask checks the defined routes and executes the corresponding function to generate a response. 
- This is done using the @app.route() decorator, which binds a URL path to a function.
- **Dynamic URLs** :
- We can also build dynamic URLs by using variables in the URL. 
- To add variables to URLs, use the <variable_name> syntax in the route. 
- The function then receives the <variable_name> as keyword argument. 
```python
    from flask import Flask

    app=Flask(__name__)

    @app.route("/hello/<variable_name>")
    def hello(variable_name):
        return f"hello {variable_name}"

    if __name__=="__main__":
        app.run(debug=True)
```
- Additionally, we can also use a **Converter** to convert the variable to a specific data type. 
- By default, variables are treated as strings. 
- To specify a data type, use <converter:variable_name>. 
- The following converters are supported:
    - string: default type and it accepts any text without a slash.
    - int: accepts positive integers.
    - float: accepts positive floating-point values.
    - path: a string but also accepts slashes.
    - uuid: accepts UUID strings.

```python
    from flask import Flask

    app=Flask(__name__)

    @app.route("/hello/<hello_variable>")
    def hello(hello_variable):
        return "hello"

    @app.route("/converter/<int:converter_variable>")
    def converter(converter_variable):
        return converter_variable

```
- **add_url_rule**:
- The URL mapping can also be done using the add_url_rule() function. 
- This approach is mainly used when the view function is defined in another module.
- In fact, the app.route calls this function internally.
- Syntax: add_url_rule(rule, endpoint, view_func)
```python
    from flask import Flask
    app=Flask(__name__)

    def show_user(username):
        return f"hello {username} !"

    app.add_url_rule("user/<username>", "show_user",show_user)

    if __name__=="__main__":
        app.run(debug=True)
```

### Models
- In Flask, models define the structure of data and handle database operations by mapping database tables to Python classes. 
- ORM (Object Relational Mapping) is used which allows to interact with the database using Python code instead of writing SQL queries. 
- Flask commonly uses SQLAlchemy as its ORM to manage data efficiently.
- Creating Models using Flask-SQLAlchemy :
- Install flask-sqlalchemy :
```bash
    pip install flask-sqlalchemy
```
- Import Module : 
```python
    from flask import Flask, render_template, request, redirect, url_for
    from flask_sqlalquemy import SQLalquemy
    import datetime
```
- Configure Flask and Database : 
```python
    app= Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///event_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```
- SQLALCHEMY_DATABASE_URI: Specifies the database location (SQLite in this case).
- SQLALCHEMY_TRACK_MODIFICATIONS: Disables unnecessary change tracking for better performance.
- Initialize the database :
```python
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
```
- Define a Model : which represents a table in the database
```python
    class Event(db.model):
        id = db.Column(db.Integer,primary_key=True)
        date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
        event = db.Column(db.String(200), nullable=False)
```
- Create the Database :
```python
    with app.app_context():
        db.create_all()
```

- Inserting Data into the Database : 
```python
    def add_event(event_description):
        new_event = Event(event = event_description)
        db.session.add(new_event)
        db.session.commit()
```

- Quering DataBase :
- GET request: Fetches all events using 
```python
    db.session.execute(db.select(Event).order_by(Event.date)).scalars()
```
- POST request: Adds a new event to the database.
```python
    @app.route('/', methods=['GET', 'POST'])
        def home():
            if(request.method == 'POST'):
                db.session.add(Event(date=datetime.datetime.now().__str__(), event=request.form['eventBox']))
                db.session.commit()
                return redirect(url_for('home'))
            return render_template('home.html', eventsList=db.session.execute(db.select(Event).order_by(Event.date)).scalars())

        return app
```

- db.session.add() adds new event
- db.session.commit() saves changes
- db.select(Event) fetches events
- order_by(Event.date) sorts by date

```python
    from flask import Flask, url_for, render_template, request, redirect
    import os
    import datetime
    import click
    from flask_sqlalchemy import SQLAlchemy
    from sqlalchemy.exc import IntergrityError
    from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

    def create_app(test_config = None):
        app = Flask( __name__, instance_relative_config= True)
        app.config.from_pyfile('config.py', silent=True)
        app.config.from_mapping(SECRET_KEY = 'dev')

        try:
            os.makedirs(app.instance_path)
        except OSError:
            pass
        
        app.config["SQL_ALCHEMY_DATABASE_URI"] = "sqlite:///event_database.db"

        class Base(DeclarativeBase):
            pass
        
        db = SQLAlchemy(model_class=Base)
        db.init_app(app)

        class Event(db.Model):
            date = mapped_column(db.String, primary_key = True)
            event = mapped_column(db.String)
        
        @click.command('init-db')
        def init_db_command():
            """Command for initializing the database"""
            with app.app_context():
                db.create_all()
                click.echo("Database create succeffuly")
        
        app.cli.add_command(init_db_command)

        @app.route('/', methods=['GET','POST'])
        def home():
            if request.method == "POST":
                db.session.add(Event(date=datetime.datetime.now().__str__(), event = request.form['enventBox']))
                db.session.commit()
                return redirect(url_for('home'))
            return render_template('home.html', eventsList = db.session.execute(db.select(Event).order_by(Event.date.scalars())))
        return app

    if __name__ == "__main__":
        app= create_app()
        app.run(debug=True)
```
- html template (Jinja2 templating)
```html
    <html>
        <head>
            <title>EventLog</title>
        </head>
        <body>
            <table>
                <tr>
                    <th>Date & Time</th>
                    <th>Event Details</th>
                </tr>
            {%-for row in eventsList-%}
                <tr>
                    <td>{{row.date}}</td>
                    <td>{{row.event}}</td>
                </tr>
            {%-endfor-%}
            </table>
            <hr/>
            <form method="post">
                <title>Add event</title>
                <label for="eventBox">Event Description</label>
                <input name="eventBox" id="eventBox" required/>
                <input type="submit" value = "Add">
            </form>
        </body>
    </html>
```


### Request Object
- The request object in Flask contains all the data associated with an incoming HTTP request. 
- It allows applications to access information sent by the client, such as **form data**, **query parameters**, **uploaded files**, **cookies**, **headers** and **the HTTP request method**. 
- It's provided by Flask and represents the current HTTP request sent by the client to the server.
- Retrieve form data submitted by users.
- Access URL query parameters.
- Read uploaded files.
- Access cookies and request headers.
- Determine the HTTP request method (GET, POST, etc.).

- request.form	Retrieves data submitted through HTML forms using the POST method.
- request.args	Retrieves query parameters from the URL.
- request.files	Accesses uploaded files.
- request.cookies	Retrieves cookies sent by the browser.
- request.method	Returns the HTTP request method (GET, POST, etc.).
- request.headers	Retrieves HTTP headers sent by the client.
- request.get_json   Retrieves data in dictinaries

```python
from flask import Flask , render_template, request

app  = Flask( __name__ )

@app.route('/')
def input():
    return render_template('home.html')

@app.route('/passing', methods=["GET", "POST"])
def display():
    if request.method=="POST":
        result = request.form
        return render_template('result_data.html', result = result)

if __name__ = "__main__":
    app.run(debug=True)
```

- Temp.html
```html
    <html>
    <style>
    body {
        text-align: center;
        background-color: green;
    }
    form {
        display: inline-block;
    }
    </style>
    <body>
        <h3>Please Fill Out This Form</h3>
        <form action="/passing" method="POST">
            <p>Name <input type="text" name="name" /></p>
            <p>Email <input type="email" name="email" /></p>
            <p>Phone Number <input type="text" name="phone" /></p>
            <p><input type="submit" value="Submit" /></p>
        </form>
    </body>
    </html>
```

- result_data.html :
```html
    <!doctype html>
    <html>
    <style>
    body {
        text-align: center;
        background-color: orange;
    }
    table {
        display: inline-block;
        border-collapse: collapse;
    }
    </style>
    <body>
        <p><strong>Registration Successful</strong></p>
        <table border="1">
            {% for key, value in result.items() %}
            <tr>
                <th>{{ key }}</th>
                <td>{{ value }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
```


### HTTP Methods :
- HTTP methods define how a client (browser) interacts with a server in a web application. 
- They are used to handle different types of requests like fetching data, sending data or updating resources. 
- GET request data from the server.
- POST submit data to be processed to the server.
- PUT replaces the entire resource with new data. If it doesn’t exist, a new one is created.
- PATCH updates only specific parts of a resource without replacing the whole thing.
- DELETE deletes the data on the server at a specified location

- **GET Method :**
- GET method is used to request data from a server.
- It appends data to the URL in a name-value pair format.
- It should not be used for sensitive data since URLs are visible in browser history.

```python
    from flask import Flask, request, render_template
    app = Flask(__name__)

    @app.route('/square', methods=['GET'])
    def squarenumber():
        num = request.args.get('num')

        if num is None:  
            return render_template('squarenum.html')
        elif num.strip() == '': 
            return "<h1>Invalid number. Please enter a number.</h1>"
        try:
            square = int(num) ** 2
            return render_template('answer.html', squareofnum=square, num=num)
        except ValueError:
            return "<h1>Invalid input. Please enter a valid number.</h1>"

    if __name__ == '__main__':
        app.run(debug=True)
```

- **POST Method :**
- POST method is used to send data to the server for processing. 
- Unlike GET, it does not append data to the URL. 
- Instead, it sends data in the request body, making it a better choice for sensitive or large data.
```python
    from flask import Flask, request, render_template
    app = Flask(__name__)

    @app.route('/square', methods=['GET', 'POST'])
    def squarenumber():
        if request.method == 'POST':
            num = request.form.get('num')
            if num.strip() == '':  
                return "<h1>Invalid number</h1>"
            square = int(num) ** 2
            return render_template('answer.html', squareofnum=square, num=num)
        return render_template('squarenum.html')

    if __name__ == '__main__':
        app.run(debug=True)
```




### Variables Rules
- Flask variable rules are used to create dynamic URLs by capturing values directly from the URL. 
- These values are passed to the view function and can be used to display different content based on user input.
- Variables are defined using <variable_name> inside the route.
- Captured values are passed as arguments to the view function.
- Converters like <int:id> and <string:name> can be used to specify the data type of the variable.
- **string** accepts any text without a slash (default).
- **int** accepts only integers.
- **float** like int but for floating point values.
- **path** like the default but also accepts slashes.
- **any** matches one of the items provided.
- **UUID** accepts UUID strings.
- String Variable : 
```python
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def msg():
        return "Welcome"

    @app.route('/vstring/<name>')
    def string(name):
        return "My Name is %s" % name

    app.run(debug=True)
```
- Integer Variable:

```python
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def msg():
        return "Welcome"

    @app.route('/vint/<int:age>')
    def vint(age):
        return "I am %d years old " % age

    app.run(debug=True)
```
- Float Variable : 
```python
    from flask import Flask
    app = Flask(__name__)

    @app.route('/')
    def msg():
        return "Welcome"

    @app.route('/vfloat/<float:balance>')
    def vfloat(balance):
        return "My Account Balance %f" % balance

    app.run(debug=True)
```


### REDIRECT AND ERRORS
- A redirect is used to send a user from one URL to another. 
- When a redirect occurs, server responds with an HTTP status code that instructs the browser to load a different location. 
- Redirects are commonly used after form submissions, authentication checks or when a resource has moved.
- flask.redirect(location, code=302)
- location (str) URL where the user should be redirected.
- code (int) HTTP status code indicating the type of redirect. If no code is specified, Flask uses 302 (temporary redirect) by default.
- Return: a response object that redirects the user to the specified URL with the given HTTP status code.
- **HTTP status** codes are three-digit numbers returned by the server to indicate how the request should be handled. 
- The following codes are commonly associated with redirects:
- **300**	Multiple Choices
- **301**	Moved Permanently
- **302**	Found (Temporary Redirect)
- **303**	See Other
- **304**	Not Modified
- **305**	Use Proxy
- **306**	Reserved
- **307**	Temporary Redirect
- To perform URL redirection, we need to import the redirect function from the Flask module:
```python
    from flask import redirect
```
- The redirect() function returns a response that instructs the browser to navigate to a different URL.
- Redirecting Based on Login Input
- we create a Flask application that redirects users based on the username entered in a login form.
- If the username is admin, the user is redirected to the success page.
- Otherwise, the user is redirected back to the login page.
```python
    from flask import Flask, redirect, url_for, render_template, request
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template("login.html")

    @app.route('/success')
    def success():
        return "logged in successfully"

    @app.route("/login", methods=["POST", "GET"])
    def login():

        if request.method == "POST" and request.form["username"] == "admin":
            return redirect(url_for("success"))

        return redirect(url_for('index'))

    if __name__ == '__main__':
        app.run(debug=True)
```
- **url_for()** Function
- url_for() function is used to dynamically generate URLs for a specific function. 
- It takes the function name as the first argument and builds the corresponding URL. 
- This is useful when performing redirects because it avoids hardcoding URLs 
- And makes the application easier to maintain.

```python
from flask import Flask, redirect, render_template, url_for, request
app = Flask(__name__)

@app.route("/admin_page")
def hello_admin():
    return "hello admin"

@app.route("/guest_page/<name>")
def hello_guest(name):
    return f"Hello {name}"

@app.route("/login/<name>")
def login(name):
    if request.form["input"] == "admin"
        redirect(url_for("hello_admin"))
    else:
        redirect(url_for("hello_guest", name = name))

if __name__ == '__main__':
    app.run(debug=True)
```

- Flask Errors
```python
    abort(code, message=None)
```
- abort() function is used to stop request processing and return an HTTP error response. 
- It is commonly used when a requested resource does not exist, request is invalid or access is not allowed.
- code (int) HTTP status code that represents the type of error.
- message (str, optional) custom error message that can be returned with the response.
- When abort() is called, Flask immediately stops the current request and returns the specified error code to the client.
- 400	Bad request
- 401	Unauthenticated
- 403	Forbidden
- 404	Not Found
- 406	Not Acceptable
- 415	Unsupported Media Type
- 429	Too Many Requests

- we check the username provided in the URL using Error Code 400.
```python
    from flask import Flask, abort
    app = Flask(__name__)

    @app.route('/<uname>')
    def index(uname):
        if uname[0].isdigit():
            abort(400)
        return '<h1>Good Username</h1>'

    if __name__ == '__main__':
        app.run()
```
- Exemple2 :
```python
    from flask import Flask, render_template, abort, redirect, url_for
    app = Flask(__name__)
    
    @app.run("name")
    def check_name(name):
        if name[0].isdigit():
            abort(403)
        return 'Good Username'
    
    if __name__ == "__main__":
        app.run(debug=True)
```

### Change Port :
- Flask runs on port 5000 by default
- the port can be changed by specifying a different port while running the application. 
- This is useful when the default port is already in use or when multiple applications are running on the same system.
- Port can be changed by passing the port parameter in the **app.run()** method
- It can also be combined with debug mode
```python
    app.run(debug = True,port = 8001)
```



### Change Ip Adress:
- By default, a Flask application runs on 127.0.0.1:5000.
- which makes it accessible only on the same machine. 
- To access the application from other devices on the same network, the host IP address can be changed.
- Host Parameters
- host parameter in app.run() is used to specify the IP address on which the application should run.
- Setting the host to a local network IP allows other devices on the same network to access the application.
```python
    from flask import Flask

    @app.routes("/")
    def home():
        return "Home page"

    if __name__ == "__main__":
        app.run(host= '192.168.0.105')
```

- the app will be accessible from other devices on the same network using 192.168.0.105:5000.
- we can also set the host and port directly when running the app from the terminal. 
```bash
    set FLASK_APP=app.py
    flask run --host=192.168.0.105 --port=5000
```

###  Process Incoming Request Data :
- Flask receive data through HTTP requests
- it can be accessed as query parameters, HTML form data, or JSON payloads , cookies
- request.args	Query parameters
- request.form	Form data
- request.get_json()	JSON request body
- request.files	Uploaded files
- request.headers	HTTP headers
- request.cookies	Cookies
- request.method	HTTP method
- **Query String :**
- Query parameters are key-value pairs appended to the end of a URL after the ? symbol. 
- They are commonly used with GET requests to send small amounts of data, such as search terms, filters, or user preferences.
- *http://127.0.0.1:5000/query_example?language=Python*
```python
    from flask import Flask,request
    app = Flask(__name__)

    @app.route('/query_example')
    def get_language():
        language = request.args.get("language")
        return f"the language is {language}"

    if __name__=="__main__":
        app.run(debug=True)
```
- **Accesses the Form Data :**
```python
from flask import Flask, request

@app.route("form_example", methods=["POST","GET"])
def form_exemple():
    if request.method == "POST":
        language = request.form.get("language")
        framework = request.form.get("framework")
        return f"language = {language} framework = {framework}"
    return "No data contains return to main page"
```

- **Accesses the JSON Data :**
```python
    from flask import Flask, request
    app = Flask(__name__)

    @app.route("/json_example", methods=["POST"])
    def json_example():

        req_data = request.get_json()

        language = req_data["language"]
        framework = req_data["framework"]
        python_version = req_data["version_info"]["python"]
        example = req_data["example"][0]
        boolean_test = req_data["boolean_test"]

        return f"""
        <h1>Language: {language}</h1>
        <h1>Framework: {framework}</h1>
        <h1>Python Version: {python_version}</h1>
        <h1>Example: {example}</h1>
        <h1>Boolean Value: {boolean_test}</h1>
        """

    if __name__ == "__main__":
        app.run(debug=True)
```


### Rendering Templates
- Flask provides template rendering using the Jinja2 templating engine, which allows HTML pages to display dynamic data. 
- Templates help separate the application logic from the user interface, making web applications easier to manage and build.
- Flask automatically looks for HTML files inside a folder named templates. Create a templates folder in the project directory and add an index.html file inside it.
- index.html :
```html
    <html>
        <head>
            <title> Flask App</title>
        </head>
        <body>
            <h2> Welcome to Flask<h2>
            <p>there is basic template rendering</p>
        </body>
    </html>
```
- render template html:
```python
    from flask import Flask, render_template
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html")

    if __name__ == "__main__":
        app.run()
```
- Pass Dynamic Data Using Jinja2
```python
    from flask import Flask, render_template
    app = Flask(__name__)

    @app.route("/<name>")
    def home(name)
        return render_template("welcome.html", name = name)

    if __name__ == "__main__" : 
        app.run(debug = True)
```
- we will create a welcome.html where we will print the data that we pass trough the template :
```html 
    <h3>
        Welcome, {{name}}
    </h3>
```
- {{ name }} is a Jinja2 placeholder used to display dynamic data.
- The value passed from render_template() replaces {{ name }} during rendering.

- **Logic in Templates :**
- Jinja2 templates support logical operations such as loops and conditional statements. 
- This allows HTML pages to display dynamic content based on data passed from Flask routes. 
```python
    @app.route("/about")
    def about():
        sites = ['twitter', 'facebook', 'instagram', 'whatsapp']
        return render_template("about.html", sites=sites)
```
```html
    {% extends 'index.html'%}
    {% block body %}
    <ul>
        {% for social in sites %}
        <li>{{social}}</li>
        {% endfor %}
    </ul>
    {% endblock %}
```
- {% endfor %} marks the end of the loop block.
-  **Adding Navigation Links :**
- Navigation links help move between Flask routes easily using url_for(). 
```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>FlaskTest</title>
    </head>
    <body>
        <h2>Welcome To GFG</h2>
        <h4>Flask: Rendering Templates</h4>
        <a href="{{ url_for('home') }}">Home</a>
        <a href="{{ url_for('index') }}">Index</a>
        <a href="{{ url_for('about') }}">About</a>
        {% block body %}
        
        <p>This is a Flask application.</p>
        {% endblock %}
    </body>
    </html>
```
- url_for() generates route URLs dynamically.
- {% block body %} creates a section that child templates can replace.
- if-else Conditions in Templates :
```python
    @app.route("/contact/<role>")
    def contact(role):
        return render_template("contact.html", person=role)
```
```html
    {% extends 'index.html' %}
    {% block body %}

    {% if person == "admin" %}
    <p>Admin Section</p>

    {% elif person == "maintainer" %}
    <p>App Source Page for Maintainer</p>

    {% elif person == "member" %}
    <p>Hope you are enjoying our services</p>

    {% else %}
    <p>Hello, {{ person }}</p>

    {% endif %}
    {% endblock %}
```


