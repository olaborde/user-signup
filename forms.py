from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
class signupForm(Form):
    user_name = StringField('user_name', validators=[DataRequired("Please enter a username")])
    password = PasswordField('password', validators=[DataRequired()])
    password2 = PasswordField('password2',validators=[DataRequired()])
    email = StringField('email')
    submit = SubmitField('signup')