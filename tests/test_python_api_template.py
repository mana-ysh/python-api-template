
import json

from python_api_template import __version__


def test_version():
    assert __version__ == '0.1.0'


def test_health(client):
    response = client.get("/health")
    assert "msg" in json.loads(response.data)
