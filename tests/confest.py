#!/usr/bin/python3

import pytest
from app import create_app
from config import TestingConfig

@pytest.fixture
def app():
    app = create_app(TestingConfig)
    yield app

