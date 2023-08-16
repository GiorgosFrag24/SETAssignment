from flask import Flask, jsonify
from utilities.httpServerUtilities import *
import json
import time
import random

appWithDelays = Flask(__name__)


@appWithDelays.route('/people/<int:personId>/', methods=['GET'])
def getPeople(personId):
    logger = setUpLogger('httpServerWithDelays')
    logger.info(f'Calling GET /people/{personId}/')
    delay = random.uniform(0.1, 1)
    time.sleep(delay)
    if not isIdValid(personId):
        logger.info('Status code 404')
        return jsonify({'detail': 'Not Found'}), 404
    logger.info('Status code 200')
    return openAndLoadJsonFile('data/dummyData/people.json'), 200


@appWithDelays.route('/planets/<int:planetId>/', methods=['GET'])
def getPlanets(planetId):
    logger = setUpLogger('httpServerWithDelays')
    logger.info(f'Calling GET /planets/{planetId}/')
    delay = random.uniform(0.1, 1)
    time.sleep(delay)
    if not isIdValid(planetId):
        logger.info('Status code 404')
        return jsonify({'detail': 'Not Found'}), 404
    logger.info('Status code 200')
    return openAndLoadJsonFile('data/dummyData/planets.json'), 200


@appWithDelays.route('/starships/<int:starshipId>/', methods=['GET'])
def getStarships(starshipId):
    logger = setUpLogger('httpServerWithDelays')
    logger.info(f'Calling GET /starships/{starshipId}/')
    delay = random.uniform(0.1, 1)
    time.sleep(delay)
    if not isIdValid(starshipId):
        logger.info('Status code 404')
        return jsonify({'detail': 'Not Found'}), 404
    logger.info('Status code 200')
    return openAndLoadJsonFile('data/dummyData/starships.json'), 200


if __name__ == '__main__':
    appWithDelays.run()
