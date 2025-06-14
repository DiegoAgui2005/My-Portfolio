from collections import Counter

def count_sales(products: list[str]) -> Counter:
    return Counter(products)

sales = ["laptop", "desktop", "laptop", "monitor", "mouse", "mouse", "mouse"]
result = count_sales(sales)
print(result)