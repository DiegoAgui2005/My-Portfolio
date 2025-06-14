def add(a,b):
    return a + b

def substract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide(a,b):
    if b == 0:
        raise ValueError("The divisor must not be zero")
    return a / b

if __name__ == "__main__":
    print("Operations")
    res_1 = add(3,4)
    print(f"Addition:{res_1}")
    