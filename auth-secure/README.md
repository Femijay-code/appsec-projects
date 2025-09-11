# Authentication Demo (Secure)

This is the **secure implementation** of the authentication demo, showing how to properly handle sessions and credentials.

---

## 🔒 Security Features

- **Hashed passwords** (using `werkzeug.security`).
- **Session tokens** stored securely with Flask sessions.
- **Proper login/logout flow**.
- **Access control** → `/dashboard` requires authentication.
- **No hardcoded credentials**.

---

## 🚀 How to Run

1. Navigate into this folder:
   ```bash
   cd auth-secure

2. Run the app:

   ```bash
   python3 app.py

3. Open in your browser:

   ```
   http://127.0.0.1:5000

---

## 🎯 Learning Goals

* Learn how to **hash and verify passwords** properly.
* Understand how Flask sessions prevent unauthorized access.
* Compare secure vs insecure authentication mechanisms.

````
