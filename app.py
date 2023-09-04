import requests

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        url = request.form.get("url")

        shrtcode = f"https://api.shrtco.de/v2/shorten?url={url}"

        response = requests.get(shrtcode)

        json = response.json()

        original_link = json["result"]["original_link"]
        short_link = json["result"]["short_link"]

        return render_template("index.html", active="home", result="true", original_link=original_link, short_link=short_link) 

    # User reached route via GET (as by clicking a link or via redirect)
    else: 
        return render_template("index.html", active="home")

@app.route("/faq")
def faq():
    return render_template("faq.html", active="faq")