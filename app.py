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

from flask import Flask, render_template, request, url_for


app = Flask(__name__)


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
    """Render the projects page."""
    return render_template("projects.html")


@app.route("/contact")
def contact():
    """Render the contact page with a simple client-side validated form.

    The form uses method=GET and submits to `/thankyou` to keep the
    implementation simple and avoid backend storage.
    """
    return render_template("contact.html")


@app.route("/thankyou")
def thankyou():
    """Render a simple confirmation page for contact form submissions.

    Expects optional query params: `name`, `email`, and `message`.
    """
    name = request.args.get("name", "")
    email = request.args.get("email", "")
    message = request.args.get("message", "")
    return render_template("thankyou.html", name=name, email=email, message=message)


if __name__ == "__main__":
    # Enable debug for local development. Use an environment variable or
    # a config file for production settings, and avoid debug mode there.
    app.run(debug=True)
