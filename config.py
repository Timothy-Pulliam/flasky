import os

DEBUG = True
SECRET_KEY = 'a8251ffb76f32d3e97937a92ed554c72'
basedir = os.path.abspath(os.path.dirname(__file__))

# Database Settings
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
