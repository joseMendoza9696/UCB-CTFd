from flask import Blueprint, render_template, request

training = Blueprint("training", __name__)

@training.route("/training")
def listing():
    return render_template("training.html")