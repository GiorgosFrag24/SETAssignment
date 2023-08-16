import logging
from flask import Flask, jsonify
import json
import time
import random

appWithDelays = Flask(__name__)
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def openAndLoadJsonFile(filename):
    f = open(filename)
    jsonData = json.loads(f.read())
    return jsonData


def isIdValid(Id):
    if isinstance(Id, int) and Id < 100:
        return True
    return False


@appWithDelays.route('/people/<int:personId>/', methods=['GET'])
def getPeople(personId):
    delay = random.uniform(0.1, 1)
    time.sleep(delay)
    if not isIdValid(personId):
        return jsonify({'detail': 'Not Found'}), 404
    return openAndLoadJsonFile('data/dummyData/people.json'), 200


@appWithDelays.route('/planets/<int:planetId>/', methods=['GET'])
def getPlanets(planetId):
    delay = random.uniform(0.1, 1)
    time.sleep(delay)
    if not isIdValid(planetId):
        return jsonify({'detail': 'Not Found'}), 404
    return openAndLoadJsonFile('data/dummyData/planets.json'), 200


@appWithDelays.route('/starships/<int:starshipId>/', methods=['GET'])
def getStarships(starshipId):
    delay = random.uniform(0.1, 1)
    time.sleep(delay)
    if not isIdValid(starshipId):
        return jsonify({'detail': 'Not Found'}), 404
    return openAndLoadJsonFile('data/dummyData/starships.json'), 200


if __name__ == '__main__':
    appWithDelays.run()
