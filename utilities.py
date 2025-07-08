import re

NUM_OR_DOT = re.compile(r'^[0-9.]$')

def isNumOrDot(string: str):
    return bool(NUM_OR_DOT.search(string))

def isValidNumber(string: str):
    valid = False
    try:
        float(string)
        valid = True
    finally:
        return valid

def convertNumber(string: str):
    number = float(string)
    if number.is_integer():
        number = int(number)
    return number

