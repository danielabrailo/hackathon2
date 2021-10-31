from flask import render_template, url_for, flash, redirect
from HACKATON_2 import app
import requests
from HACKATON_2.forms import RegistrationForm, LoginForm
from HACKATON_2.models import User

response = requests.get('http://universities.hipolabs.com/search').json()
countries = []


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/search/<name>')
def search(name):
    return render_template('details.html', info=response, name=name)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Nice to meet you {form.username.data}!", 'info')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@noa.com' and form.password.data == 'password':
            flash(f"Your'e in!", 'info')
            return redirect(url_for('home'))
        else:
            flash(f"Log in was unsuccessful", 'danger')
            return redirect(url_for('login'))
    return render_template('login.html', form=form)
