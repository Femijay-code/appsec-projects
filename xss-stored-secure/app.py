from flask import Flask, request, render_template_string
import bleach

app = Flask(__name__)

# Secure comments list (stored in memory)
comments = []

@app.route("/", methods=["GET", "POST"])
def home():
    global comments
    if request.method == "POST":
        comment = request.form.get("comment")
        # ✅ Sanitize input
        safe_comment = bleach.clean(comment)
        comments.append(safe_comment)
    return render_template_string("""
        <h2>Stored XSS Demo (Secure)</h2>
        <form method="POST">
            <input type="text" name="comment" placeholder="Enter a comment">
            <button type="submit">Post</button>
        </form>
        <h3>Comments:</h3>
        <ul>
            {% for c in comments %}
                <li>{{ c }}</li>  <!-- Safe rendering -->
            {% endfor %}
        </ul>
    """, comments=comments)

if __name__ == "__main__":
    app.run(debug=True)
