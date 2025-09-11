# Application Security Projects

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey?logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?logo=sqlite)
![Security](https://img.shields.io/badge/Focus-Application%20Security-red?logo=datadog)


This repository is a growing collection of my hands-on **application security projects**.
Each project demonstrates common security vulnerabilities and their secure implementations, helping to bridge the gap between theory and practice.

---

## 📑 Table of Contents
- [Current Projects](#-current-projects)
- [Projects Overview Table](#-projects-overview-table)
- [Roadmap](#-roadmap-upcoming-projects)
- [How to Use](#-how-to-use)
- [Purpose](#-purpose)
- [Disclaimer](#-disclaimer)


---

## 📂 Current Projects

### 1. SQL Injection Demo
* **Folder:** `sql-injection-demo/`
* A deliberately vulnerable web application showcasing **SQL Injection (SQLi)** attacks.
* Goal: Learn how SQLi works, identify vulnerabilities, and practice exploiting them in a safe environment.

### 2. SQL Injection Safe Version
* **Folder:** `sql-injection-safe/`
* A secure version of the SQLi demo app.
* Demonstrates how to properly implement **input validation, prepared statements, and secure coding practices** to prevent SQL Injection.

### 3. Reflected XSS Demo (Vulnerable)
* **Folder:** `xss-vulnerable/`
* A web application that does **not sanitize user input**, allowing reflected XSS attacks.
* Goal: Understand how attackers inject malicious scripts into web pages.

### 4. Reflected XSS Demo (Secure)
* **Folder:** `xss-secure/`
* A secure version of the reflected XSS demo that uses **input sanitization (Bleach library)** to prevent execution of malicious scripts.
* Demonstrates how to protect against XSS vulnerabilities.

### 5. Stored XSS Demo (Vulnerable)
* **Folder:** `xss-stored-vulnerable/`
* A web application vulnerable to **stored cross-site scripting**, where malicious input is saved in the database and shown to all visitors.
* Goal: Demonstrate how stored XSS persists across sessions and impacts multiple users.

### 6. Stored XSS Demo (Secure)
* **Folder:** `xss-stored-secure/`
* A secure version of the stored XSS demo that sanitizes input before saving it to the database.
* Shows how proper **input sanitization and output encoding** prevent stored XSS attacks.
  
### 7. Command Injection Demo (Vulnerable)
* **Folder:** `command-injection-vulnerable/`
* A deliberately vulnerable app that allows **unsanitized system command execution**.
* Goal: Understand how attackers exploit command injection flaws to run arbitrary commands on the host.

### 8. Command Injection Demo (Secure)

* **Folder:** `command-injection-secure/`
* A secure version of the demo that uses **input validation and safe system command handling**.
* Demonstrates how to mitigate command injection vulnerabilities effectively.

### 9. File Upload Demo (Vulnerable)
* **Folder:** `file-upload-vulnerable/`
* A deliberately vulnerable app that allows **unrestricted file uploads**.
* Goal: Understand risks like malicious scripts, webshells, and unauthorized access.

### 10. File Upload Demo (Secure)
* **Folder:** `file-upload-secure/`
* A secure version of the file upload demo.
* Implements **file type validation, size limits, and safe storage practices** to prevent exploitation.

---

## 📊 Projects Overview Table

| Vulnerability       | Vulnerable App | Secure App | Key Fix Implemented |
|---------------------|---------------|------------|---------------------|
| SQL Injection       | [`sql-injection-demo`](./sql-injection-demo) | [`sql-injection-safe`](./sql-injection-safe) | Parameterized queries, input validation |
| Reflected XSS       | [`xss-vulnerable`](./xss-vulnerable) | [`xss-secure`](./xss-secure) | Input sanitization with Bleach |
| Stored XSS          | [`xss-stored-vulnerable`](./xss-stored-vulnerable) | [`xss-stored-secure`](./xss-stored-secure) | Sanitization before DB storage |
| XSS (with DB)       | [`xss-vulnerable`](./xss-vulnerable) | [`xss-secure`](./xss-secure) | Escaping + validation on input/output |
| File Upload         | [`file-upload-vulnerable`](./file-upload-vulnerable) | [`file-upload-secure`](./file-upload-secure) | File type validation, size limits, safe storage |
| Authentication & Session Management flaws | `auth-vulnerable/` | `auth-secure/` | Demonstrates weak authentication (plain text passwords, no session handling) vs secure version with password hashing, session management, and logout. |

---

## 📌 Roadmap (Upcoming Projects)

* Authentication & Session Management flaws
* More OWASP Top 10 vulnerabilities

---

## 🚀 How to Use

1. Navigate into a project folder (e.g., `sql-injection-demo/`, `sql-injection-safe/`, `xss-vulnerable/`, `xss-secure/`).
2. Follow the setup instructions in that project’s README.
3. Experiment with the vulnerable app, then compare it with the secure version.

---

## 🎯 Purpose

* Document and showcase hands-on **application security projects**.
* Provide a structured learning path for understanding and preventing real-world vulnerabilities.

---

## ⚠️ Disclaimer

These projects are for **educational purposes only**.
Do not deploy vulnerable versions in production environments.
