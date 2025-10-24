"""Flask application for the personal website.

This app renders pages via Jinja templates (in the `templates/` folder)
and serves assets from `static/` (css, js, images, docs).

Routes:
    /           Home page
    /about      About page
    /resume     Resume page
    /projects   Projects page
    /contact    Contact form page (GET)
    /thankyou   Simple confirmation page that echoes query params
"""

from flask import Flask, render_template, request, url_for, redirect, flash
from werkzeug.utils import secure_filename
import os
import DAL


app = Flask(__name__)
app.secret_key = "dev-secret-key"  # for flashing simple validation messages

# Ensure database and table exist on startup, then guarantee baseline projects
DAL.init_db()
DAL.ensure_baseline_projects()

# Upload config for project images
ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}
app.config["UPLOAD_FOLDER"] = os.path.join(app.root_path, "static", "images")
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024  # 10 MB limit


def allowed_file(filename: str) -> bool:
    has_dot = "." in filename
    ext = filename.rsplit(".", 1)[1].lower() if has_dot else ""
    return has_dot and ext in ALLOWED_EXTENSIONS


def ensure_unique_path(directory: str, filename: str) -> str:
    """Ensure a unique filename by adding a numeric suffix if needed."""
    name, ext = os.path.splitext(filename)
    candidate = filename
    counter = 1
    while os.path.exists(os.path.join(directory, candidate)):
        candidate = f"{name}_{counter}{ext}"
        counter += 1
    return candidate


@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")


@app.route("/about")
def about():
    """Render the about page."""
    return render_template("about.html")


@app.route("/resume")
def resume():
    """Render the resume page (with inline page-specific styles)."""
    return render_template("resume.html")


@app.route("/projects")
def projects():
    """Render the projects page from database entries."""
    items = DAL.get_all_projects()
    return render_template("projects.html", projects=items)


@app.route("/contact")
def contact():
    """Render the original contact page that submits to /thankyou via GET."""
    return render_template("contact.html")


@app.route("/add-project", methods=["GET", "POST"])
def add_project():
    """Add Project form to insert new projects (supports image upload)."""
    if request.method == "POST":
        title = (request.form.get("title") or "").strip()
        description = (request.form.get("description") or "").strip()
        file = request.files.get("image_file")

        if not title or not description:
            flash("Title and Description are required.")
            return render_template("add_project.html"), 400

        if not file or not file.filename:
            flash("Please upload an image file.")
            return render_template("add_project.html"), 400

        raw_name = secure_filename(file.filename)
        if not raw_name or not allowed_file(raw_name):
            flash("Please upload an image file (png, jpg, jpeg, gif, webp).")
            return render_template("add_project.html"), 400

        os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
        unique_name = ensure_unique_path(app.config["UPLOAD_FOLDER"], raw_name)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], unique_name))

        # Insert project and redirect to projects page
        DAL.insert_project(title, description, unique_name)
        return redirect(url_for("projects"))

    return render_template("add_project.html")


@app.route("/thankyou")
def thankyou():
    """Render a simple confirmation page for contact form submissions.

    Expects optional query params: `name`, `email`, and `message`.
    """
    name = request.args.get("name", "")
    email = request.args.get("email", "")
    message = request.args.get("message", "")
    return render_template(
        "thankyou.html",
        name=name,
        email=email,
        message=message,
    )


if __name__ == "__main__":
    # Enable debug for local development. Use an environment variable or
    # a config file for production settings, and avoid debug mode there.
    app.run(debug=True)
