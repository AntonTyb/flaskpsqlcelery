import os


class Config(object):
    SECRET_KEY = os.environ.get("FLASK_SECRET_KEY") or "supersekrit"
    SSL_REDIRECT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI") or "sqlite:///app.sqlite3"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL =  os.environ.get("REDIS_URL")
    CELERY_RESULT_BACKEND = os.environ.get("REDIS_URL")