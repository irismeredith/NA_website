from flask import render_template, redirect, send_from_directory
from flask_mail import Message
from app import mail
from app import app
from app.forms import ContactForm


@app.route('/')
@app.route('/index')
def index():
    return redirect('/index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()

    if form.validate_on_submit():

        confirmation_message = Message('Noether Analytics: Message Received', sender=app.config['ADMINS'][0],
                                       recipients=[form.email.data])

        confirmation_message.body = 'Hello ' + form.name.data + ',\n\n Thank you for your message. We have received it ' \
                                                                'and will be in touch shortly.\n\n Sincerely,\n\n ' \
                                                                'Noether Analytics'

        mail.send(confirmation_message)

        forwarded_message = Message('Contact Form submission: ' + form.name.data, sender=app.config['ADMINS'][0],
                                    recipients=['irishenceaway@gmail.com'])

        forwarded_message.body = 'Sender email: ' + form.email.data + '\n' + form.message.data
        mail.send(forwarded_message)

        # Emit some Javascript here to change the DOM and add a redirect link: I feel like that's probably more elegant
        # than loading another page

        return redirect('/index.html')

    return render_template('contact_form.html', title='Contact Us', form=form)
