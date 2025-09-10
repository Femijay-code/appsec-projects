# Command Injection Demo (Secure)

This project is the **secure version** of the vulnerable command injection demo.  
It demonstrates how to prevent command injection by sanitizing user input before execution.

---

## ✅ Fix Implemented
- **Sanitization with `shlex.quote`:** User input is properly escaped before being passed to the shell.  
- **Effect:** Prevents attackers from injecting additional commands.  
- Example:
  - Input: `127.0.0.1; ls`  
  - Actual execution: Only `ping '127.0.0.1; ls'` → treated as a single argument, not multiple commands.  

---

## ▶️ How to Run (Secure App)
1. Install dependencies:
   ```bash
   pip install flask
  


## ▶️ How to Run (Secure App)
1. Install dependencies:
   ```bash
   pip install flask

2. Run the app:

   ```bash
   python3 app.py
   
3. Open in browser:

   ```
   http://127.0.0.1:5000/
  
4. Test the same payload:

   * Input: `127.0.0.1; ls`
   * Output: Only a ping to `"127.0.0.1; ls"`, **no command injection occurs**.

---

## 🎯 Learning Objective

* See how proper sanitization blocks command injection attacks.
* Understand the importance of never directly passing raw user input into shell commands.

