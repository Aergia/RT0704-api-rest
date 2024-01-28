from flask import Flask, render_template, request
import os
import requests

path = os.path.dirname(__file__)
app = Flask(__name__)

@app.route('/')
def hello():
    value = ["film1", "film2"]
    return render_template('index.html', films=value)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/add', methods=['POST'])
def add():
    print("mpm")

@app.route('/print', methods=['POST'])
def print():
    name = str(request.get_data())[7:]
    films = str(name[:int(len(name)-1)])

    return render_template('index.html', films=films)

if __name__ == '__main__':
    app.run(debug=True, port=8000)