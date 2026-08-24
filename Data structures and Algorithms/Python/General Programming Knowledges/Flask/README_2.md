### Template Inheritances
- Template inheritance allows multiple HTML pages to share a common layout using Jinja templates. 
- A base template contains common sections such as headers, footers and navigation bars, while other templates inherit and customize specific parts of that layout.
- Steps : 
    - Set Up a Flask App
    - Create a Base Template
        - Create a file named base.html inside the templates folder. 
        - This file contains the common layout shared by all pages.
        ```html
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <title>My Flask App</title>
                </head>
                <body>
                    <h1>Welcome to My Website</h1>
                    <nav>
                        <a href="/">Home</a> |
                        <a href="/about">About</a>
                    </nav>
                    {% block content %}{% endblock %}
                </body>
            </html>
        ```
        - {% block content %} creates a placeholder for page-specific content.
        - Common elements like headings and navigation bars are written only once in base.html.
    - Create Child Templates
        ```html
            {% extends "base.html" %}

            {% block content %}
                <h2>Home Page</h2>
                <p>Welcome to the homepage of our Flask app!</p>
            {% endblock %}
        ```
        - {% extends "base.html" %} inherits the layout from base.html
        - {% block content %} replaces the content section defined in the base template
        - Only the content inside the {% block content %} section changes
    


### Serve static files in Flask
- Flask uses a dedicated static directory to serve files that do not change dynamically
- stylesheets, JavaScript code, images, videos, and other media assets
- Serve Css :
    ```html
        <head>
            <title>Flask Static Demo</title>
            <link rel="stylesheet" href="/static/style.css" />
        </head>
    ```
- Serve Javascript :
    ```html
        <body>
            <h1>{{message}}</h1>

            <script src="/static/serve.js" charset="utf-8"></script>
        </body>
    ```
- Serve Images :
    ```html
        <img src="/static/cat.jpg" alt="Cat image" width="20%" height="auto" />
        <img src="{{ url_for('static', filename='images/sample.jpg') }}" alt="Sample Image">
    ```
- Serve video :
    ```html
        <video width="320" height="240" controls>
            <source src="/static/ocean_video.mp4" type="video/mp4" />
        </video>
    ```
- Serve Audio : 
    ```html
        <audio controls>
            <source src="/static/audio.mp3" />
        </audio>
    ```
- Serve Pdf and Text File : 
    ```html
        <a href="{{ url_for('static', filename='guide.pdf') }}" target="_blank"> View PDF </a>
        <a href="{{ url_for('static', filename='sample.txt') }}"> Open Text File </a>
    ```



### SQLAlchemy 
- Flask doesn’t have a built-in way to handle databases, so it relies on SQLAlchemy, a library that makes working with databases easier
- Setting Up SQLAlchemy
    - To create a database we need to import SQLAlchemy in app.py, set up SQLite configuration, and create a database instance.
    ```python
        from flask import Flask, render_template, request, redirect
        from flask_sqlalchemy import SQLAlchemy

        app = Flask(__name__)

        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
        db = SQLAlchemy(app)

        if __name__ == '__main__':
            with app.app_context():
                db.create_all()
            app.run(debug=True)
    ```
    - Creating Model :
    ```python
        class Profile(db.Model):
            id = db.Column(db.Integer, primary_key= True)
            first_name = db.Column(db.String(20), unique=False, nullable=False)
            last_name = db.Column(db.String(20), unique=False, nullable=False)
            age = db.Column(db.Integer, nullable= False)

            def __repr__(self):
                return f" Name : {self.first_name}, Age : {self.age}"
    ```
    - Display data on Index Page :
    ```python
        @app.route("/")
        def index(): 
            profiles = Profile.query.all()
            return render_template('index.html', profiles = profiles)
    ```
    -  Creating "/add" routes
    ```python
        @app.routes("/add", methods =["POST"])
        def profile():
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            age = request.form.get("age")
            if first_name !='' and last_name !='' and age is not None:
                p = Profile(first_name = firstaname, last_name = last_name, age = age)
                db.session.add(p)
                db.session.commit()
                return redirect("/")
            else : 
                return redirect("/")
    ```

    - deleting :
    ```python
        @app.routes("/delete/<id>")
        def delete(id):
            data = db.session.get(Profile,id)
            db.session.delete(data)
            db.session.commit()
            return redirect("/")
    ```

    - Final Code :
    ```python
        from flask import Flask, request, redirect
        from flask.templating import render_template
        from flask_sqlalchemy import SQLAlchemy

        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Avoids a warning


        app = Flask(__name__)
        app.debug = True

        # adding configuration for using a sqlite database
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

        # Creating an SQLAlchemy instance
        db = SQLAlchemy(app)

        # Models
        class Profile(db.Model):
            id = db.Column(db.Integer, primary_key=True)
            first_name = db.Column(db.String(20), unique=False, nullable=False)
            last_name = db.Column(db.String(20), unique=False, nullable=False)
            age = db.Column(db.Integer, nullable=False)

            def __repr__(self):
                return f"Name : {self.first_name}, Age: {self.age}"

        # function to render index page
        @app.route('/')
        def index():
            profiles = Profile.query.all()
            return render_template('index.html', profiles=profiles)

        @app.route('/add_data')
        def add_data():
            return render_template('add_profile.html')

        # function to add profiles
        @app.route('/add', methods=["POST"])
        def profile():
            first_name = request.form.get("first_name")
            last_name = request.form.get("last_name")
            age = request.form.get("age")

            if first_name != '' and last_name != '' and age is not None:
                p = Profile(first_name=first_name, last_name=last_name, age=age)
                db.session.add(p)
                db.session.commit()
                return redirect('/')
            else:
                return redirect('/')

        @app.route('/delete/<int:id>')
        def erase(id): 
            data = db.session.get(Profile, id)
            db.session.delete(data)
            db.session.commit()
            return redirect('/')

        if __name__ == '__main__':
            with app.app_context():  # Needed for DB operations outside a request
                db.create_all()      # Creates the database and tables
            app.run(debug=True)
    ```


###  Implement Filtering, Sorting, and Pagination in Flask
- Configure flask application
- Create the Database Model
    ```python
        class Movie(db.Model):
            __tablename__ = "movies"

            id = db.Column(db.Integer, primary_key=True)
            name = db.Column(db.String(100), nullable=False)
            genre = db.Column(db.String(50), nullable=False)
            rating = db.Column(db.Float, nullable=False)

            def format(self):
                return {
                    "id": self.id,
                    "name": self.name,
                    "genre": self.genre,
                    "rating": self.rating
                }
    ```
- Insert Sample Data :
    ```python
        with app.app_context():
            if not Movie.query.first():
                movies = [
                    Movie(name="Inception", genre="Sci-Fi", rating=8.8),
                    Movie(name="The Dark Knight", genre="Action", rating=9.0),
                    Movie(name="Interstellar", genre="Sci-Fi", rating=8.7),
                    Movie(name="Parasite", genre="Thriller", rating=8.5),
                    Movie(name="Avengers: Endgame", genre="Action", rating=8.4),
                    Movie(name="The Matrix", genre="Sci-Fi", rating=8.7),
                    Movie(name="Joker", genre="Drama", rating=8.4),
                ]

                db.session.bulk_save_objects(movies)
                db.session.commit()
    ```
- Filtering in Flask
    ```python
        from flask import Flask, request
        @app.route("/movie/filter")
        def filter_movier():
            genre = request.args.get("genre")
            movies = Movie.query.filter(Movie.genre.ilike(genre)).all()
            results = [movie.format() for movie in movies]
            return jsonify[
                {
                    "success": True,
                    "count" : len(results)
                    "results": results
                }
            ]

    ```
- Sorting in Flask
    ```python
        from flask import jsonify

        @app.route("/movies/sort")
        def sort_movies():
            movies = Movie.query.order_by(Movie.rating.desc()).all()

            results = [movie.format() for movie in movies]

            return jsonify({
                "success": True,
                "count": len(results),
                "results": results
            })
    ```
- Pagination in Flask :
    - Pagination divides large datasets into smaller pages, 
    - reducing the amount of data returned in a single request. 
    - This improves response time and makes it easier to navigate through records
    ```python
        from flask import Flask, jsonify
        @app.route("/movies")
        def get_movies():
            page = request.args.get("page", 1, int)
            per_page = 5 
            pagination = Movie.query.paginate(
                page = page,
                per_page = per_page,
                error_out = False
            )
            movies = [movie.format() for movie in pagination.items]
            return jsonify({
                "success": True,
                "page": page,
                "per_page": per_page,
                "total_records": pagination.total,
                "total_pages": pagination.pages,
                "has_next": pagination.has_next,
                "has_prev": pagination.has_prev,
                "results": movies
            })
    ```
    - request.args.get() retrieves the page number from the query parameters.
    - paginate() divides the query results into pages.
    - pagination.items returns only the records for the requested page.
    - pagination.total returns the total number of records.
    - pagination.pages returns the total number of available pages.
    - has_next and has_prev indicate whether the next or previous page exists
    - Flask-SQLAlchemy provides the paginate() method to divide query results into smaller pages. 
    - It returns a pagination object containing the records for the requested page along with useful metadata 
    - such as the total number of records and pages.
    - page: The page number to retrieve. The default value is 1.
    - per_page: The maximum number of records returned per page.
    - error_out: If True, an invalid page number returns a 404 error. 
    - If False, an empty result set is returned instead.


### Middlewares
- Flask provides middleware support through request hooks, allowing applications to process requests, modify responses, and implement features like logging and authentication. 
    - Checking user authentication before processing a request
    - Capturing request details for debugging and analytics
    - Ensuring requests meet certain criteria before reaching the main app
    - Adding or modifying headers before sending a response
    - Controlling request rates and preventing malicious activities
- **Creating Custom Middleware :**
- Flask provides hooks, which are special functions that allow you to execute code before or after processing a request. 
- These hooks help in modifying requests, logging, authentication, and more.
    - **before_request**: Runs before the request is processed.
    - **after_request**: Runs after the request is processed, modifying the response if needed
    ```python
        from flask import Flask, request

        app = Flask(__name__)

        @app.before_request
        def log_request():
            print(f"Incoming request: {request.method} {request.url}")

        @app.after_request
        def log_response(response):
            print(f"Outgoing response: {response.status_code}")
            return response

        @app.route('/')
        def home():
            return "Hello, Flask!"

        if __name__ == '__main__':
            app.run(debug=True)
    ```
    - **@app.before_request**: Middleware that handles incoming requests by executing log_request() before each request and printing the HTTP method and request URL.
    - **@app.after_request**: Middleware that handles outgoing responses by executing log_response(response) after each request, logging the response status code, and returning the response to complete the request cycle.
    - Authentication middleware ensures that only authorized users can access specific routes. 
    - This is useful for securing APIs and web applications.
    ```python
        from flask import Flask, request, jsonify

        app = Flask(__name__)

        API_KEY = "my_secret_api_key"

        @app.before_request
        def check_authentication():
            token = request.headers.get("Authorization")
            if token != f"Bearer {API_KEY}":
                return jsonify({"error": "Unauthorized"}), 401

        @app.route('/protected')
        def protected():
            return jsonify({"message": "Welcome to the protected route!"})

        if __name__ == '__main__':
            app.run(debug=True)
    ```

- **Third-Party Middleware :**
- Instead of writing custom middleware for every feature, we can use Flask extensions or third-party libraries for advanced middleware functionalities.
    - Flask-CORS: Handles Cross-Origin Resource Sharing (CORS).
    - Flask-Limiter: Implements rate limiting to prevent abuse.
    - Flask-Talisman: Adds security headers for better protection.

- **Cross-Origin Resource Sharing :**
    - CORS is a security feature implemented by web browsers that restricts how resources on a web page can be requested from another domain.
    - For example, if your frontend (React, Vue, or plain JavaScript) is running on http://localhost:3000 and your Flask backend is running on http://127.0.0.1:5000, the browser will block requests from the frontend to the backend due to CORS policy. 
    - CORS middleware allows controlled access to your Flask API from different origins.
    ```python
        from flask import Flask, jsonify
        from flask_cors import CORS

        app = Flask(__name__)

        # Allow requests only from specific frontend origins
        CORS(app, origins=["http://localhost:3000", "https://myfrontend.com/"])

        @app.route('/public-data')
        def public_data():
            return jsonify({"message": "This data is accessible from allowed origins."})

        @app.route('/private-data')
        def private_data():
            return jsonify({"message": "This endpoint also follows CORS rules."})

        if __name__ == '__main__':
            app.run(debug=True)
    ```
- Using Multiple Middleware Layers :
    - Multiple middleware functions can be used in Flask to process requests before they reach route handlers, enabling features like logging, authentication, validation, and security checks without repeating logic across routes.


### WSGI Middlewares
- Middleware is used to process and modify requests and responses before they reach the application or client. 
- While Flask provides request hooks such as before_request and after_request, WSGI (Web Server Gateway Interface) middleware operates at a lower level between the web server and the Flask application, 
- allowing requests and responses to be intercepted and modified before reaching Flask.
- WSGI is faster than flask 
- WSGI is framework agnostic
- WSGI middleware intercepts a raw HTTP request before Flask even knows it exists, whereas Flask hooks intercept the request after Flask has initialized its internal environment.
- WSGI middleware operates at the web server level outside of Flask, while Flask middleware (via request hooks) runs inside the framework with full access to Flask's application context.

| Feature | WSGI Middleware | Flask Middleware (Request Hooks) |
|---|---|---|
| Execution Layer | Between the WSGI Server (e.g., Gunicorn) and Flask. | Deep inside the Flask application. |
| Data Format | Raw Python dictionaries (`environ`) and strings. | High-level Flask request and response objects. |
| Context Access | No access to Flask globals like `g`, `session`, or `current_app`. | Full access to Flask route variables and app context. |
| Routing Aware | No. It cannot target specific endpoints easily. | Yes. It can be bound to specific Blueprints or routes. |
| Implementation | Custom Python classes or callables wrapping the app. | Decorators like `@app.before_request` and `@app.after_request`. |

- **Use Cases: Which One to Choose?**
- Use WSGI Middleware When You Need Framework-Agnostic, Global ActionsBecause it runs before Flask loads, WSGI middleware is faster, isolated, and completely independent of your routing logic.
    - **Fixing Reverse Proxies**: Correcting headers (like X-Forwarded-For) if your application is sitting behind a load balancer or Nginx (e.g., Werkzeug's ProxyFix)
    - **Global Security & Firewalls**: Blocking specific IP addresses, basic rate-limiting, or enforcing global HTTPS redirects before loading heavy application memory.
    - **Routing specific URL prefixes to entirely separate Python apps** (e.g., /api goes to Flask, but /legacy goes to an older framework)
    -  **Handling or offloading asset delivery** before hitting the application routing layer.
- Use Flask Middleware When You Need Application Logic and Context.
    - **User Authentication & Authorization**: Extracting a bearer token, validating it, and attaching the user profile directly to the Flask g or session object.
    - **Database Connection Management**: Opening a database session before a route runs (@app.before_request) and tearing it down safely after it completes (@app.teardown_request).
    - **Scoped Blueprint Logic**: Running specific logic (like language localization) strictly for your /dashboard routes while ignoring your public landing page.
    - **Custom Application Logging**: Logging detailed analytics that include the name of the matched Python view function or specific user IDs
- Implementation :
    - WSGI middleware follows a specific pattern:
    - It is implemented as a class that takes the Flask app as an argument.
    - The class must define a __call__ method, which processes the WSGI environment (incoming request details) and start_response (the response handler).
    - The modified request is then passed to the Flask app.
    ```python
        class customWSGIMiddleWare:
            def __init__(self,app):
                self.app = app
            
            def __call__(self, environ, start_response):
                # Modify request before passing it to Flask
                print(f" Incoming request :{environ["REQUEST_METHOD"]}{environ["PATH_INFO"]}")

                # Process the request with the Flask app
                response = self.app(environ, start_response)
                
                # Modify response if needed
                return response
        
        #to apply the above WSGI Middleware to a flask app use this:
        app.wsgi_app = CustomWSGIMiddleware(app.wsgi_app)
    ```
    - Creating Custom Logging WSGI Middleware
    ```python
        from flask import Flask

        class CustomWSGIMiddleware():
            def __init__(self, app):
                self.app = app
            
            def __call__(self, environ, start_response):
                print(f"Incoming request: {environ['REQUEST_METHOD']} {environ['PATH_INFO']}")
                return self.app(environ, start_response)

        app = Flask(__name__)
        app.wsgi_app = CustomWSGIMiddleware(app.wsgi_app)

        @app.route("/hello")
        def hello():
            return "Hello wsgi middleware"
    ```
    - __call__: This method intercepts the request before it reaches Flask.
    - environ: Contains request details like method and path.
    - start_response: A callable provided by the WSGI server used to start the HTTP response.
    - app.wsgi_app = WSGILoggingMiddleware(app.wsgi_app): Applies the middleware to Flask.

- Third-Party WSGI Middleware :
    - Instead of writing custom middleware, you can use pre-built WSGI middleware. 
    - A popular option is Werkzeug’s ProxyFix, which helps handle reverse proxy headers (like Nginx or a load balancer). 
    - Reverse proxies often modify headers like REMOTE_ADDR, HTTP_HOST, and SCRIPT_NAME, which Flask wouldn't recognize correctly by default.
    ```python
        from werkzeug.middleware.proxy_fix import ProxyFix
        from flask import Flask

        app = Flask(__name__)
        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1, x_prefix=1)

        @app.route('/')
        def home():
            return "ProxyFix Middleware Applied!"

        if __name__ == '__main__':
            app.run(debug=True)
    ```
    - ProxyFix(app.wsgi_app, x_for=1, x_host=1) configures Flask to trust specific proxy headers when the application is deployed behind a reverse proxy.
    - x_for=1 allows Flask to use the first X-Forwarded-For header to identify the client’s actual IP address.
    - x_host=1 enables Flask to determine the correct host using the X-Forwarded-Host header.

### Flask Session
- Sessions in Flask store user-specific data across requests, like login status, using cookies. 
- Data is stored on the client side but signed with a secret key to ensure security. 
- They help maintain user sessions without requiring constant authentication.
- we will implement server-side sessions in Flask using the Flask-Session extension. 
- Installation : 
    ```bash
        pip install flask flask-session
    ```
- Importing Modules and Configuring Flask-Session
    - The configuration sets the session type (filesystem) and defines whether sessions are permanent.
    ```python
        from flask import Flask, render_template, redirect, request, session
        from flask_session import Session
        from datetime import timedelta

        app = Flask(__name__)

        app.config["SESSION_PERMANENT"] = False     # Sessions expire when the browser is closed
        app.config["SESSION_TYPE"] = "filesystem"     # Store session data in files
        app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=10)
        app.config["SESSION_REFRESH_EACH_REQUEST"] = True

        # Initialize Flask-Session
        Session(app)
    ```
    - Module Imports: Import Flask, its built-in session, and the Flask-Session extension, Configuration:
        - SESSION_PERMANENT is set to False so sessions expire when the browser closes.
        - SESSION_TYPE is set to "filesystem" so that session data is stored on the server's disk.
        - Initialization: Calling Session(app) configures the Flask app to use the server-side session mechanism.
    - Defining Routes for Session Handling :
        ```python
        
        @app.route("/")
        def index():
            # If no username in session, redirect to login
            if not session.get("name"):
                return redirect("/login")
            return render_template("index.html")

        @app.route("/login", methods=["GET", "POST"])
        def login():
            if request.method == "POST":
                # Record the user name in session
                session["name"] = request.form.get("name")
                return redirect("/")
            return render_template("login.html")

        @app.route("/logout")
        def logout():
            # Clear the username from session
            session["name"] = None
            return redirect("/")
        ```



### Login Mechanism
- verify email and password in database
- if exist retrieve and  create session with user informations
- go to database and verify

### Logout Mechanism 
- delete all sessions informations

### Register Mechanism
- verify format email, birth date, valid email format
- verify if email already exist, if the case go back to register page and tell user
- verify all the data 
- then store the users informations

### Flask Login
- Installation :
```bash
    pip install flask flask_sqlalchemy flask_login werkzeug
```
- flask-Login: Manages user sessions and authentication.
- flask-SQLAlchemy: Stores user data like usernames and passwords.
- Werkzeug: Used for secure password hashing and verification
- LoginManager :
    - manages the authentication system
    - remembering who is logged in
    - loading users
    - protecting routes
    - managing the login session
- UserMixin :
    - This is a helper class that gives your User model the methods/properties Flask-Login expects.
    - Flask-Login knows how to handle things such as:
        - user.is_authenticated
        - user.is_active
        - user.is_anonymous
        - user.get_id()
- login_user : 
    - Once login_user(user) executes, Flask-Login stores information in the session indicating that this user is authenticated.
    - The exact session data is managed by Flask-Login; you generally shouldn't manually manipulate it.
- logout_user :
    - It removes the user's authenticated state.
    - logout_user()
- login_required :
    - This is a decorator used to protect routes.
    - The user must log in before accessing 
- current_user : 
    - current_user
    - This represents the currently authenticated user.
    - current_user.username
- Password hashing :
    - You should never store passwords directly in your database.
    ```python
        from werkzeug.security import generate_password_hash, check_password_hash
        password_hash = generate_password_hash("mypassword123")
        user.password = password_hash
        check_password_hash(
            user.password,
            password
        )
    ```
    - You don't hash it yourself and compare strings manually.
    - password is the plain-text password entered by the user.

- Implementation : Step 1 
    -  Import the necessary modules and configuration
    ```python
        from flask import Flask, render_template, request, url_for, redirect
        from flask_sqlalchemy import SQLAlchemy
        from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
        from werkzeug.security import generate_password_hash, check_password_hash

        # Initialize Flask app
        app = Flask(__name__)
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SECRET_KEY"] = "supersecretkey"

        # Initialize database and login manager
        db = SQLAlchemy(app)
        login_manager = LoginManager()
        login_manager.init_app(app)
        login_manager.login_view = "login"
    ```
- Implementation : Step 2
    - Create a User Model & Database
    ```python
        # User model
        class Users(UserMixin, db.Model):
            id = db.Column(db.Integer, primary_key=True)
            username = db.Column(db.String(250), unique=True, nullable=False)
            password = db.Column(db.String(250), nullable=False)

        # Create database
        with app.app_context():
            db.create_all()
    ```
- Implementation : Step 3
    - Adding a user loader
    - Before adding user authentication, we need a function for Flask-Login to retrieve a user by ID.
    - Flask-SQLAlchemy handles this, so we can simply use the get() method with the user ID
    ```python
        # Load user for Flask-Login
        @login_manager.user_loader
        def load_user(user_id):
            return Users.query.get(int(user_id))
    ```
- Implementation : Step 4
    - Registering new accounts with Flask-Login
    - Create an HTML registration form (sign_up.html).
    - Create a /register route to handle user registration.
    - We check if the request method is POST using Flask’s request object.
    - we create a new user using the Users model, getting the username and password from request.form.get().
    - The user is added to the session, and changes are committed
    - We redirect the user to the login route using redirect(url_for("login"))
    ```python
        # Register route
        @app.route('/register', methods=["GET", "POST"])
        def register():
            if request.method == "POST":
                username = request.form.get("username")
                password = request.form.get("password")

                if Users.query.filter_by(username=username).first():
                    return render_template("sign_up.html", error="Username already taken!")

                hashed_password = generate_password_hash(password, method="pbkdf2:sha256")

                new_user = Users(username=username, password=hashed_password)
                db.session.add(new_user)
                db.session.commit()

                return redirect(url_for("login"))
            
            return render_template("sign_up.html")
    ```

- Implementation : Step 5
    - Create an HTML login form (login.html)
    - Implement a /login route to authenticate users
    - Check if the request method is POST.
    - If POST, filter the database for a user with the entered username.
    - Compare the stored password with the entered password.
    - If they match, log in the user using Flask-Login’s login_user function.
    - Redirect the user to the dashboard route.
    - If the request is GET, render the login template.
    ```python
        # Login route
        @app.route("/login", methods=["GET", "POST"])
        def login():
            if request.method == "POST":
                username = request.form.get("username")
                password = request.form.get("password")

                user = Users.query.filter_by(username=username).first()

                if user and check_password_hash(user.password, password):
                    login_user(user)
                    return redirect(url_for("dashboard"))
                else:
                    return render_template("login.html", error="Invalid username or password")

            return render_template("login.html")
    ```
- Implementation : Step 6
    - Logout Functionality
    ```python
    # Logout route
    @app.route("/logout")
    @login_required
    def logout():
        logout_user()
        return redirect(url_for("login"))
    ```


### Hashing with Bcrypt 
- Password hashing converts plaintext passwords into secure hashed values that cannot be easily reversed.
- Bcrypt is a widely used password-hashing function 
- based on the Blowfish cipher, designed to be computationally expensive and resistant to brute-force attacks
- making password storage more secure in Flask applications.
- Password Hashing: The process of converting a plaintext password into a secure hashed format.
- Bcrypt: A password-hashing function based on the Blowfish cipher.
- Salt: Random data that is used as additional input to a one-way function that hashes a password or passphrase.
- Hashing Algorithm: A mathematical function that converts a plaintext password into a fixed-length hash value.
- Iterations: Iterations (Cost Factor): Determines how computationally expensive the bcrypt hashing process will be.
- Installation : 
```bash
    pip install flask flask-bcrypt
```
- Import :
```python
    from flask_bcrypt import Bcrypt
```
- Create a Bcrypt Object :
```python
    bcrypt = Bcrypt(app)
```
- Hash a Password : 
```python
    hashed_password = bcrypt.generate_password_hash(
                        'password'
                    ).decode('utf-8')
```
- The generated hash is decoded using decode('utf-8') because the method returns the hash as a bytes object.
- Check password :
```python
    is_valid = bcrypt.check_password_hash(
        hashed_password,
        'password'
    )
```