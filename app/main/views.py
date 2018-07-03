from app import app
from flask import render_template,flash,url_for,redirect,request
from .forms import RegistrationForm,LoginForm,pitchForm
# from app import db


app.config['SECRET_KEY'] = 'kabagemark'  

@app.route('/pitch')
def pitch():
    return render_template('pitch.html')
    pitchstored = pitch.query.filter_by
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = pitchForm()
    if form.validate_on_submit():    
        pitch = form.pitch.data
        category = form.category.data
        print(pitch)
        print(category)
        flash(f'The pitch {form.pitch.data} under {form.category.data} category has been created',)
        return render_template('home.html',pitch=pitch, category=category,form = form)  
        # return redirect(url_for('home'))

    return render_template('home.html', form = form,)  

@app.route("/register" ,methods=['GET','POST'])
def Register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template('register.html', form = form)

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('login.html' , form = form)

  