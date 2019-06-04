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

#what the heartbeat protocol would return
output = ""
#very secret data no one should know that we totally won't expliot :)
secret_string = "a97b79,password_user_bob=\"password12345\",cookie_data_session_1=\"bannana\",123f7a757575a57c57meaning_of_life=42,"

@app.route("/demo.html")
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
    output = "Error: input must be an integer"
  
  #html stuff
  return render_template("demo.html",content = str(output))
 
