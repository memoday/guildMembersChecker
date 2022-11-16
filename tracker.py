import checkInfo as ci
import requests
from bs4 import BeautifulSoup

def tracker(trackingNick, newNickList):

    global info

    nickInfoList = []
    maybe = [] #닉변 유력 후보

    nickInfoList = ci.checkAllGG(trackingNick)
    info = {
        "job" : nickInfoList[0],
        "level" : nickInfoList[1],
        "popularity" : nickInfoList[2],
        "union" : nickInfoList[3],
    }

    for i in range(len(newNickList)):
        check = compare(newNickList[i])
        if check == 'true':
            maybe.append(newNickList[i])
    
    return maybe

def compare(newNick):

    nickInfoList2 = ci.checkForTracker(newNick)
    newInfo = {
        "job" : nickInfoList2[0],
        "level" : nickInfoList2[1],
        "popularity" : nickInfoList2[2],
        "union" : nickInfoList2[3],
    }
    check = 'false'

    if info["job"] == newInfo["job"]:
        if int(info["level"]) <= int(newInfo["level"]):
              if int(info["popularity"])-50 <= int(newInfo["popularity"]) <= int(info["popularity"])+50:
                  if int(info["union"])-100 <= int(newInfo["union"]) <= int(info["union"])+200:
                    check = 'true'

#유니온 8000이상일 때의 조건 따로 추가, 8000이상 -50, +200
#제로일 때 인기도 9999 추가

    return check

