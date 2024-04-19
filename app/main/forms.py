from flask_wtf import FlaskForm
from wtforms import EmailField, SubmitField
from wtforms.validators import DataRequired, Length

class MailForm(FlaskForm):
    email=EmailField("Your mail", validators=[DataRequired(), Length(1, 64)])
    submit = SubmitField("send")