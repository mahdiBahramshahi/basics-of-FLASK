from flask_wtf import FlaskForm
from wtforms import TextField,PasswordField
from wtforms.validators import data_required


class loginform(FlaskForm):
    username=TextField(validators=[data_required()])
    password = PasswordField(validators=[data_required()])






