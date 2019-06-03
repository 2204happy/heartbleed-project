from flask import *

app = Flask(__name__)
from datetime import *

#url_for('static', filename='style.css')

@app.route('/')
@app.route('/index.html')
def index():
  return render_template("index.html", thingo = "greeting")

@app.route('/protocols.html')
def protocols():
  return render_template("protocols.html", thingo = "greeting")

@app.route('/style.css')
def style():
  return render_template("style.css")
