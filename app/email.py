from threading import Thread
from . import mail
from flask_mail import Message
from flask import render_template, current_app



def send_async_mail(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(subject, template, to, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['APP_MAIL_SUBJECT_PREFIX']+subject, recipients=[to], sender = app.config['APP_MAIL_SENDER'])
    msg.body = render_template(template+".txt", **kwargs)
    msg.html = render_template(template+".html", **kwargs)
    thr = Thread(target=send_async_mail, args=[app, msg])
    thr.start()
    return thr
