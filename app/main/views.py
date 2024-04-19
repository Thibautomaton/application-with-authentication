from . import main
from .forms import MailForm
from ..models import User
from flask import session, flash, render_template, redirect, url_for
from app import db
from ..email import send_email
from flask_login import login_required


@main.route("/", methods=["GET", "POST"])
def index():
    form = MailForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            user = User(email=form.email.data)
            db.session.add(user)
            db.session.commit()
            session["known"] = False
        else:
            session["known"] = True
            flash("user already in database")
            flash("well done")
            # send_email("registration attempt", "index", form.email.data, form=form, known=session.get("known"))

        redirect(url_for('.index'))
    return render_template("index.html", form=form, known=session.get("known"))


@main.route('/secret')
@login_required
def secret():
    return render_template("secret.html")
