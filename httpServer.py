from utilities.httpServerUtilities import *
from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/people/<int:personId>/', methods=['GET'])
def getPeople(personId):
    logger = setUpLogger('httpServer')
    logger.info(f'Calling GET /people/{personId}/')
    if not isIdValid(personId):
        logger.info('Status code 404')
        return jsonify({'detail': 'Not Found'}), 404
    logger.info('Status code 404')
    return openAndLoadJsonFile('data/dummyData/people.json'), 200


@app.route('/planets/<int:planetId>/', methods=['GET'])
def getPlanets(planetId):
    logger = setUpLogger('httpServer')
    logger.info(f'Calling GET /planets/{planetId}/')
    if not isIdValid(planetId):
        logger.info('Status code 404')
        return jsonify({'detail': 'Not Found'}), 404
    logger.info('Status code 200')
    return openAndLoadJsonFile('data/dummyData/planets.json'), 200


@app.route('/starships/<int:starshipId>/', methods=['GET'])
def getStarships(starshipId):
    logger = setUpLogger('httpServer')
    logger.info(f'Calling GET /starships/{starshipId}/')
    if not isIdValid(starshipId):
        logger.info('Status code 404')
        return jsonify({'detail': 'Not Found'}), 404
    logger.info('Status code 200')
    return openAndLoadJsonFile('data/dummyData/starships.json'), 200


if __name__ == '__main__':
    app.run()
