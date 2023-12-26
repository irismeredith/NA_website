# This is a basic Flask app initiation: the only really interesting thing here is probably the use of whitenoise for serving static files

# Author: Iris Meredith

# Last modified: 27/12/2023

from flask import Flask
from flask_mail import Mail
from app import config
from whitenoise import WhiteNoise

import os

app = Flask(__name__)
app.config.from_object(config.Config)
app.wsgi_app = WhiteNoise(app.wsgi_app, root=os.path.join(os.path.dirname(__file__), 'static'))
mail = Mail(app)

from app import routes
