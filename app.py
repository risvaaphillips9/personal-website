from flask import Flask, render_template, request, url_for


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/resume")
def resume():
    return render_template("resume.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/thankyou")
def thankyou():
    name = request.args.get("name", "")
    email = request.args.get("email", "")
    message = request.args.get("message", "")
    return render_template("thankyou.html", name=name, email=email, message=message)


if __name__ == "__main__":
    # Enable debug for development; remove or set via env var in production
    app.run(debug=True)

