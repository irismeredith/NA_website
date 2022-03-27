from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, email_validator


class ContactForm(FlaskForm):
    email = StringField('Contact Email',  validators=[Email(), DataRequired()])
    name = StringField('Your name', validators=[DataRequired()])
    message = TextAreaField('Your message', validators=[DataRequired()])
    submit = SubmitField('Send Message')
