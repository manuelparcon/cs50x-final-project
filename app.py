from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", active="home")

@app.route("/faq")
def faq():
    return render_template("faq.html", active="faq")