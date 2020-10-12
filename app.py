from flask import Flask, render_template,  session, redirect, request, jsonify
from flask_cors import CORS,cross_origin
from scraper import scrap_flipkart

app = Flask(__name__)

@app.route('/', methods=['GET'])
@cross_origin()
def homePage():
	return render_template("index.html")

@app.route('/scrap', methods=['GET'])
@cross_origin()
def scrap():
	search_text = request.args.get("query")
	result = scrap_flipkart(search_text)
	return jsonify(result)

if __name__ == '__main__':
	app.run()