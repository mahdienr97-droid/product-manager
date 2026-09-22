import os

print(os.getcwd())

import json
try:
    with open ("products.json","r") as file:
        products = json.load(file)

    total = 0
    counter = 0
    for product in products:
        total += product["price"]
        counter += 1
    print("Number of products:",counter)
    print("Total:",total)
    print("Git practice")
    print("Git is useful")
    print("Staging test")
    print("Search feature")


except FileNotFoundError:
    print("File Not Found")

except json.JSONDecodeError:
    print("Invalid JSON")