from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder="templates", static_folder="templates/static")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/contact")
def connect():
    return render_template("contact.html")


if __name__ == "__main__":
    app.config["ENV"] = "development"
    app.config["DEBUG"] = True
    app.run()
