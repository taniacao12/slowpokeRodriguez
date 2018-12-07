import json, random
from urllib.request import Request, urlopen


api_key= "64106f2b76682a44579d3f30f29c2ca5"

def toptracks():
    URL="http://ws.audioscrobbler.com/2.0/?method=chart.getTopTracks&api_key=" + api_key + "&format=json"
    response = urlopen(Request(URL, headers={'User-Agent': 'Mozilla/5.0'})).read()
    info = json.loads(response)
    return info["tracks"]["track"]

def randtoptrack():
    randNum = random.randint(0,49)
    return toptracks()[randNum]

print(randtoptrack())
