### JWT for user authentication 
- JWT (JSON Web Token) is a compact, secure, and self-contained token used for securely transmitting information between parties. 
- It is often used for authentication and authorization in web applications. 
- JWT consists of three parts:
    - Header - Contains metadata (e.g., algorithm used for signing).
    - Payload - Stores user information (claims like user ID, roles).
    - Signature - Ensures token integrity using a secret key.

- In Flask, JWT is commonly used to authenticate users by issuing tokens upon login and verifying them for protected routes. 
- Installasion :
```python
    pip install Flask Flask-SQLAlchemy Werkzeug PyJWT
```
- App Configuration :
```python
    from flask import Flask, render_template, request, redirect, url_for, jsonify, make_response
    from flask_sqlalchemy import SQLAlchemy
    from werkzeug.security import generate_password_hash, check_password_hash
    import jwt
    import uuid
    from datetime import datetime, timezone, timedelta
    from functools import wraps

    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Database setup
    db = SQLAlchemy(app)
```
- Creating the User Model :
```python
    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        public_id = db.Column(db.String(50), unique=True)
        name = db.Column(db.String(100))
        email = db.Column(db.String(70), unique=True)
        password = db.Column(db.String(80))
```
- Implementing Authentication (Login and Registration) : 
```python
    @app.route('/signup', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']

            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                return jsonify({'message': 'User already exists. Please login.'}), 400

            hashed_password = generate_password_hash(password)
            new_user = User(public_id=str(uuid.uuid4()), name=name, email=email, password=hashed_password)

            db.session.add(new_user)
            db.session.commit()

            return redirect(url_for('login'))

        return render_template('register.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password']
            user = User.query.filter_by(email=email).first()

            if not user or not check_password_hash(user.password, password):
                return jsonify({'message': 'Invalid email or password'}), 401

            token = jwt.encode(
                {
                    'public_id': user.public_id, 
                    'exp': datetime.now(timezone.utc) + timedelta(hours=1)
                }, 
                app.config['SECRET_KEY'], 
                algorithm="HS256"
            )

            response = make_response(redirect(url_for('dashboard')))
            response.set_cookie('jwt_token', token)

            return response

        return render_template('login.html')
```
- Implementing JWT Token Verification :
```python
    def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = request.cookies.get('jwt_token')

            if not token:
                return jsonify({'message': 'Token is missing!'}), 401

            try:
                data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
                current_user = User.query.filter_by(public_id=data['public_id']).first()
            except:
                return jsonify({'message': 'Token is invalid!'}), 401

            return f(current_user, *args, **kwargs)

        return decorated
```
- Creating Routes for Home and Dashboard:
```python
    @app.route('/')
    def home():
        return render_template('login.html')

    @app.route('/dashboard')
    @token_required
    def dashboard(current_user):
        return f"Welcome {current_user.name}! You are logged in."
```

### Role Base Acess Control ( Rbac )
- Role-Based Access Control (RBAC) is a security mechanism that restricts user access based on their roles within an application.
- Instead of assigning permissions to individual users, RBAC groups users into roles and each role has specific permissions.
- This approach improves security, simplifies permission management and ensures users only access what they need.
- Installation : 
    ```bash
    pip install flask flask-security flask-sqlalchemy flask-login email-validator
    ```
    - Flask: A lightweight web framework for building web applications.
    - Flask-Security: Adds authentication and role management features.
    - Flask-SQLAlchemy: Integrates SQLAlchemy for easy database operations.
    - Flask-Login: Manages user sessions and handles login/logout.
    - Email-validator: Validates email addresses for correct formatting
- Importing Modules and Setting Configurations :
    ```python
    from flask import Flask, render_template, url_for, request, redirect
    from flask_sqlalchemy import SQLAlchemy
    from flask_login import LoginManager, login_user, logout_user, current_user
    from flask_security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, roles_accepted
    import uuid

    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///g4g.sqlite3"
    app.config['SECRET_KEY'] = 'MY_SECRET'

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view='signin'
    db = SQLAlchemy(app)
    ```
- Create Database Models:
    ```python
    roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
    )
    class User(db.Model, UserMixin):
        __tablename__='user'
        id=db.Column(db.Integer, autoincrement = True , primary_key = True)
        email=db.Column(db.String(255), unique = True, nullable = False)
        password = db.Column(db.String(255), nullable = False, server_default='')
        fs_uniquifier = db.Column(db.String(255), unique = True, nullable = False, default = lambda:uuid.uuid4().hex)
        roles = db.relationship('Role', secondary = roles_users, backref='users')
    class Role(db.Model, RoleMixin):
        id=db.Column(db.Integer(), primary_key = True)
        name = db.Column(db.String(255), unique = True, nullable = False)
    ```
    - Association Table: roles_users is a helper table to create a many-to-many relationship between User and Role.
    - User Model: Contains user details including email, password, activation status and a unique identifier (fs_uniquifier) for security. It also relates to roles.
    - Role Model: Defines roles with a unique ID and name.
- Defining Routes :
    ```python
    from flask_login import login_required
    user_datastore = SQLAlchemyDatastore(db, User, Role)
    security = Security(app,user_datastore)

    @app.route('/')
    def index():
        return render_template("index.html")

    # Signup routes for user registration 
    @app.route('/signup',methods = ['GET', 'POST'])
    def signup():
        msg = ''
        user = User.query.filter_by(email=request.form["email"]).first()
        if user : 
            msg = 'User already exists'
            return render_template("signup.html", msg=msg)
        user = User(email = request.form['email'], password = request.form['password'])
        role = Role.query.filter_by(id = int(request.form['options'])).first()
        if role : 
            user.roles.append(role)
        else :
            msg = "Invalid role selection"
            return render_template("signup.html",msg = msg)
    
    #Signin route for users
    @app.route('/signin')
    def signin():
        msg = ""
        if request.method == "POST":
            user= User.query.filter_by(email = request.form["email"]).first()
            if user :
                if user.password == request.form["password"]:
                    login_user(user)
                    return redirect(url_for('index'))
                else :
                    msg = "wrong password"
            else : 
                msg = "user does'nt exist"
        return render_template("signing.html", msg = msg)
    
    @app.route("/logout")
    def logout():
        logout_user()
        return redirect(url_for("index"))
    
    @app.route('/teachers')
    @login_required
    @roles_accepted("Admins")
    def teachers():
        teacher_list = [

        ]
        role_teachers = db.session.query(roles_users).filter_by(role_id=2).all()
        for teacher in role_teachers:
            user = User.query.filter_by(id = teacher.user_id).first()
            if user : 
                teachers_list.append(user)
        return render_template("teacher.html", teachers = teachers_list)
    
    @app.route('/staff')
    @login_required
    @roles_accepted('Admin', 'Teacher')
    def staff():
        staff_list = []
        role_staff = db.session.query(roles_users).filter_by(role_id=3).all()
        for staff in role_staff :
            user= User.query.filter_by(id=staff.user_id).first()
            if user : 
                staff_list.append(user)
        return render_html("staff.html", staff_list = staff_list)
    
    # Students route (Accessible to Admin, Teacher, and Staff)
    @app.route('/students')
    @login_required
    @roles_accepted('Admin', 'Teacher', 'Staff')
    def students():
        students_list = []
        role_students = db.session.query(roles_users).filter_by(role_id=4).all()
        for s in role_students:
            user = User.query.filter_by(id=s.user_id).first()
            if user:
                students_list.append(user)
        return render_template("students.html", students=students_list)

    # My Details route (Accessible to all roles)
    @app.route('/mydetails')
    @login_required
    @roles_accepted('Admin', 'Teacher', 'Staff', 'Student')
    def mydetails():
        return render_template("mydetails.html")
    ```
    - Explanation
    - Flask-Security Setup: Initializes Flask-Security with the user datastore connecting the User and Role models
    - Home (/): Displays the index page with navigation links.
    - Signup (/signup): Handles user registration and role assignment.
    - Signin (/signin): Authenticates users based on email and password.
    - Logout (/logout): Logs out the user.
    - Protected Routes: (/teachers, /staff, /students, /mydetails) Use the @roles_accepted decorator to restrict access based on roles.
- Creating Roles :
    ```python
    from app import Role, db, app

    def create_roles():
        with app.app_context():
            admin = Role(id=1, name='Admin')
            teacher = Role(id=2, name='Teacher')
            staff = Role(id=3, name='Staff')
            student = Role(id=4, name='Student')

            db.session.add(admin)
            db.session.add(teacher)
            db.session.add(staff)
            db.session.add(student)

            db.session.commit()
            print("Roles created successfully!")

    if __name__ == '__main__':
        create_roles()
    ```

### Flask Cookies
- Cookies store user data in the browser as key-value pairs, allowing websites to remember logins, preferences, and other details. 
- This helps improve the user experience by making the site more convenient and personalized.
- Setting Cookies in Flask :
    - set_cookie( ) method: 
    - Using this method we can generate cookies in any application code. 
    - The syntax for this cookies setting method:
    ```python
    Response.set_cookie(key, value = '', max_age = None, expires = None, path = '/', domain = None,  secure = None, httponly = False)
    ```
    - key – Name of the cookie to be set.
    - value – Value of the cookie to be set.
    - max_age – should be a few seconds, None (default) if the cookie should last as long as the client’s browser session.
    - expires – should be a datetime object or UNIX timestamp.
    - domain – To set a cross-domain cookie.
    - path – limits the cookie to given path, (default) it will span the whole domain.
    ```python
    from flask import Flask, request, make_response
    app = Flask(__name__)
    @app.route('/setcookie')
    def setcookie():
        resp = make_response('Setting the cookie')
        resp.set_cookie('GFG', 'Computer Science Portal')
        return resp
    # getting cookie from the previous set_cookie code
    @app.route('/getcookie')
    def getcookie():
        GFG = request.cookies.get('GFG')
        return 'GFG is a '+ GFG

    app.run()
    ```
    - Login Application in Flask using cookies :
    ```python
    from flask import Flask, request, make_response, render_template

    app = Flask(__name__)

    @app.route('/', methods = ['GET'])
    def Login():
    return render_template('Login.html')

    @app.route('/details', methods = ['GET','POST'])
    def login():
        if request.method == 'POST':
            name = request.form['username']
            output = 'Hi, Welcome '+name+ ''
            resp = make_response(output)
            resp.set_cookie('username', name)
        return resp

    app.run(debug=True)
    ```
    - Tracking Website Visitors Using Cookies :
    ```python
        from flask import Flask, request, make_response

        app = Flask(__name__)
        app.config['DEBUG'] = True


        @app.route('/')
        def vistors_count():
            # Converting str to int
            count = int(request.cookies.get('visitors count', 0))
            # Getting the key-visitors count value as 0
            count = count+1
            output = 'You visited this page for '+str(count) + ' times'
            resp = make_response(output)
            resp.set_cookie('visitors count', str(count))
            return resp


        @app.route('/get')
        def get_vistors_count():
            count = request.cookies.get('visitors count')
            return count


        app.run()
    ```
    - The flask cookies can be secured by putting the secure parameter in response.set_cookie('key', 'value', secure = True)

### Flask Creating Rest APIs
- A REST API (Representational State Transfer API) is a way for applications to communicate over the web using standard HTTP methods. 
- It allows clients (such as web or mobile apps) to interact with a server by sending requests and receiving responses, typically in JSON format.
- REST APIs follow a stateless architecture, meaning each request from a client to the server is independent and does not rely on previous requests. 
- This makes REST APIs scalable, flexible, and easy to integrate with different platforms.
- Key Features of REST APIs:
    - Uses standard HTTP methods for CRUD operations:
        - GET: Retrieve data
        - POST: Send new data
        - PUT: Update existing data
        - DELETE: Remove data
    - Follows a stateless design (each request is processed independently).
    - Uses JSON or XML for structured data exchange.
    - Enables easy integration with web, mobile, and third-party services.
- Creating API Routes for CRUD Operations :
    - GET /books: This route retrieves all books from our dataset and returns them in JSON format.
    - GET /books/<book_id>: This retrieves a single book based on its ID. If the book is not found, it returns a 404 error.
    - POST /books: This allows users to add a new book to the dataset by sending a JSON payload containing the book details.
    - PUT /books/<book_id>: This updates an existing book’s details based on the provided book ID. If the book is not found, it returns an error.
    - DELETE /books/<book_id>: This removes a book from the dataset based on the book ID and returns a confirmation message.
    ```python
        from flask import Flask, jsonify, request

        app = Flask(__name__)

        # Sample data
        books = [
            {"id": 1, "title": "Concept of Physics", "author": "H.C Verma"},
            {"id": 2, "title": "Gunahon ka Devta", "author": "Dharamvir Bharti"},
            {"id": 3, "title": "Problems in General Physsics", "author": "I.E Irodov"}
        ]

        # Get all books
        @app.route('/books', methods=['GET'])
        def get_books():
            return jsonify(books)

        # Get a single book by ID
        @app.route('/books/<int:book_id>', methods=['GET'])
        def get_book(book_id):
            book = next((book for book in books if book["id"] == book_id), None)
            return jsonify(book) if book else (jsonify({"error": "Book not found"}), 404)

        # Add a new book
        @app.route('/books', methods=['POST'])
        def add_book():
            new_book = request.json
            books.append(new_book)
            return jsonify(new_book), 201

        # Update a book
        @app.route('/books/<int:book_id>', methods=['PUT'])
        def update_book(book_id):
            book = next((book for book in books if book["id"] == book_id), None)
            if not book:
                return jsonify({"error": "Book not found"}), 404

            data = request.json
            book.update(data)
            return jsonify(book)

        # Delete a book
        @app.route('/books/<int:book_id>', methods=['DELETE'])
        def delete_book(book_id):
            global books
            books = [book for book in books if book["id"] != book_id]
            return jsonify({"message": "Book deleted"})

        if __name__ == '__main__':
            app.run(debug=True)
    ```


### SubDomains 
-  A subdomain is a child domain that’s part of a larger domain. 
- For example, practice.geeksforgeeks.org and write.geeksforgeeks.org are subdomains of the geeksforgeeks.org domain, which in turn is a subdomain of the org top-level domain (TLD). 
- Setting Up Host Entries :
    - Before writing any Flask code, you need to give your local IP (127.0.0.1) alternate domain names for testing subdomains on your machine. 
    - Open Notepad with administrator access and open the host file of your system in it make edits, path to the host file for:
        - Linux: /etc/hosts
        - Windows: C:\\Windows\\System32\\Drivers\\etc\\hosts
    - Add entries for your custom domain and subdomain in the end of the host file and save changes
        ```text
            127.0.0.1       vibhu.gfg
            127.0.0.1       practice.vibhu.gfg
        ```
    - vibhu.gfg is our main domain, and practice.vibhu.gfg is the subdomain we’ll use in the Flask app.
- Configuring the Server :
    - Flask requires a SERVER_NAME setting for subdomains to work
    - This includes both the domain name and the port number
    ```python
        from flask import Flask

        app = Flask(__name__)
        app.config['SERVER_NAME'] = 'vibhu.gfg:5000'

        @app.route('/')
        def home():
            return "Welcome to GeeksForGeeks !"

        if __name__ == "__main__":
            app.run()
    ```
    - website_url is set to vibhu.gfg:5000, matching the domain name and the Flask default port.
    - app.config['SERVER_NAME'] tells Flask to use vibhu.gfg as the main domain.
- Creating Multiple Endpoints with Subdomains : 
    - We’ll add three routes on the main domain (vibhu.gfg) and subdomain (practice.vibhu.gfg)
    - Subdomains are defined using the subdomain parameter in the @app.route decorator.
    ```python
        from flask import Flask

        app = Flask(__name__)

        @app.route('/')
        def home():
            return "Welcome to GeeksForGeeks !"

        @app.route('/basic/')
        def basic():
            return "Basic Category Articles listed on this page."

        @app.route('/', subdomain='practice')
        def practice():
            return "Coding Practice Page"

        @app.route('/courses/', subdomain='practice')
        def courses():
            return "Courses listed under practice subdomain."

        if __name__ == "__main__":
            website_url = 'vibhu.gfg:5000'
            app.config['SERVER_NAME'] = website_url
            app.run()
        app = Flask(__name__)

        @app.route('/')
        def home():
            return "Welcome to GeeksForGeeks !"

        @app.route('/basic/')
        def basic():
            return "Basic Category Articles listed on this page."

        @app.route('/', subdomain='practice')
        def practice():
            return "Coding Practice Page"

        @app.route('/courses/', subdomain='practice')
        def courses():
            return "Courses listed under practice subdomain."

        if __name__ == "__main__":
            website_url = 'vibhu.gfg:5000'
            app.config['SERVER_NAME'] = website_url
            app.run()
    ```

### Flask CORS
- Flask-CORS is a Flask extension that enables Cross-Origin Resource Sharing (CORS), allowing web applications hosted on different origins to communicate with a Flask backend. 
- It is commonly used when building REST APIs that interact with frontend frameworks such as React, Angular, or Vue.
- Cross-Origin Resource Sharing (CORS) is a browser security mechanism that controls whether a web application can access resources from a different origin. An origin consists of three components:
    - Protocol (http or https)
    - Domain name
    - Port number
- Features of Flask-CORS: 
    - Allow communication between frontend and backend applications running on different origins.
    - Enable API access from web and mobile applications.
    - Simplify handling cross-origin AJAX requests. 
    - Control which domains can access a Flask application.
- Installation : 
    ```bash
        pip install Flask-Cors
    ```
- Enable CORS in the Flask : 
    - CORS(app) enables CORS for all routes.
    - Every endpoint can now receive requests from different origins.
    - Flask automatically sends the required CORS headers.
    ```python
        from flask import Flask
        from flask_cors import Cors
        app = Flask(__name__)
        CORS(app)
        @app.route("/")
        def home():
            return "Hello World !"
        if __name__ == "__main__" :
            app.run(debug = True)
    ```
- Enable CORS for Specific Routes :
    - @cross_origin() enables CORS only for the specified route.
    - Other routes remain unaffected.
    - This approach provides better control over API access.
    ```python
        from flask import Flask 
        from flask_cors import cross_origin
        app = Flask(__name__)
        @app.route("/")
        @cross_origin()
        def home():
            return "Hello World !"
        if __name__=="__main__":
            app.run(debug = True)
    ```
- Flask-CORS Configuration Options : 
    - origins : Specifies allowed domains.
    - methods : Specifies allowed HTTP methods.
    - allow_headers : Specifies allowed request headers.
    - supports_credentials : Allows cookies and authentication headers.
    - max_age : Sets how long browsers cache preflight requests.
    ```python
        from flask import Flask
        from flask_cors import CORS
        app = Flask(__name__)
        CORS(
            app,
            origins=["http://localhost:3000"],
            methods=["GET", "POST"],
            supports_credentials=True
        )
    ```

### Handling 404 Error 
- A 404 Error occurs when a page is not found. This can happen due to several reasons:
    - The URL was changed, but the old links were not updated.
    - The page was deleted from the website.
    - The user mistyped the URL.
- To improve user experience, websites should have a custom error page instead of showing a generic
```python
    from flask import Flask, render_template
    app = Flask(__name__)
    @app.errorhandler(404)
    def not_found(e):
        return render_template("404.html")
```

### Flask RESTFUL Extension
- Flask-RESTful is an extension for Flask that simplifies the process of building REST APIs. 
- It provides additional tools for creating APIs with minimal boilerplate code while following REST principles.
- With Flask-RESTful, defining API resources, handling requests, and formatting responses become more structured and efficient.
- Features of Flask-RESTful:
    - Simplifies API Development – Provides a cleaner and more structured approach.
    - Automatic Request Parsing – Built-in support for handling request arguments.
    - Better Resource Management – Uses classes to define API resources.
    - Response Formatting – Automatically formats responses in JSON.
    - Integrated Error Handling – Provides built-in exception handling for common errors.