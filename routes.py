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
  
@app.route("/buffer.html")
def buffer():
  return render_template("buffer.html", thingo = "greeting")
  
@app.route("/impacts.html")
def impacts():
  return render_template("impacts.html", thingo = "greeting")
  
@app.route("/method.html")
def method():
  return render_template("method.html", thingo = "greeting")

@app.route("/style.css")
def style():
  return render_template("style.css")

#what the heart beet protocol would return
output = ""
#very secret data no one should know that we totally won't expliot :)
secret_string = "a97b79,password_user_bob=\"password12345\",cookie_data_session_1=\"bannana\",123f7a757575a57c57meaning_of_life=42,"

@app.route("/demonstration")
def demo():
  global output
  #if the request field is empty leave it is blank otherwise popualte it
  if request.args.get("request") == None:
    message = ""
  else:
    message = str(request.args.get("request"))
  
  #the try will catch errors where the length is not an integer leteral
  try:
    #if the length is not popualted set it to 0 othereise make it the integer of the input 
    if request.args.get("length") == None:
      length = 0
    else:
      length = int(request.args.get("length"))
   
    #if the length is less than the actuall length return that amount of the message
    if length <= len(message):
      output = message[0:length]
    
    #if the request length is longer the the length of the message make up the diference from the scret string
    else:
      output = message
      length -= len(message)
      output += secret_string[0:length]
      
      #if the requested length is even longer than message and the secret string then make up the diference from the bee movie script
      if length > len(secret_string):
        length -= len(secret_string)
        with open("bee_movie_script", 'r') as bee_movie_file:
      	  output += bee_movie_file.read(length)
  except ValueError:
    output = "Error: length of data must be an integer"
  
  #html stuff
  return "<style> body { font-family: \"Comic Sans MS\", cursive, sans-serif; }</style><body>\n<p><a href=\"/\">Back</a><br>\n  Input: <br>\n <form method=\"get\">\n Data: <input type=\"text\" name=\"request\"> <br>\n Length of data: <input type=\"text\" name=\"length\"> <br>\n <input type=\"submit\" value=\"Send heartbeet\">\n </form>\n Output: <br>" + str(output) + "</p></body>"
 
