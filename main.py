from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('mainpage.html')

@app.route('/about')
def about():
    return render_template('about.html')