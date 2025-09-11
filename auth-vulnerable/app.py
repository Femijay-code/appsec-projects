from flask import Flask, request, redirect, make_response

app = Flask(__name__)

# Hardcoded "users" database (insecure)
users = {
    "admin": "password123",
    "user": "1234"
}

@app.route("/")
def home():
    username = request.cookies.get("username")
    if username:
        return f"<h1>Welcome back, {username}!</h1><br><a href='/logout'>Logout</a>"
    return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Insecure check (plaintext password)
        if username in users and users[username] == password:
            resp = make_response(redirect("/"))
            # 🚨 Vulnerability: Session is just a cookie with username, no security
            resp.set_cookie("username", username)
            return resp
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
    resp = make_response(redirect("/login"))
    resp.delete_cookie("username")
    return resp

if __name__ == "__main__":
    app.run(debug=True)
