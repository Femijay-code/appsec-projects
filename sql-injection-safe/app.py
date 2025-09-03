from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# Initialize database
def init_db():
    conn = sqlite3.connect("users_safe.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT)")
    cursor.execute("INSERT OR IGNORE INTO users VALUES ('admin', 'admin123')")
    cursor.execute("INSERT OR IGNORE INTO users VALUES ('user', 'password')")
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return "<h1>Welcome to Safe SQL App</h1><p>Go to /login to test</p>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users_safe.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # ✅ Safe parameterized query
        query = "SELECT * FROM users WHERE username=? AND password=?"
        cursor.execute(query, (username, password))
        row = cursor.fetchone()
        conn.close()

        if row:
            return f"<h2>Welcome, {row['username']}!</h2>"
        else:
            return "<h2>Login failed</h2>"

    return render_template_string('''
        <form method="post">
            <input type="text" name="username" placeholder="Username"><br>
            <input type="password" name="password" placeholder="Password"><br>
            <input type="submit" value="Login">
        </form>
    ''')

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
