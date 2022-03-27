from os import environ
from urllib.parse import urlparse
import smtplib
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# read and parse MailerToGo env vars

mailertogo = urlparse(environ.get('MAILERTOGO_URL'))
mailertogo_domain = environ.get('MAILERTOGO_DOMAIN', 'instruments-of-mayhem.co.nz')

# sender
sender_user = 'noreply'
sender_email = "@".join([sender_user, mailertogo_domain])
sender_name = 'Example'

# recipient
recipient_email = sender_email # change to recipient email. Make sure to use a real email address in your tests to avoid hard bounces and protect your reputation as a sender.
recipient_name = 'Ms. Example'

# subject
subject = 'Mailer To Go Test'

# text body
body_plain = ("Hi,\n"
    "Test from Mailer To Go\n"
    )


# create message container
message = MIMEMultipart('alternative')
message['Subject'] = subject
message['From'] = email.utils.formataddr((sender_name, sender_email))
message['To'] = email.utils.formataddr((recipient_name, recipient_email))

# prepare plain and html message parts
part1 = MIMEText(body_plain, 'plain')

# attach parts to message

message.attach(part1)

# send the message.
try:
    server = smtplib.SMTP(mailertogo.hostname, mailertogo.port)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(mailertogo.username, mailertogo.password)
    server.sendmail(sender_email, recipient_email, message.as_string())
    server.close()
except Exception as e:
    print ("Error: ", e)
else:
    print ("Email sent!")
