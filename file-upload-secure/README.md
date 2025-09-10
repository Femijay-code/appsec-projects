# File Upload Secure Demo

This project demonstrates a **secure implementation of file upload handling**.  
The application validates file types, enforces size limits, and securely stores uploaded files.

---

## 🔒 Security Controls

- Only specific file extensions allowed: `.png`, `.jpg`, `.jpeg`, `.gif`, `.txt`, `.pdf`
- File size limit of **2 MB**
- Uses `werkzeug.utils.secure_filename` to sanitize filenames
- Prevents path traversal (`../../etc/passwd`)
- Blocks dangerous file types (e.g., `.php`, `.exe`, `.html`)

---

## 🚀 How to Run

1. Navigate into the project folder:
   ```bash
   cd file-upload-secure
````

2. Run the Flask app:

   ```bash
   python3 app.py
   ```
3. Open your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## 🎯 Try It

* ✅ Upload allowed files (e.g., `.png`, `.txt`, `.pdf`) → works.
* ❌ Upload disallowed files (e.g., `.php`, `.exe`, `.html`) → blocked.
* ❌ Upload files >2 MB → blocked.

---

## 📌 Purpose

This app demonstrates **secure coding practices** to prevent **Unrestricted File Upload vulnerabilities**, aligned with **OWASP recommendations**.

````

