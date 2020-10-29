from flask import Flask,request

app = Flask(__name__)

# @app.route('/',methods=['GET','POST'])
# def index():
#     responce = 'request context \n'
#     responce += f"request method : {request.method}\n"
#     responce += f"request GET args : {request.form}\n"
#     return responce


@app.route('/',methods=['GET','POST'])
def index():
    name = request.args.get('name') or request.form.get('name')
    return f"hello {name}\n"



