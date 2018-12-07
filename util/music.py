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
<<<<<<< HEAD
    # print(URL)
=======
    #print(URL)
>>>>>>> 5fb6ba100f4c4c5743247c1a742cfc05926b2425
    response = urlopen(Request(URL, headers={'User-Agent': 'Mozilla/5.0'})).read()
    info = json.loads(response)
    return info["tracks"]["track"]

def randtoptrack():
    randNum = random.randint(0,49)
    return toptracks()[randNum]["name"]


def randyoutube():
    randTrack = randtoptrack()
<<<<<<< HEAD
    # print("randTrack: " + randTrack)
=======
    #print("randTrack: " + randTrack)
>>>>>>> 5fb6ba100f4c4c5743247c1a742cfc05926b2425
    randtrackl=randTrack.split()
    finalrand = ""
    for i in range(len(randtrackl)):
        finalrand += randtrackl[i] + "%20"
<<<<<<< HEAD
    # print (finalrand)

    URL = "https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q=" + finalrand + "&key=" + you_key
    # print(URL)
=======
    #print (finalrand)

    URL = "https://www.googleapis.com/youtube/v3/search?part=snippet&type=video&q=" + finalrand + "&key=" + you_key
    #print(URL)
>>>>>>> 5fb6ba100f4c4c5743247c1a742cfc05926b2425
    response = urlopen(Request(URL, headers={'User-Agent': 'Mozilla/5.0'})).read()
    info = json.loads(response)
    return "https://www.youtube.com/embed/" + info["items"][0]["id"]["videoId"] + "?ecver=1"



# print(randtoptrack())
<<<<<<< HEAD
# print(randyoutube())
=======
#print(randyoutube())
>>>>>>> 5fb6ba100f4c4c5743247c1a742cfc05926b2425
