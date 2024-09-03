#!/usr/bin/python3
# app/__init__.py

#!/usr/bin/python3
# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from config import config

# Initialize extensions
db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()

def create_app(config_name='default'):
    """Factory function to create and configure the Flask application"""
    app = Flask(__name__)

    # Use the config dictionary to get the correct configuration
    app.config.from_object(config[config_name])

    # Initialize extensions with the app
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Import routes and register them
    from app.routes import init_routes  # Move this import to the top
    init_routes(app)  # Call the function to register routes

    return app

