---

# 🛡️ XSS Secure Demo

This project is the **secure version** of the XSS (Cross-Site Scripting) demo app.
It shows how to defend against malicious script injection by sanitizing user input.

---

## ✨ Features

* Uses the **Bleach library** to sanitize user input before rendering.
* Prevents execution of injected scripts like `<script>alert("XSS Attack!")</script>`.
* Demonstrates **best practices** for defending against XSS.

---

## 📂 Project Structure

```
xss-secure/
│
├── app.py          # Secure Flask application
└── README.md       # Project documentation
```

---

## 🚀 Run Locally

1. Navigate into the project folder:

   ```bash
   cd xss-secure
   ```

2. (Optional) Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:

   ```bash
   pip install flask bleach
   ```

4. Run the application:

   ```bash
   python3 app.py
   ```

5. Open in your browser:

   ```
   http://127.0.0.1:5000/
   ```

---

## ✅ Expected Behavior

* Malicious scripts (like `<script>alert("XSS Attack!")</script>`) are **not executed**.
* Instead, they are displayed back safely as plain text.

---

## 🎯 Purpose

* Show how simple input sanitization protects against XSS attacks.
* Highlight the importance of secure coding practices in web development.

---

⚠️ **Disclaimer:** This project is for **educational purposes only**.

---


