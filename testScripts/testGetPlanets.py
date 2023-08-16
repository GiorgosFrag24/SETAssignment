import logging
from utilities.fieldValidator import FieldValidator
import json
import time
import statistics

expectedFields = {
    "name": str,
    "rotation_period": r'^\d+$',
    "orbital_period": r'^\d+$',
    "diameter": r'^\d+$',
    "climate": str,
    "gravity": str,
    "surface_water": r'^\d+$',
    "population": r'^\d+$',
    "residents": [r'^https?://[\S]+$'],
    "films": [r'^https?://[\S]+$'],
    "created": r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}Z$',
    "edited": r'^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{6}Z$',
    "url": r'^https?://[\S]+$'
}


def testGetPlanetsHappyPath(server):
    logging.info('Calling GET /planets/id/ with a valid id')
    response = server.get('/planets/1/')
    logging.info('Expecting response code to equal 200')
    assert response.status_code == 200
    fieldValidator = FieldValidator(expectedFields, json.loads(response.text))
    fieldValidator.validateJsonFieldPresence()
    fieldValidator.validateJsonFieldType()


def testGetPlanetsInvalidId(server):
    invalidIds = ['150', 'a', '-1', '/', '&']
    for invalidId in invalidIds:
        logging.info('Calling GET /planets/id/ with invalid id parameter ' + invalidId)
        response = server.get('/planets/' + invalidId + '/')
        logging.info('Expecting response code to equal 404')
        assert response.status_code == 404
        logging.info('Expecting response message to contain "Not Found" ')
        assert "Not Found" in response.text


def testGetPlanetsWithNoId(server):
    logging.info('Calling GET /planets/id/ with no id')
    response = server.get('/planets/')
    logging.info('Expecting response code to equal 200')
    assert response.status_code == 404
    logging.info('Expecting response message to contain "Not Found" ')
    assert "Not Found" in response.text


def testGetPlanetsWithDelays(serverWithDelay):
    duration = 60
    startTime = time.time()
    responseTimes = []
    logging.info('Waiting for the continuous access to /planets/ to finish')
    while time.time() - startTime < duration:
        startRequestTime = time.time()
        _ = serverWithDelay.get('/planets/1/')
        endRequestTime = time.time()
        responseTime = endRequestTime - startRequestTime
        responseTimes.append(responseTime)
    meanResponseTime = statistics.mean(responseTimes)
    stdDeviation = statistics.stdev(responseTimes)
    logging.info(f'The mean response time is {meanResponseTime}')
    logging.info(f'The standard deviation is {stdDeviation}')