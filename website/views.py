
# Flask Imports
from flask import Blueprint, render_template, request, flash, jsonify, url_for, redirect


# Views Blueprint
views = Blueprint('views', __name__)



# Home Route
@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")




