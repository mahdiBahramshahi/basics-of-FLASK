import random
from flask import Flask , render_template

app = Flask(__name__,template_folder='thems_5')

@app.route('/')
def index():
    return render_template("index_2.html")

@app.route('/result/')
def result():
    heads_or_tails = random.randint(1,2)
    if heads_or_tails == 1 :
        result_text = "heads"
    else:
        result_text = "tails"
    return render_template('result.html',result_text=result_text)




