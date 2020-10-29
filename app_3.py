from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>index</h1>'

@app.route('/about')
def about():
    return "this is about page"


@app.route('/hello/<string:name>')
def hello_name(name):
    return f"hello {name}"
