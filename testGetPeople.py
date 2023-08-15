import logging
from fieldValidator import FieldValidator
import json

expectedFields = {
    "name": str,
    "height": r'^\d+$',
    "mass": r'^\d+$',
    "hair_color": str,
    "skin_color": str,
    "eye_color": str,
    "birth_year": str,
    "gender": str,
    "homeworld": r'^https?://[\S]+$',
    "films": [r'^https?://[\S]+$'],
    "species": [],
    "vehicles": [r'^https?://[\S]+$'],
    "starships": [r'^https?://[\S]+$'],
    "created": r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}Z$',
    "edited": r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}Z$',
    "url": r'^https?://[\S]+$'
}


def testGetPeopleHappyPath(client):
    logging.info('Calling GET /people/1/')
    response = client.get('/people/1/')
    logging.info('Expecting response code to equal 200')
    assert response.status_code == 200
    fieldValidator = FieldValidator(expectedFields, json.loads(response.text))
    for fieldName, expectedValue in expectedFields.items():
        logging.info(f'Expecting response body to contain field {fieldName} of type {expectedValue}')
        fieldValidator.validateJsonFieldPresence(fieldName)
        fieldValidator.validateJsonFieldType(fieldName)


def testGetPeopleNoId(client):
    logging.info('Calling GET /people/1/')
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
