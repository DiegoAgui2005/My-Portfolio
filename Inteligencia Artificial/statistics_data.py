import os
import csv
import statistics

# Obtener la ruta absoluta del script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "monthly_sales.csv")

# Intentar abrir el archivo usando la ruta absoluta
monthly_sales = {}

with open(file_path, newline='', encoding="utf-8") as f:
    reader = csv.DictReader(f)  # Usamos DictReader para acceder a los nombres de las columnas
    for row in reader:
        month = row["month"]
        sales = int(row["sales"])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(sales)


mean_sales = statistics.mean(sales)
print(f"La media es: {mean_sales}")

mean_sales = statistics.median(sales)
print(f"La mediana es: {mean_sales}")

mean_sales = statistics.mode(sales)
print(f"La mediana es: {mean_sales}")

stdev_sales = statistics.stdev(sales)
print(f"La desviación estandar es: {stdev_sales}")

variance = statistics.variance(sales)
print(f"La varianza es:{variance}")

max_sales = max(sales)
print(f"El máximo es: {max_sales}")

min_sales = min(sales)
print(f"El mínimo es: {min_sales}")

range_sales = max_sales - min_sales
print(f"El rango es: {range_sales}")