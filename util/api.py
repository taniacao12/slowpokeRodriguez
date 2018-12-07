import json, random
from urllib.request import Request, urlopen

from util import db

api_list = [] # list o api keys
curInd = 0 # current index of working api_keys

with open("yummly_key.txt") as file:
    api_keys = file.read()
    # print(api_keys)
    api_keys=api_keys.strip("\n")
    api_list = api_keys.split(",")
    # print(api_list)

keyMain = api_list[0]

def search(query):
    URL = "http://api.yummly.com/v1/api/recipes?_app_id=bd0cd97c&_app_key=" + keyMain + "&q=" + query
    response = urlopen(Request(URL, headers={'User-Agent': 'Mozilla/5.0'})).read()
    info = json.loads(response)
    return info["matches"]

def get_recipes(user):
    keyMain = api_list[0] #key to be used
    
    recipes = {}

    if not user:
        try:
            recipes_res = search("")
            for num in range(9):
                title = recipes_res[num]["recipeName"]

                recipes[title] = [
                    recipes_res[num]["sourceDisplayName"],
                    "https://www.yummly.com/recipe/" + recipes_res[num]["id"],
                    recipes_res[num]["imageUrlsBySize"]["90"].replace("90", "500"),
                    recipes_res[num]["ingredients"],
                    recipes_res[num]["id"]
                ]
        except:
            print("o no")

        return recipes

    to_search = random.sample(db.get_preference(user), 3)
    # to_search = ["chicken", "beans", "potato"]

    for thing in to_search:
        
    #   print("preference:!!!! " + thing )

        recipes_res = search(thing.strip().replace(" ", ""))
        try:
            for num in range(5):
                rand = random.randint(0,9)

                recipes[recipes_res[rand]["recipeName"]] = [
                    recipes_res[rand]["sourceDisplayName"],
                    "https://www.yummly.com/recipe/" + recipes_res[rand]["id"],
                    recipes_res[rand]["imageUrlsBySize"]["90"].replace("90", "500"),

                ]
        except:
            print("o no")

    print(recipes)
    return recipes

def find_recipe(recipe_id):
    URL = "http://api.yummly.com/v1/api/recipe/{}?_app_id=bd0cd97c&_app_key={}".format(recipe_id, keyMain)
    response = urlopen(Request(URL, headers={'User-Agent': 'Mozilla/5.0'})).read()
    info = json.loads(response)
    recipe_res = info
    
    recipe_info = {
        "name": recipe_res["name"],
        "image_url": recipe_res["images"][0]["hostedLargeUrl"].replace("360", "500"),
        "source_url": recipe_res["source"]["sourceRecipeUrl"],
        "ingredients": recipe_res["ingredientLines"],
        "servings": recipe_res["numberOfServings"],
        "rating": recipe_res["rating"]
    }

    return recipe_info

def verify_key(key):
    try:
        URL = "https://www.food2fork.com/api/search?key=" + key
        response = urlopen(Request(URL, headers={'User-Agent': 'Mozilla/5.0'})).read()
        info = json.loads(response)
        recipes = info["recipes"]
        return True
    except:
        return False


print(find_recipe("Curried-Tomato-Tortellini-Soup-2604059"))
