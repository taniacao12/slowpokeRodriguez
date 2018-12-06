import json
#import urllib.request
from urllib.request import Request, urlopen

api_list = [] # list o api keys
curInd = 0 # current index of working api_keys



with open("food2fork_keys.txt") as file:
    api_keys = file.read()
    print(api_keys)
    api_keys=api_keys.strip("\n")
    api_list = api_keys.split(",")
    print(api_list)


def search(query):
    keyMain = "" #key to be used
    #need to add try except here
    URL=""
    info=""
    for key in api_list:
        URL = "https://www.food2fork.com/api/search?key=" + key + "&q=" + query
        print(URL)
        response = urlopen(Request(URL, headers={'User-Agent': 'Mozilla/5.0'})).read()
        info = json.loads(response)
        if "error" not in info:
            keyMain = key
<<<<<<< HEAD
            break

        # if verify_key(key) == True:
        #     keyMain = key
        # else:
        #     keyMain = ""
        #     continue
    print("keymain" + keyMain)
    #keyMain="94c7e919219ad94b3d5997ef849a8884"

    # URL = "https://www.food2fork.com/api/search?key=" + keyMain + "&q=" + query
    # response = urlopen(Request(URL, headers={'User-Agent': 'Mozilla/5.0'})).read()
    # info = json.loads(response)
    #print(info)
=======
        else:
            keyMain = ""
            continue

    keyMain = "31ba86125159f0785f5e18dc89b4730d"
    URL = "https://www.food2fork.com/api/search?key=" + keyMain + "&q=chicken"

    response = urlopen(Request(URL, headers={'User-Agent': 'Mozilla/5.0'})).read()
    info = json.loads(response)
    print(info)
>>>>>>> 7a71eb201701a9fd848f0f254f7faa08e50e840e
    recipes_res = info["recipes"]

    recipes = {}
    for num in range(10):
        title = recipes_res[num]["title"]

        recipes[title] = [
            recipes_res[num]["publisher"],
            recipes_res[num]["source_url"],
            recipes_res[num]["image_url"]
        ]
    #print("it working" + key)
    return recipes



def verify_key(key):
    try:
        URL = "https://www.food2fork.com/api/search?key=" + key
        response = urlopen(Request(URL, headers={'User-Agent': 'Mozilla/5.0'})).read()
        info = json.loads(response)
        recipes = info["recipes"]
        #print(recipes)
        return True
    except:
        #print("broken")
        return False

def test():
    keyMain="e6680d203687186f7099c33ccb2d6a61"
    URL = "https://www.food2fork.com/api/search?key=" + keyMain + "&q=chicken"
    response = urlopen(Request(URL, headers={'User-Agent': 'Mozilla/5.0'})).read()
    print(response)

search("chicken")
#test()
