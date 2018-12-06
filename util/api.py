import json
#import urllib.request
from urllib.request import Request, urlopen

api_list = [] # list o api keys
curInd = 0 # current index of working api_keys



with open("util/api_keys.txt") as file:
    api_keys = file.read()
    api_list = api_keys.split(",")


def search():

    keyMain = ""
    for key in api_list:
        if verify_key(key) == True:
            keyMain = key
        else:
            continue
    URL = "https://www.food2fork.com/api/search?key=" + keyMain
    response = urlopen(Request(URL, headers={'User-Agent': 'Mozilla/5.0'})).read()
    info = json.loads(response)
    recipes_res = info["recipes"]

    recipes = {}
    for num in range(10):
        title = recipes_res[num]["title"]

        recipes[title] = [
            recipes_res[num]["publisher"],
            recipes_res[num]["source_url"],
            recipes_res[num]["image_url"]
        ]
    print("it working" + key)
    return recipes



def verify_key(key):
    try:
        URL = "https://www.food2fork.com/api/search?key=" + key
        response = urlopen(Request(URL, headers={'User-Agent': 'Mozilla/5.0'})).read()
        return True
    except:
        return False

search()
