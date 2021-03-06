from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, length, equal_to, Email


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                           validators=[DataRequired(), length(min=2, max=20)])
    confirm_password = PasswordField('Confirm Password',
                           validators=[DataRequired(), length(min=2, max=20), equal_to('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired()])
    password = PasswordField('Password',
                            validators=[DataRequired(), length(min=2, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')
