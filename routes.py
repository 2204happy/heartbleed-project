from flask import *

app = Flask(__name__)
from datetime import *

#url_for('static', filename='style.css')

@app.route("/")
@app.route("/index.html")
def index():
  return render_template("index.html", thingo = "greeting")

@app.route("/protocols.html")
def protocols():
  return render_template("protocols.html", thingo = "greeting")

@app.route("/style.css")
def style():
  return render_template("style.css")

output = ""
secret_string = "a97b79,password_user_bob=\"password12345\",cockie_data_session_1=\"bannana\",123f7a757575a57c57meaning_of_life=42,"

@app.route("/demonstration")
def demo():
  global output
  
  if request.args.get("request") == None:
    message = ""
  else:
    message = str(request.args.get("request"))
  try:
    if request.args.get("length") == None:
      length = 0
    else:
      length = int(request.args.get("length"))
   
    if length <= len(message):
      output = message[0:length]
    else:
      output = message
      length -= len(message)
      output += secret_string[0:length]
      if length > len(secret_string):
        length -= len(secret_string)
        with open("bee_movie_script", 'r') as bee_movie_file:
      	  output += bee_movie_file.read(length)
  except ValueError:
    output = "Error: input must be an integer"
  
  return "<link rel=\"stylesheet\" type=\"text/css\" href=\"styles/demonstration.css\"> Input: <br> <form method=\"get\"> Request: <input type=\"text\" name=\"request\"> <br> Length of request: <input type=\"text\" name=\"length\"> <br> <input type=\"submit\"> </form> Output: <br>" + str(output)
