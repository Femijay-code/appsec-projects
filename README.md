```markdown
# SQL Injection Demo

This project demonstrates a simple **SQL Injection vulnerability** using **Flask** and **SQLite**.  
It is meant for educational purposes only to understand how SQL Injection works and why secure coding practices are important.

---

## Features
- A login page with a vulnerable SQL query
- Demonstrates how attackers can bypass authentication using SQL Injection
- Example payloads you can test

---

## Project Structure

```

sql-injection-demo/
├── app.py              # Main Flask application
├── users.db            # SQLite database with sample users
├── templates/
│   ├── login.html      # Login page template
│   └── home.html       # Dashboard/home page template
└── README.md           # Project documentation

````

---

## Run Locally

1. **Clone the repository**
```bash
git clone https://github.com/Femijay-code/sql-injection-demo.git
cd sql-injection-demo
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

## Example SQL Injection Payloads

Try logging in with:

```
Username: admin' --
Password: anything
```

This works because the app does not properly sanitize user input.

---

## Disclaimer

⚠️ This project is for **educational purposes only**.
Do not use these techniques on any system without permission.

```
```
