from flask import Flask
from flask_bootstrap import Bootstrap

from celery import Celery

from .config import Config

#mongodb = MongoEngine()
bootstrap = Bootstrap()
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)

from .cli import create_db, shell_context_processor
from .models import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    celery.conf.update(app.config)

    #app.cli.add_command(create_db)
    #create_db()
    app.cli.add_command(create_db)
    app.shell_context_processors.append(shell_context_processor)

    db.init_app(app)

    #db.create_all() #this might cause clearing all data at restart
    bootstrap.init_app(app)

    return app

app = create_app()

@app.cli.command()
def deploy():
    print("deploying fresh")
    db.create_all()