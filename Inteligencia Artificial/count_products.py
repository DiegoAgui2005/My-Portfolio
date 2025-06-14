from collections import defaultdict

def count_products(orders: list[str]) -> dict[str, int]:
    product_count = defaultdict(int)
    for product in orders:
            product_count[product] += 1
    return product_count

orders = ["Laptop", "Laptop", "Monitor", "Mouse", "Mouse", "Mouse"]
count = count_products(orders)
print(count)
