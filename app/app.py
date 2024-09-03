#!/usr/bin/python3

# app.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create an instance of SQLAlchemy
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # Configure your database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize SQLAlchemy with the Flask app
    db.init_app(app)

    # Import the routes and register them
    from app.routes import init_routes
    init_routes(app)  # Call the function here, after importing

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
# In app.py


