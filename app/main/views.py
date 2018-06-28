from app import app
from flask import render_template,flash,url_for,redirect
from .forms import RegistrationForm,LoginForm


app.config['SECRET_KEY'] = 'kabagemark'  

@app.route('/home')
def home():
    return render_template('home.html')

@app.route("/register" ,methods=['GET','POST'])
def Register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template('register.html', form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html' , form = form)    