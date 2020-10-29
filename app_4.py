from flask import Flask,render_template

app = Flask(__name__,template_folder='thems_4')

@app.route('/')
def index():
    return render_template('index.html')
    