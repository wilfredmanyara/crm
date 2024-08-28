#!/usr/bin/python3

import sys
print(sys.path)
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config, DevelopmentConfig, TestingConfig, ProductionConfig
from flask_testing import TestCase  # Import TestCase from flask_testing
from app import create_app, db  # Import create_app and db from your app module

class TestConfig(TestCase):
    def create_app(self):
        """Create the Flask app with testing configuration."""
        return create_app('testing')

    def setUp(self):
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_base_config(self):
        self.assertTrue(self.app.config['TESTING'])
        self.assertIsNotNone(self.app.config['SQLALCHEMY_DATABASE_URI'])

