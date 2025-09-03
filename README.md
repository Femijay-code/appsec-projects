```markdown
# SQL Injection Safe Demo

This project demonstrates a **secure version** of a login system protected against **SQL Injection** using **Flask** and **SQLite**.  
It is meant to show how **parameterized queries** prevent attackers from bypassing authentication.

---

## Features
- A login page with secure database queries
- Prevents SQL Injection attacks
- Educational demo for safe coding practices

---

## Project Structure

```

sql-injection-safe/
├── app.py              # Main Flask application (safe version)
├── users\_safe.db       # SQLite database with sample users
├── templates/
│   ├── login.html      # Login page template
│   └── home.html       # Dashboard/home page template
└── README.md           # Project documentation

````

---

## Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/Femijay-code/sql-injection-safe.git
cd sql-injection-safe
````

2. **Create a virtual environment** (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

3. **Install dependencies**

```bash
pip install flask
```

4. **Run the application**

```bash
python3 app.py
```

5. **Open in your browser**
   Go to: [http://127.0.0.1:5000/login](http://127.0.0.1:5000/login)

---

## Testing Safe Login

* **Valid credentials:**

```
Username: admin
Password: admin123
```

→ Shows: `Welcome, admin!`

* **SQL Injection attempt:**

```
Username: ' OR '1'='1' --
Password: anything
```

→ Shows: `Login failed` ✅

---

## Screenshots

* `login-page.png` → Login page
* `valid-login.png` → Successful login
* `sqli-attempt.png` → SQLi attempt failed
* `terminal.png` → Terminal running the app

---

## Key Takeaways

* **Parameterized queries** prevent SQL Injection
* Never directly insert user input into SQL queries
* Always validate and sanitize input in real-world applications

---

## Disclaimer

⚠️ This project is for **educational purposes only**.
Do not use these techniques on any system without permission.

```
---
```
