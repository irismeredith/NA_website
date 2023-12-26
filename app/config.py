# This is a flask config file containing all the important configuration info for the website.
# There's nothing much to see here really.

# Author: Iris Meredith

# Last modified: 27/12/2023

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'test_key'
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    TEMPLATES_AUTO_RELOAD = True
    SEND_FILE_MAX_AGE_DEFAULT = 0
    ADMINS = [os.environ.get('SENDER')]
