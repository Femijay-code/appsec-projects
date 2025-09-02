from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__)

# Home/Login Page
@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # ⚠️ Insecure query (SQL Injection demo)
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()

        if result:
            return render_template("dashboard.html", user=username)
        else:
            message = "Invalid credentials!"
    return render_template("login.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)
