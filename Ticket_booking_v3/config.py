import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'une_cle_secrete_a_changer'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'reservations.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LANGUAGES = ['fr', 'en']
    BABEL_DEFAULT_LOCALE = 'fr'
