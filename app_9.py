from flask import Flask , render_template , request
from forms_9 import loginform

app = Flask(__name__,template_folder='thems_9')
app.config['SECRET_KEY'] = 'kxdjvzdkfhb'


@app.route('/')
def index():
    login_form = loginform()
    return render_template('index_5.html',login_form=login_form)


@app.route('/login' ,methods=['POST'])
def login():
    login_form =loginform(request.form)
    if not login_form.validate_on_submit():
        return "ERROR!"
    return '<h1>ok</h1>'

