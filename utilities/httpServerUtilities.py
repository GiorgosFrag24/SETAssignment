import logging
import json


def setUpLogger(httpServer):
    logger = logging.getLogger(httpServer)
    logger.setLevel(logging.INFO)

    fileHandler = logging.FileHandler(f'{httpServer}.log')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler)
    return logger


def openAndLoadJsonFile(filename):
    f = open(filename)
    jsonData = json.loads(f.read())
    return jsonData


def isIdValid(Id):
    if isinstance(Id, int) and Id < 100:
        return True
    return False
