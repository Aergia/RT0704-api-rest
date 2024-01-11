from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Videotheque</h1>'

@app.route('/register')
def register():
    return 'register'

@app.route('/login')
def login():
    return 'login'
