````markdown
# Stored XSS Demo (Secure)

## Overview
This version mitigates stored XSS by sanitizing user input with the `bleach` library before storage.

## Steps
1. Run the app:
   ```bash
   python3 app.py
````

2. Submit the same payload:

   ```html
   <script>alert("Hacked!")</script>
   ```
3. The script is displayed as plain text instead of executing.

## Screenshot

*Add screenshot of sanitized output here.*

## Security Fix

* Input sanitization (`bleach.clean()`)
* No use of `|safe` filter when rendering

````
