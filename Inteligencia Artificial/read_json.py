import json
#Reading of the document
with open("products.json", "r") as file:
    products = json.load(file)

#Show the content
for product in products:
    print(f"{product}")