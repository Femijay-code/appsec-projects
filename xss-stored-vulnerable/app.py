from flask import Flask, request, render_template_string

app = Flask(__name__)

# Insecure comments list (stored in memory)
comments = []

@app.route("/", methods=["GET", "POST"])
def home():
    global comments
    if request.method == "POST":
        comment = request.form.get("comment")
        comments.append(comment)  # 🚨 Vulnerable: stores raw input
    return render_template_string("""
        <h2>Stored XSS Demo (Vulnerable)</h2>
        <form method="POST">
            <input type="text" name="comment" placeholder="Enter a comment">
            <button type="submit">Post</button>
        </form>
        <h3>Comments:</h3>
        <ul>
            {% for c in comments %}
                <li>{{ c|safe }}</li>  <!-- 🚨 Rendered unsafely -->
            {% endfor %}
        </ul>
    """, comments=comments)

if __name__ == "__main__":
    app.run(debug=True)
