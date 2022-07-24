from flask import Blueprint, render_template
from app.models import Product, User

blueprint = Blueprint("main", __name__)

@blueprint.route("/")
def index():
    return render_template("home.j2")

@blueprint.route("/get/<object>")
def get_object(object):
    return render_template("object.j2")


