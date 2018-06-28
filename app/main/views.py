from app import app
from flask import render_template
from .forms import RegistrationForm,LoginForm


app.config['SECRET_KEY'] = 'kabagemark'  

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route("/register")
def Register():
    form = RegistrationForm()
    return render_template('register.html', form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html' , form = form)    