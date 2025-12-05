from flask import Flask, render_template, request, redirect, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key_here"

# ---------------------------------------------
# Database Initialization
# ---------------------------------------------
def init_db():
    con = sqlite3.connect("users.db")
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            email TEXT UNIQUE,
            password TEXT
        )
    """)
    con.commit()
    con.close()

init_db()


# ---------------------------------------------
# Routes
# ---------------------------------------------
@app.route("/")
def home():
    if "user" in session:
        return redirect("/dashboard")
    return redirect("/login")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = generate_password_hash(request.form["password"])

        con = sqlite3.connect("users.db")
        cur = con.cursor()

        try:
            cur.execute("INSERT INTO users(username, email, password) VALUES (?,?,?)",
                        (username, email, password))
            con.commit()
            con.close()
            return redirect("/login")
        except:
            return "Error: Username or email already exists!"

    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        con = sqlite3.connect("users.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE username=?", (username,))
        user = cur.fetchone()

        if user and check_password_hash(user[3], password):
            session["user"] = username
            return redirect("/dashboard")
        else:
            return "Invalid username or password!"

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")
    return render_template("dashboard.html", user=session["user"])


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)
