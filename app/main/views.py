from app import app
from flask import render_template,flash,url_for,redirect,request
from .forms import RegistrationForm,LoginForm,pitchForm
from flask_login import login_required

# from app import db


app.config['SECRET_KEY'] = 'kabagemark'  

@app.route("/home",methods=['GET','POST'])
def home():
    form = pitchForm()    
    pitch = form.pitch.data
    category = form.category.data
    comments = form.comments.data
    print(pitch)
    print(category)
    print(comments) 
    return render_template('home.html',pitch=pitch, category=category,comments=comments,form = form)
    # pitchstored = pitch.query.filter_by

@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('login.html' , form = form)

@app.route("/register" ,methods=['GET','POST'])
def Register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template('register.html', form = form)

    
# @app.route("/home", methods=['GET', 'POST'])
# def home():
#     form = pitchForm()
#     if form.validate_on_submit():    
#         pitch = form.pitch.data
#         category = form.category.data
#         comments = form.comments.data
#         print(pitch)
#         print(category)
#         print(comments)  
#         flash(f'The pitch {pitch} under {category} category has been created',)
#         # return redirect(url_for('home'))
#         return render_template('home.html',pitch=pitch,comments=comments, category=category,form = form)  
  





  