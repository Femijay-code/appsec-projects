# Authentication Demo (Vulnerable)

This is a deliberately **insecure authentication system** to demonstrate common flaws in session management.

---

## ⚠️ Vulnerabilities

- **Hardcoded credentials** (`admin` / `password`).
- **No session tokens** → users stay “logged in” just by visiting `/dashboard`.
- **No password hashing** → credentials are stored and compared in plaintext.
- **No logout mechanism** → users cannot properly end a session.

---

## 🚀 How to Run

1. Navigate into this folder:
   ```bash
   cd auth-vulnerable

2. Run the app:

   ```bash
   python3 app.py

3. Open in your browser:

   ```
   http://127.0.0.1:5000

---

## 🎯 Learning Goals

* Understand why hardcoding passwords is dangerous.
* Learn why proper session management is critical.
* Recognize how attackers can bypass weak authentication systems.

````

