from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h2>Ping a Host (Vulnerable)</h2>
        <form action="/ping" method="GET">
            <input type="text" name="host" placeholder="Enter hostname or IP">
            <input type="submit" value="Ping">
        </form>
    '''

@app.route('/ping')
def ping():
    host = request.args.get("host", "")
    # 🚨 Vulnerability: directly passing user input to system command
    result = os.popen(f"ping -c 2 {host}").read()
    return render_template_string("<pre>{{result}}</pre>", result=result)

if __name__ == "__main__":
    app.run(debug=True)
