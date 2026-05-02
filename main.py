import matplotlib.pyplot as plt
import numpy
from io import BytesIO
import re

from stats import *

def getStats(combos: str, coin: bool = False):
    """
    Show/Compare the stats of (up to) 10 combos.

    Parameters
    ----------
    combos: str
        Comma separated combos
    
    coin: bool
        Optional: Include coin curve values for each combo
    """
    exitProgram = False

    fullStats = []

    # get all combos
    inputList = re.split(",+", combos)
    if len(inputList) > 10: # more than 10 combos
        raise OverflowError(f"Too many combos! (received {len(inputList)} combos, only 10 allowed)")
    elif len(inputList) == 0:
        raise IndexError("Please input a combo to show stats!")

    valueIsIncorrect = False
    incorrectCombos = ""

    # create list of short names: [["c", "v"], ...]
    for i in range(len(inputList)):
        inputList[i] = str(inputList[i]).strip().lower()

    # process inputs into correct format: [["c", "v"], ...]
    processedList = inputList
    for i in range(len(inputList)):
        if len(re.findall("\\s+", inputList[i])) != 1: # bad syntax
            incorrectCombos = incorrectCombos + ", " if incorrectCombos != "" else "" + str(i+1)
            raise SyntaxError(f"Bad input! (incorrect syntax in these combos: {incorrectCombos})")
        processedList[i] = re.split("\\s+", inputList[i])
    
    # get and assign values
    try:
        fullStats = getNamesAndStats(processedList) # assign values
    except ValueError as e:
        raise ValueError(f"Bad input! ({e})")
    
    # return values
    return 