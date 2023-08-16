import logging
from utilities.fieldValidator import FieldValidator
import json
import time
import statistics

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


def testGetPeopleHappyPath(server):
    logging.info('Calling GET /people/id/ with a valid id')
    response = server.get('/people/1/')
    logging.info('Expecting response code to equal 200')
    assert response.status_code == 200
    fieldValidator = FieldValidator(expectedFields, json.loads(response.text))
    fieldValidator.validateJsonFieldPresence()
    fieldValidator.validateJsonFieldType()


def testGetPeopleInvalidId(server):
    invalidIds = ['150', 'a', '-1', '/', '&']
    for invalidId in invalidIds:
        logging.info('Calling GET /people/id/ with invalid id parameter ' + invalidId)
        response = server.get('/people/' + invalidId + '/')
        logging.info('Expecting response code to equal 404')
        assert response.status_code == 404
        logging.info('Expecting response message to contain "Not Found" ')
        assert "Not Found" in response.text


def testGetPeopleMissingId(server):
    logging.info('Calling GET /people/id/ with no id')
    response = server.get('/people/')
    logging.info('Expecting response code to equal 200')
    assert response.status_code == 404
    logging.info('Expecting response message to contain "Not Found" ')
    assert "Not Found" in response.text


def testGetPeopleWithDelays(serverWithDelay):
    duration = 60
    startTime = time.time()
    responseTimes = []
    logging.info('Waiting for the continuous access to /people/ to finish')
    while time.time() - startTime < duration:
        startRequestTime = time.time()
        _ = serverWithDelay.get('/people/1/')
        endRequestTime = time.time()
        responseTime = endRequestTime - startRequestTime
        responseTimes.append(responseTime)
    meanResponseTime = statistics.mean(responseTimes)
    stdDeviation = statistics.stdev(responseTimes)
    logging.info(f'The mean response time is {meanResponseTime}')
    logging.info(f'The standard deviation is {stdDeviation}')



