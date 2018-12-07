import json, random
from urllib.request import Request, urlopen


fm_key= "64106f2b76682a44579d3f30f29c2ca5"

you_key="AIzaSyB54bR0_J9yC_IpWsbqM-faMRdSgM6GpoA"

def toptracks():
    URL="http://ws.audioscrobbler.com/2.0/?method=chart.getTopTracks&api_key=" + fm_key + "&format=json"
    print(URL)
    response = urlopen(Request(URL, headers={'User-Agent': 'Mozilla/5.0'})).read()
    info = json.loads(response)
    return info["tracks"]["track"]

def randtoptrack():
    randNum = random.randint(0,49)
    return toptracks()[randNum]["name"]


def randyoutube():
    randTrack = randtoptrack()
    randtrackl=randTrack.split()
    finalrand = ""
    for i in range(len(randtrackl)-1):
        finalrand += randtrackl[i] + "%20"
    print (finalrand)

    URL = "https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q=" + finalrand + "&key=" + you_key
    print(URL)
    response = urlopen(Request(URL, headers={'User-Agent': 'Mozilla/5.0'})).read()
    info = json.loads(response)
    yourl="https://www.youtube.com/watch?v="
    return "https://www.youtube.com/watch?v=" + info["items"][0]["id"]["videoId"]


print(randtoptrack())
print(randyoutube())
