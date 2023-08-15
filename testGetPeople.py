import pytest
import requests
import logging


def testGetPeopleHappyPath(client):
    logging.info('Fetching the person with id:1')
    response = client.get('/people/1/')
    logging.info('Calling GET /people/1/')
    assert response.status_code == 200
    logging.info('Successful Response')


def testGetPeopleNoId(client):
    logging.info('Fetching the person with id:1')
    response = client.get('/people/1/')
    logging.info('Calling GET /people/1/')
    assert response.status_code == 200
    logging.info('Successful Response')


def testGetPeopleInvalidId(client):
    logging.info('Fetching the person with id:234')
    response = client.get('/people/234/')
    logging.info('Calling GET /people/234/')
    assert response.status_code == 404
    logging.info(response.text)

