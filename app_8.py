from flask import Flask , render_template,request

app = Flask(__name__,template_folder='thems_8')

auth={'username' : 'mahdi',
      'password' : '1234567890'}



@app.route('/',methods=['GET','POST'])
def index():
    print(request.form)
    return render_template('index_4.html')



@app.route('/login/',methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    if not password:
        return 'Error!'
        
    if username.lower() == auth['username'] and password == auth['password']:
        return f"Welcome dear {username}"
    return 'Incorrect username/password.'




