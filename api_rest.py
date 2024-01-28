from flask import Flask, render_template
import os

path = os.path.dirname(__file__)
app = Flask(__name__)

@app.route('/')
def hello():
    value = ["film1", "film2"]
    return render_template('index.html', films=value)

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)