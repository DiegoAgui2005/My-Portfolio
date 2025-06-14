import csv

file_path = "prodcts.csv"
updated_file_path = "updated_products.csv"

with open("products.csv", "r") as file:
    csv_reader = csv.DictReader(file)
    
    fieldnames = csv_reader.fieldnames + ["total_value"]
    
    with open("updated_products.csv", "w", newline="") as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames= fieldnames)
        csv_writer.writeheader()  # write header row
        
        for row in csv_reader:
            row["total_value"] = int(row["price"]) * int(row["quantity"])
            csv_writer.writerow(row)