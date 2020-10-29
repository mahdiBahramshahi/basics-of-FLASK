from flask import Flask , render_template

app = Flask(__name__,template_folder='tamrin')

@app.route('/')
def index():
    return render_template('tamrin.html')

