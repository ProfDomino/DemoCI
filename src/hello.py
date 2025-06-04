import os
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'demo-key'  # Needed for session storage

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/", methods=["GET", "POST"])
def toggle_button():
    # Initialize toggle state
    if "toggle_state" not in session:
        session["toggle_state"] = "OFF"

    # Handle button press
    if request.method == "POST":
        if session["toggle_state"] == "OFF":
            session["toggle_state"] = "ON"  
        else:
            session["toggle_state"] = "OFF"
        return redirect(url_for("toggle_button"))

    return render_template("toggle_button.html", state=session["toggle_state"])
