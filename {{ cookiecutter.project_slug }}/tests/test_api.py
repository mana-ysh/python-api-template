
from {{ cookiecutter.project_slug }} import __version__


def test_version():
    assert __version__ == "0.1.0"


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"msg": "I'm healthy"}
