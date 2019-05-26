from . import *
from flask import *

from datetime import *

#url_for('static', filename='style.css')

@app.route('/')
@app.route('/index.html')
def index():
    return render_template("index.html", thingo = "greeting")
