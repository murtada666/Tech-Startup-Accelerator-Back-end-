
import json


def FileReading():
    with open("products/db.json", "r") as f:
        data = json.load(f)
        
        return data


def FileWritting(data, filename="products/db.json"):
    with open("products/db.json", "w") as f:
        json.dump(data, f, indent=4)
