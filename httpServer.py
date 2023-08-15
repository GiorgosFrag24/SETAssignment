import logging
from flask import Flask, jsonify

app = Flask(__name__)

logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def isIdValid(Id):
    if isinstance(int, Id) and Id<100:
        return True
    return False

@app.route('/people/<int:personId>/', methods=['GET'])
def getPeople(personId):
    if personId > 100:
        return jsonify({'error': 'Not Found'}), 404
    else:
        return jsonify({'name': 'Luke Skywalker', 'height': '172cm'}), 200


@app.route('/planets/<int:planetId>/', methods=['GET'])
def getPlanets(planetId):
    if planetId > 100:
        return jsonify({'error': 'Not Found'}), 404
    else:
        return jsonify({'name': 'Luke Skywalker', 'height': '172cm'}), 200


if __name__ == '__main__':
    app.run()
