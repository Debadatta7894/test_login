# Import required libraries from Flask
from flask import Flask, redirect, url_for, render_template, request, jsonify, session

# Import SQLite database
import sqlite3

# Import password hashing functions for security
from werkzeug.security import generate_password_hash, check_password_hash

# Used for token expiration time
from datetime import timedelta

# Used for generating secure keys (not used here currently)
import secrets

# Import JWT (JSON Web Token) functions
from flask_jwt_extended import (
    JWTManager,              # Initialize JWT
    create_access_token,     # Create token
    jwt_required,            # Protect routes
    get_jwt_identity         # Get logged-in user
)

# Create Flask app
app = Flask(__name__)

# Secret key for session security (important)
app.secret_key = "supersecretkey-change-this"


# ----------------
# JWT CONFIGURATION
# ----------------

# Secret key for JWT token encryption
app.config["JWT_SECRET_KEY"] = "jwt-super-secret-chge-this"

# Token will expire in 1 hour
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

# Initialize JWT with Flask app
jwt = JWTManager(app)


# Database file name
DATABASE = "users.db"


# ----------------
# DATABASE SETUP
# ----------------

# Function to create table if not exists
def init_db():
    conn = sqlite3.connect(DATABASE)  # Connect to database
    cursor = conn.cursor()            # Create cursor

    # Create users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT NOT NULL,
    role TEXT NOT NULL,
    password TEXT NOT NULL)
    """)

    conn.commit()  # Save changes
    conn.close()   # Close connection


# Function to get DB connection
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # Access columns by name
    return conn


# -------------------------
# FRONTEND ROUTES
# -------------------------

# Home route → redirect to signup page
@app.route("/")
def home():
    return redirect(url_for("signup_page"))


# Signup page route
@app.route("/signup", methods=["GET"])
def signup_page():
    return render_template("signup.html")  # Load signup.html


# Login page route
@app.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")   # Load login.html


# Dashboard page route
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")  # Load dashboard.html


# -------------------------------
# API ROUTES
# -------------------------------

# Signup API
@app.route("/api/signup", methods=["POST"])
def signup():

    # Accept form data or JSON data
    data = request.form if request.form else request.get_json()

    # Get user input and remove spaces
    first_name = data.get("first_name").strip()
    last_name = data.get("last_name").strip()
    email = data.get("email").strip()
    phone = data.get("phone").strip()
    role = data.get("role").strip()
    password = data.get("password").strip()
    confirm_password = data.get("confirm_password")

    # Validation: check if any field is empty
    if not all([first_name, last_name, email, phone, role, password, confirm_password]):
        return jsonify({"message": "All fields are required"})

    # Check if passwords match
    if password != confirm_password:
        return jsonify({"message": "Passwords do not match"})

    # Hash the password for security
    hashed_password = generate_password_hash(password)

    try:
        # Insert user into database
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO users (first_name, last_name, email, phone, role, password)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (first_name, last_name, email, phone, role, hashed_password))

        conn.commit()
        conn.close()

        # Redirect to login page after signup
        return redirect(url_for("login_page"))

    except sqlite3.IntegrityError:
        # If email already exists
        return jsonify({"message": "Email already exists"})

    except Exception as e:
        # Handle any other error
        return jsonify({"message": str(e)})


# Get all users API
@app.route("/api/users", methods=["GET"])
def get_users():
    conn = get_db_connection()  # Get DB connection
    users = conn.execute("SELECT * FROM users").fetchall()  # Fetch all users
    conn.close()

    # Convert rows to dictionary format
    user_list = [dict(i) for i in users]

    return jsonify(user_list), 200


# ------------------------------------
# LOGIN API WITH JWT TOKEN
# ------------------------------------

@app.route("/api/login", methods=["POST"])
def login():

    # Accept form or JSON data
    data = request.form if request.form else request.get_json()

    # Get email and password
    email = data.get("email").strip()
    password = data.get("password").strip()

    # Validation
    if not email or not password:
        return jsonify({"message": "Email or password are required"})

    # Fetch user from database
    conn = get_db_connection()
    user = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    conn.close()

    # Check password
    if user and check_password_hash(user["password"], password):

        # Store session
        session["user_email"] = email

        # Create JWT token
        access_token = create_access_token(
            identity=email,  # user identity
            additional_claims={
                "role": user["role"],        # extra data
                "token_type": "user_jwt"
            }
        )

        # Return success response
        return jsonify({
            "message": "Login Successful",
            "access_token": access_token,
            "token_type": "Bearer",
            "redirect_url": "/dashboard"
        })

    # If login fails
    return jsonify({"message": "Invalid credentials"}), 401


# -------------------------
# RUN APPLICATION
# -------------------------

if __name__ == "__main__":
    init_db()              # Create table if not exists
    app.run(debug=True)    # Run Flask app