````markdown
# Command Injection Demo (Vulnerable)

This project demonstrates a **Command Injection vulnerability** in a simple Flask app.  
The application allows users to "ping" a host, but fails to properly sanitize user input, making it possible to inject system commands.

---

## 🚨 Vulnerability Overview
- **Issue:** Unsanitized user input is passed directly to the system shell.  
- **Impact:** An attacker can execute arbitrary commands on the host machine.  
- **Example Attack:**  
  - Input: `127.0.0.1; ls`  
  - Effect: Executes `ping 127.0.0.1` *and* lists files in the server directory.  

---

## ▶️ How to Run (Vulnerable App)
1. Install dependencies:
   ```bash
   pip install flask
````

2. Run the app:

   ```bash
   python3 app.py
   ```
3. Open in browser:

   ```
   http://127.0.0.1:5000/
   ```
4. Try the exploit:

   * Input: `127.0.0.1; ls`
   * You should see the ping output followed by the directory listing.

---

## 🎯 Learning Objective

* Understand how improper input handling can allow **command injection**.
* Learn to recognize patterns where shell commands are executed insecurely.

````

