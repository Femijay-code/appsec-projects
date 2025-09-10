# File Upload Vulnerable Demo

This project demonstrates an **insecure file upload vulnerability**.  
The application allows users to upload any file type without restrictions, making it possible to upload malicious scripts (e.g., `.php`, `.html`, `.exe`) that could be executed on the server.

---

## ⚠️ Vulnerability

- No validation of file type or extension.
- No size restrictions.
- Uploaded files are stored directly and could be executed if the server interprets them.

This is a **classic example of Unrestricted File Upload vulnerability** (OWASP A08:2021 – Software and Data Integrity Failures).

---

## 🚀 How to Run

1. Navigate into the project folder:
   ```bash
   cd file-upload-vulnerable

2. Run the Flask app:

   ```bash
   python3 app.py
3. Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## 🎯 Try It

* Upload safe files (e.g., `.png`, `.txt`) → they will be stored.
* Upload malicious files (e.g., `.php`, `.html`) → these are also accepted ❌.

---

## 📌 Purpose

This vulnerable app is for **educational purposes only**, showing how dangerous unrestricted file uploads can be.

````

