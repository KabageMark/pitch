from flask import render_template
from app import auth
from app import app
from flask import render_template,flash,url_for,redirect,request
from forms import RegistrationForm,LoginForm
from flask_login import login_required

# @auth.route('auth/login')
# def login():
#     return render_template('home.html')

# @auth.route("/auth/login", methods=['GET','POST'])
# @login_required
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         return redirect(url_for('main.home'))
#     return render_template('auth/login.html' , form = form)

# @auth.route("/auth/register" ,methods=['GET','POST'])
# def Register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}','success')
#         return redirect(url_for('main.home'))
#     return render_template('auth/register.html', form = form)   