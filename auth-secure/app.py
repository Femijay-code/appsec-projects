from flask import Flask, request, redirect, render_template_string, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "supersecretkey123"  # Should be random and stored securely

# Secure "database" with hashed passwords
users = {
    "admin": generate_password_hash("password123"),
    "user": generate_password_hash("1234")
}

@app.route("/")
def home():
    if "username" in session:
        return f"<h1>Welcome back, {session['username']}!</h1><br><a href='/logout'>Logout</a>"
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and check_password_hash(users[username], password):
            session["username"] = username
            return redirect(url_for("home"))
        return "<h3>Invalid credentials</h3><a href='/login'>Try again</a>"

    return '''
        <h2>Login</h2>
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
