#!/usr/bin/python3
# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_name='default'):
    """Factory function to create and configure the Flask application"""
    app = Flask(__name__)

    # Use the config dictionary to get the correct configuration
    app.config.from_object(config[config_name])

    db.init_app(app)

    return app

