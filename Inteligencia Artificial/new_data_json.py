import json

file_path = "products.json"

new_product = {
    "id": 4,
    "name": "Smartwatch",
    "price": 199.99,
    "category": "Electronics",
    "quantity": 10
    }

# Open the file in read mode
with open(file_path, "r") as file:
    products = json.load(file)
    
    
products.append(new_product)

# Open the file in write mode

with open(file_path, "w") as file:
    json.dump(products, file, indent=4)