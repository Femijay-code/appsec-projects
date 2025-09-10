from flask import Flask, request, render_template_string
import subprocess
import shlex

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h2>Ping a Host (Secure)</h2>
        <form action="/ping" method="GET">
            <input type="text" name="host" placeholder="Enter hostname or IP">
            <input type="submit" value="Ping">
        </form>
    '''

@app.route('/ping')
def ping():
    host = request.args.get("host", "")
    try:
        # ✅ Secure: sanitize input using shlex.quote, no direct string concatenation
        safe_host = shlex.quote(host)
        result = subprocess.run(["ping", "-c", "2", safe_host],
                                capture_output=True, text=True, check=True)
        output = result.stdout
    except Exception as e:
        output = f"Error: {str(e)}"
    return render_template_string("<pre>{{output}}</pre>", output=output)

if __name__ == "__main__":
    app.run(debug=True)
