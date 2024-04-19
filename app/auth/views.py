from . import auth
from ..models import User
from flask_login import login_required, login_user, logout_user, current_user
from flask import flash, render_template, redirect, url_for
from .forms import LoginForm, RegisterForm
from app import db
from ..email import send_email

@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            flash('You are now logged in')
            return redirect(url_for('main.index'))
        flash('The information entered are invalid')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('main.index'))

@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        print("TOKEN %s", token)
        send_email("confirm registration", 'auth/mail/confirm', form.email.data, user=user, token=token)
        flash("An email was sent, click on the link to confirm your account")
        return redirect(url_for('main.index'))
    return render_template("auth/register.html", form=form)

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        db.session.commit()
        flash('You have confirmed')
    else:
        flash("The link was invalid or expired please try again")
    return redirect(url_for('main.index'))

