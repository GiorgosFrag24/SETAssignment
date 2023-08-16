from httpServer import app
from httpServerWithDelays import appWithDelays
import pytest


@pytest.fixture
def server():
    app.config['TESTING'] = True
    with app.test_client() as server:
        yield server


@pytest.fixture
def serverWithDelay():
    appWithDelays.config['TESTING'] = True
    with appWithDelays.test_client() as server:
        yield server
