
from typing import Generator

from flask import Flask
from flask.testing import FlaskClient
import pytest

from {{ cookiecutter.project_slug }}.controller import create_app


@pytest.fixture
def app() -> Generator[Flask, None, None]:
    app = create_app()
    app.config['TESTING'] = True
    yield app


@pytest.fixture
def client(app: Flask) -> FlaskClient:
    """A test client for the app."""
    return app.test_client()
