import requests
from pprint import pprint


def most_clever():
    URL = "https://akabab.github.io/superhero-api/api/all.json"
    resp = requests.get(URL)
    answer = []
    for superheroes in resp.json():
        name = superheroes["name"]
        if name in ["Hulk", "Captain America", "Thanos"]:
            intelligence = superheroes["powerstats"]["intelligence"]
            answer.append({"name": name, "intelligence": intelligence})
    return max(answer, key=lambda row: row["intelligence"])


print(most_clever())
