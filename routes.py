from . import app
from flask import request, render_template

from datetime import *

@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html", thingo = "greeting")
