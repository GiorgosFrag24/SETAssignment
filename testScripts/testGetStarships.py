import logging
from utilities.fieldValidator import FieldValidator
import json
import time
import statistics

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


def testGetStarshipsHappyPath(server):
    logging.info('Calling GET /starships/id/ with a valid id')
    response = server.get('/starships/1/')
    logging.info('Expecting response code to equal 200')
    assert response.status_code == 200
    fieldValidator = FieldValidator(expectedFields, json.loads(response.text))
    fieldValidator.validateJsonFieldPresence()
    fieldValidator.validateJsonFieldType()


def testGetStarshipsInvalidId(server):
    invalidIds = ['150', 'a', '-1', '/', '&']
    for invalidId in invalidIds:
        logging.info('Calling GET /starships/id/ with invalid id parameter ' + invalidId)
        response = server.get('/starships/' + invalidId + '/')
        logging.info('Expecting response code to equal 404')
        assert response.status_code == 404
        logging.info('Expecting response message to contain "Not Found" ')
        assert "Not Found" in response.text


def testGetPlanetsWithNoId(server):
    logging.info('Calling GET /starships/id/ with no id')
    response = server.get('/starships/')
    logging.info('Expecting response code to equal 404')
    assert response.status_code == 404
    logging.info('Expecting response message to contain "Not Found" ')
    assert "Not Found" in response.text


def testGetStarshipsWithDelays(serverWithDelay):
    duration = 60
    startTime = time.time()
    responseTimes = []
    logging.info('Waiting for the continuous access to /starships/ to finish')
    while time.time() - startTime < duration:
        startRequestTime = time.time()
        _ = serverWithDelay.get('/starships/10/')
        endRequestTime = time.time()
        responseTime = endRequestTime - startRequestTime
        responseTimes.append(responseTime)
    meanResponseTime = statistics.mean(responseTimes)
    stdDeviation = statistics.stdev(responseTimes)
    logging.info(f'The mean response time is {meanResponseTime}')
    logging.info(f'The standard deviation is {stdDeviation}')

