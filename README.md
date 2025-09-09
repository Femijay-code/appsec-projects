# Application Security Projects

This repository is a growing collection of hands-on **application security projects**.
Each project demonstrates common security vulnerabilities and their secure implementations, helping to bridge the gap between theory and practice.

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

### 3. XSS Demo (Vulnerable)

* **Folder:** `xss-vulnerable/`
* A web application that does **not sanitize user input**, allowing stored/reflected XSS attacks.
* Goal: Understand how attackers inject malicious scripts into web pages.

### 4. XSS Demo (Secure)

* **Folder:** `xss-secure/`
* A secure version of the XSS demo that uses **input sanitization (Bleach library)** to prevent execution of malicious scripts.
* Demonstrates how to protect against XSS vulnerabilities.

---

## 📌 Roadmap (Upcoming Projects)

* Command Injection
* Insecure File Uploads
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
* Serve as a professional portfolio for practical security skills.

---

## ⚠️ Disclaimer

These projects are for **educational purposes only**.
Do not deploy vulnerable versions in production environments.

---

👉 Would you like me to also write **separate README files** for `xss-vulnerable/` and `xss-secure/` (just like your SQLi folders have), or keep everything only in the main README for now?
