from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, EmailField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Regexp, ValidationError


class LoginForm(FlaskForm):
    email = EmailField("Your email", validators=[DataRequired(), Length(1, 64)])
    password = PasswordField("Your password", validators=[DataRequired()])
    remember_me = BooleanField("Stay logged in")
    send = SubmitField("Log in")


class RegisterForm(FlaskForm):
    username = StringField("Your username", validators=[DataRequired(), Length(1, 64), Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, 'Your username should start with letters and only comprise letters underscores numbers or dots')])
    email = EmailField("Your work email", validators=[DataRequired(), Length(1, 64)])
    password = PasswordField("Your password", validators=[DataRequired(), Length(8, 16), EqualTo('password2', message='Your passwords should match')])
    password2 = PasswordField("Repeat password", validators=[DataRequired()])
    send = SubmitField("Register")