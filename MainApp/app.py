from flask import Flask, json, render_template, jsonify
import requests 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)