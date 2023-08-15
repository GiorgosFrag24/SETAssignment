import pytest
import logging


def test_GetPlanetsHappyPath(client):
    response = client.get('/planets/1/')
    logging.info(response)
    assert response.status_code == 200

