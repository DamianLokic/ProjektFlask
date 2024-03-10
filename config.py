import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'bardzo-tajny-klucz'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
