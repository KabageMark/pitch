from app import app
from flask import render_template,flash,url_for,redirect,request
from .forms import RegistrationForm,LoginForm,pitchForm


app.config['SECRET_KEY'] = 'kabagemark'  

# @app.route('/home')
# def home():
#     return render_template('home.html')
@app.route("/home", methods=['GET', 'POST'])
def home():
    form = pitchForm()
    name=request.form
    if form.validate_on_submit():
        print (name)
        if form.validate():
            # Save the comment here.
            flash("cannot post empty quote")
        else:
            flash('All the form fields are required. ')
 
    return render_template('home.html', form = form, name = name)  

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

  