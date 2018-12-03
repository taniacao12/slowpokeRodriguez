import json
#import urllib.request
from urllib.request import Request, urlopen

def search():
    URL = "https://www.food2fork.com/api/search?key=116b5832d48d9f642361a4e878b5cf8f&q=" + "chicken"

    response = urlopen(Request(URL, headers={'User-Agent': 'Mozilla/5.0'})).read()
    info = json.loads(response)
    recipes_res = info["recipes"]

    recipes = {}
    for num in range(5):
        title = recipes_res[num]["title"]

        recipes[title] = [
            recipes_res[num]["publisher"],
            recipes_res[num]["source_url"],
            recipes_res[num]["image_url"]
        ]

    print(recipes);
    return recipes;

search()
