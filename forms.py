from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, Length
class signupForm(Form):
    user_name = StringField('user_name', validators=[DataRequired("Please enter a username")])
    password = PasswordField('password', validators=[DataRequired(), Length(min=3, message="password should be between 3 and 20 characteres"), validators.EqualTo('vpassword', message='password mnust match')])
    vpassword = PasswordField('vpassword',validators=[DataRequired(), Length(min=3, message="password should be between 3 and 20 characteres")])
    email = StringField('email')
    submit = SubmitField('signup')

