import re
import logging


class FieldValidator:

    def __init__(self, expectedFieldValues, testData):
        self.expectedFieldValues = expectedFieldValues
        self.testData = testData

    def validateJsonFieldPresence(self, fieldName):
        #logging.info(f'Expecting field {fieldName} to be present in response')
        assert fieldName in self.testData

    def validateJsonFieldType(self, fieldName):

        fieldValue = self.testData[fieldName]
        expectedValue = self.expectedFieldValues[fieldName]
        if isinstance(expectedValue, str) and re.match(expectedValue, fieldValue):
            assert re.match(expectedValue, fieldValue)
        elif isinstance(expectedValue, list) and all(isinstance(pattern, str) for pattern in expectedValue):
            assert isinstance(fieldValue, list)
            for url, pattern in zip(fieldValue, expectedValue):
                assert re.match(pattern, url)
        else:
            assert isinstance(fieldValue, expectedValue)
