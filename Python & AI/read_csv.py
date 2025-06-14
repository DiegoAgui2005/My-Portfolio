import csv

# Open the file
"""with open("products.csv", mode = "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)"""
        
        
# Show the info by columns
with open("products.csv", mode = "r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        brand_name = row.get('BrandName', 'Unknown')
        price = row.get('Price', 'Unknown')
        print(f"Producto: {brand_name}, Precio: {price}")