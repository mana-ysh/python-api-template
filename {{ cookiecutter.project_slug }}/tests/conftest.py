
from typing import Generator

from fastapi import FastAPI
from fastapi.testclient import TestClient
import pytest

from {{ cookiecutter.project_slug }}.controller import create_app


@pytest.fixture
def app() -> Generator[FastAPI, None, None]:
    app = create_app()
    yield app


@pytest.fixture
def client(app: FastAPI) -> TestClient:
    """A test client for the app."""
    yield TestClient(app)
