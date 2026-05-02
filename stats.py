import numpy as np
import pandas as pd

cInput = []

cStats = []
vStats = []

tStats = []
tNames = ["", ""]

statsOut = []
namesOut = []

cCurveOut = []

nameAndStats = [["", ""], [0 for _ in range(10)]]
finalOutput = []

cCount = 0

testInputCombos = [["mario", "blooper"]]
testInputCoin = [9]

csvCharStats = pd.read_csv("csv/charStats.csv")
csvVehStats = pd.read_csv("csv/vehStats.csv")
csvCoinCurve = pd.read_csv("csv/coinCurve.csv")
# the rest

def getValues(combos):
    returnVal = [[["", ""], [0 for _ in range(10)]] for _ in range(len(combos))] # [[["h", "h"], [0, 0, 0, ...]], ...]

    # try:
    for i in range(len(combos)):
        # character
        row = csvCharStats.index[csvCharStats["Short"] == combos[i][0]].tolist() # find row index
        
        # not found
        if row == []: 
            raise ValueError(f"\"{combos[i][0]}\" is not a character") # error for nonexistent character
        
        result = csvCharStats.iloc[row[0]].tolist() # get row values
        tNames[0] = csvCharStats.at[row[0], "Name"] # get name
        cStats = ["" for _ in range((len(result)-2))] # get only stats
        for k in range(len(result)-2):
            cStats[k] = int(result[k+2])
        
        # vehicle 
        row = csvVehStats.index[csvVehStats["Short"] == combos[i][1]].tolist() # find row index
        
        # not found
        if row == []:     
            raise ValueError(f"\"{combos[i][1]}\" is not a vehicle") # error for nonexistent vehicle
        
        result = csvVehStats.iloc[row[0]].tolist() # get row values
        tNames[1] = csvVehStats.at[row[0], "Name"] # get name
        vStats = ["" for _ in range((len(result)-2))] # get only stats
        for k in range(len(result)-2):
            vStats[k] = int(result[k+2])
        
        tStats = np.add(cStats, vStats).tolist() # total stats

        # [[["h", "h"], [1, 1, 1]], ...]
        # [combo][names/stats][values]
        print(returnVal)
        returnVal[i][0] = [tNames[0], tNames[1]]
        returnVal[i][1] = tStats
        print(returnVal)
    
    return returnVal
    # except Exception:
    #     raise ValueError()

def getCoinCurve(statList):
    cCurveOut = [[0.0 for _ in range(21)] for _ in range(len(statList))]

    for i in range(len(statList)):
        result = csvCoinCurve.iloc[statList[i]].tolist() # get row values
        for k in range(len(result)-1):
            cCurveOut[i][k] = float(result[k+1])
    
    return cCurveOut

def getNamesAndStats(combos):
    cCount = len(combos)
    cInput = combos
    finalOutput = [[["", ""], [0 for _ in range(10)]] for _ in range(cCount)]

    namesOut = [["", ""] for _ in range(cCount)] # [["", ""], ["", ""], ...]
    statsOut = [[0] for _ in range(10) for _ in range(cCount)] # [[0, 0, ...], [0, 0, ...]]

    # assign and return names and stats: [[["h", "h"], [1, 1, 1]], ...]
    # get and assign stats
    # [combo][names/stats][values]
    
    return getValues(combos)

# getNamesAndStats(testInput)
# getCoinCurve(testInputCoin)