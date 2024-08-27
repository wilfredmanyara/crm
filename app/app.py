#!/usr/bin/python3

from flask import Flask
from config import DevelopmentConfig, TestingConfig, ProductionConfig

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)
    # Initialize other extensions or blueprints here
    return app

