import json
#import urllib.request
from urllib.request import Request, urlopen

def search():
    cApi=urlopen("https://www.food2fork.com/api/search?key=116b5832d48d9f642361a4e878b5cf8f&q=" + "chicken")
    cApi = cApi.read()
    dict = json.loads(cApi)

    print(dict)

search()
