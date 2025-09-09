# XSS Vulnerable Demo

## 📌 Overview
This is a deliberately vulnerable Flask application that demonstrates how **Reflected Cross-Site Scripting (XSS)** attacks work.

The app directly renders user input into the page without sanitization, allowing attackers to inject JavaScript.

---

## ⚙️ How to Run
```bash
cd xss-vulnerable
python3 app.py
````

App runs on: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🚨 Attack Demo

Example payload:

```html
<script>alert("XSS Attack!")</script>
```

➡️ This will trigger a JavaScript pop-up, proving the site is vulnerable.

---

## 🎯 Key Takeaway

Always sanitize and escape user input before rendering to prevent XSS.

````

When done, press:  
`CTRL + O` → Enter → `CTRL + X`  

---

### ✅ Step 2: Create README for **xss-secure**
Type:  
```bash
nano ~/appsec-projects/xss-secure/README.md
````

Paste this content:

````markdown
# XSS Secure Demo

## 📌 Overview
This is the secured version of the XSS demo. It uses the **Bleach** library to sanitize user input before rendering it into the page.

This prevents execution of malicious JavaScript.

---

## ⚙️ How to Run
```bash
cd xss-secure
python3 app.py
````

App runs on: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## ✅ Security Demo

Example payload:

```html
<script>alert("XSS Attack!")</script>
```

➡️ Instead of executing, it will render harmlessly as text on the page.

---

## 🎯 Key Takeaway

Input sanitization (e.g., using Bleach) is an effective way to defend against XSS.

````

