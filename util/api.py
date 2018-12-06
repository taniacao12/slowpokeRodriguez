import json
#import urllib.request
from urllib.request import Request, urlopen

def search():
    URL = "https://www.food2fork.com/api/search?key=d17e8595c263b1890118c592b195e191&q=" + "chicken"

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

    # print(recipes);
    return recipes;

search()
