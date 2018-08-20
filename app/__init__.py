from instance.config import DevelopmentConfig
from flask import Flask


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    return app
