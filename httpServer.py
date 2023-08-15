import logging
from flask import Flask, jsonify
import json

app = Flask(__name__)
logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def openAndLoadJsonFile(filename):
    f = open(filename)
    jsonData = json.loads(f.read())
    return jsonData


def isIdValid(Id):
    if isinstance(Id, int) and Id < 100:
        return True
    return False


@app.route('/people/<int:personId>/', methods=['GET'])
def getPeople(personId):
    if not isIdValid(personId):
        return jsonify({'detail': 'Not Found'}), 404
    return openAndLoadJsonFile('data/people.json'), 200


@app.route('/planets/<int:planetId>/', methods=['GET'])
def getPlanets(planetId):
    if not isIdValid(planetId) :
        return jsonify({'detail': 'Not Found'}), 404
    return openAndLoadJsonFile('data/planets.json'), 200


@app.route('/starships/<int:starshipId>/', methods=['GET'])
def getStarships(starshipId):
    if not isIdValid(starshipId) :
        return jsonify({'detail': 'Not Found'}), 404
    return openAndLoadJsonFile('data/starships.json'), 200

if __name__ == '__main__':
    app.run()
