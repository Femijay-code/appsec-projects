from flask import Flask, request, render_template_string
import bleach

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        user_input = request.form.get("user_input")
        sanitized_input = bleach.clean(user_input)
        return render_template_string(f"<h1>Your input: {sanitized_input}</h1>")
    return '''
        <form method="POST">
            <input name="user_input" placeholder="Enter text">
            <button type="submit">Submit</button>
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True)
