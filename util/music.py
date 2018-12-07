import json, random
from urllib.request import Request, urlopen

fm_key = ""
you_key = ""

with open("lastFM_keys.txt") as file:
    api_keys = file.read()
    fm_key = api_keys.strip("\n")

with open("youtube_keys.txt") as file:
    api_keys = file.read()
    you_key = api_keys.strip("\n")

def toptracks():
    URL="http://ws.audioscrobbler.com/2.0/?method=chart.getTopTracks&api_key=" + fm_key + "&format=json"
    #print(URL)
    try:
        response = urlopen(Request(URL, headers={'User-Agent': 'Mozilla/5.0'})).read()
        info = json.loads(response)
        return info["tracks"]["track"]
    except:
        return None



def randtoptrack():
    randNum = random.randint(0,49)
    try:
        ptracks= toptracks()[randNum]
        return ptracks["name"] + " " + ptracks["artist"]["name"]
    except:
        return None


def randyoutube():
    try:
        randTrack = randtoptrack()
        #print("randTrack: " + randTrack)
        randtrackl=randTrack.split()
        finalrandurl = ""
        for i in range(len(randtrackl)):
            finalrandurl += randtrackl[i] + "%20"
        #print ("url: " + finalrandurl)

        URL = "https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q=" + finalrandurl + "&key=" + you_key
        #print(URL)
        try:
            response = urlopen(Request(URL, headers={'User-Agent': 'Mozilla/5.0'})).read()
            info = json.loads(response)
            return "https://www.youtube.com/embed/" + info["items"][0]["id"]["videoId"] + "?ecver=1"
        except:
            #print("first error")
            return None
    except:
        #print("second erro")
        return None




#print(toptracks())
print(randyoutube())
