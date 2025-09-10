from flask import Flask, request, render_template_string
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "txt", "pdf"}
MAX_FILE_SIZE = 2 * 1024 * 1024  # 2 MB limit

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files.get("file")
        if file and allowed_file(file.filename):
            # Secure the filename
            filename = secure_filename(file.filename)

            # Check file size
            file.seek(0, os.SEEK_END)
            size = file.tell()
            file.seek(0)

            if size > MAX_FILE_SIZE:
                return "❌ File too large! (Max 2MB)"

            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            return f"✅ File uploaded successfully: {filepath}"
        else:
            return "❌ Invalid file type! Only images, txt, pdf allowed."

    return """
        <h2>Secure File Upload Demo</h2>
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    """

if __name__ == "__main__":
    app.run(debug=True)
