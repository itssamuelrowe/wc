from flask import Flask, render_template,  session, redirect, request
from flask_cors import CORS,cross_origin

app = Flask(__name__)

@app.route('/',methods=['GET'])  
@cross_origin()
def homePage():
	return render_template("index.html")

if __name__ == '__main__':
	app.run()