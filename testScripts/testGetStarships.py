import logging
from utilities.fieldValidator import FieldValidator
import json

expectedFields = {
    "name": str,
    "model": str,
    "manufacturer": str,
    "cost_in_credits": r'^\d+$',
    "length": r'^\d+(\.\d+)?$',
    "max_atmosphering_speed": r'^\d+$',
    "crew": r'^\d+$',
    "passengers": r'^\d+$',
    "cargo_capacity": r'^\d+$',
    "consumables": str,
    "hyperdrive_rating": r'^\d+(\.\d+)?$',
    "MGLT": r'^\d+$',
    "starship_class": str,
    "pilots": [r'^https?://[\S]+$'],
    "films": [r'^https?://[\S]+$'],
    "created": r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}Z$',
    "edited": r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}Z$',
    "url": r'^https?://[\S]+$'
}


def testGetStarshipsHappyPath(client):
    logging.info('Calling GET /starships/id/ with a valid id')
    response = client.get('/starships/1/')
    logging.info('Expecting response code to equal 200')
    assert response.status_code == 200
    fieldValidator = FieldValidator(expectedFields, json.loads(response.text))
    for fieldName, expectedValue in expectedFields.items():
        logging.info(f'Expecting response body to contain field {fieldName} of type {expectedValue}')
        fieldValidator.validateJsonFieldPresence(fieldName)
        fieldValidator.validateJsonFieldType(fieldName)


def testGetStarshipsInvalidId(client):
    invalidIds = ['150', 'a', '-1', '/', '&']
    for invalidId in invalidIds:
        logging.info('Calling GET /starships/id/ with invalid id parameter ' + invalidId)
        response = client.get('/starships/' + invalidId + '/')
        logging.info('Expecting response code to equal 404')
        assert response.status_code == 404
        logging.info('Expecting response message to contain "Not Found" ')
        assert "Not Found" in response.text


def testGetPlanetsWithNoId(client):
    logging.info('Calling GET /starships/id/ with no id')
    response = client.get('/starships/')
    logging.info('Expecting response code to equal 404')
    assert response.status_code == 404
    logging.info('Expecting response message to contain "Not Found" ')
    assert "Not Found" in response.text



