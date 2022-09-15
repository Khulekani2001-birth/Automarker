from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("main.html", title="Home")
