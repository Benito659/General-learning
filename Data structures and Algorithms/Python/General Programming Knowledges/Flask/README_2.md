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
