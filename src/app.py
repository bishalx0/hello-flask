from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def welcome():
	return "Welcome to the flask app!"
	
	
@app.route("/hello-world")
def hello_world():
	return render_template("index.html")
	
	
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=4000)
