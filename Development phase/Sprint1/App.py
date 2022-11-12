from flask import Flask,render_template, flash,redirect, url_for,request
app = Flask(__name__)
app.secret_key="hello"

@app.route("/")
def homepage():
	return render_template("homepage.html")
	
@app.route("/catalogue")                                      
def catalogue():
	return render_template("catalogue.html")


@app.route("/orderconfirmed")
def orderconfirmed():
   return render_template("orderconfirmed.html")

@app.route("/payment")
def payment():
   return render_template("payment.html")
 
@app.route("/registration_with_js_validation")
def registration_with_js_validation():
   return render_template("registration_with_js_validation.html")
 
@app.route("/registration")
def registration():
   return render_template("registration.html")
 
@app.route("/shoppingcart")
def shoppingcart():
   return render_template("shoppingcart.html")

