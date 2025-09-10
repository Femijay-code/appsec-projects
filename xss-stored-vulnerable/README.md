````markdown
# Stored XSS Demo (Vulnerable)

## Overview
This Flask app demonstrates a **stored cross-site scripting (XSS)** vulnerability.  
User input is stored and rendered without sanitization, allowing malicious scripts to persist.

## Steps to Reproduce
1. Run the app:
   ```bash
   python3 app.py
````

2. Open `http://127.0.0.1:5000`
3. Submit a comment with payload:

   ```html
   <script>alert("Hacked!")</script>
   ```
4. The payload executes every time the page loads.

## Screenshot

*Add screenshot of the alert popup here.*

## Impact

Attackers can steal cookies, deface pages, or run arbitrary JavaScript.

````
