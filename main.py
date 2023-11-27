from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/index')
def index():
<<<<<<< HEAD
    return 'main page'
=======
    return 'mainpage'

@app.route('/')
def mainpage():
    return 'Main page'
>>>>>>> newpage
