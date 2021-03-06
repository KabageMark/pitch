from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField , SubmitField,BooleanField
from wtforms.validators import DataRequired , Length , Email , EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])

    email = StringField('Email',validators=[DataRequired(),Email()])
    
    password = PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])

    submit = SubmitField('sign-up')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    
    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember me')

    submit = SubmitField('Login')

class pitchForm(FlaskForm):
    pitch = StringField('Pitch',validators=[DataRequired()])

    category = StringField('Category',validators=[DataRequired()])

    comments = StringField('Comments')

    submit = SubmitField('submit') 