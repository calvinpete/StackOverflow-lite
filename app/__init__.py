from instance.config import DevelopmentConfig
from flask import Flask
from app.views import main_blueprint


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(main_blueprint)
    return app
