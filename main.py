from flask import Flask, render_template, url_for, request, redirect

from flask_mail import Mail, Message

app = Flask(__name__, template_folder="templates", static_folder="templates/static")

# FLASK MAIL - https://www.youtube.com/watch?v=1oOefRD8jek
mail = Mail(app)
#




@app.route("/")
def main():
    return render_template("index.html")

@app.route("/contact")
def connect():
    return render_template("contact.html")

@app.route("/contact_test")
def contact_test():
    return render_template("contact_test.html")


### FOR TEST
@app.route("/login_test", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        login_name = request.form["login_name"]
        return redirect(url_for("logged_in", login=login_name))
    else:
        return render_template("login.html")


@app.route("/<login>_test")
def logged_in(login):
    return f"<html><p>Hello my friend</p><br><h2>{login}</h2></html>"

### FOR TEST


if __name__ == "__main__":
    app.config["ENV"] = "development"
    app.config["DEBUG"] = True
    app.run()
