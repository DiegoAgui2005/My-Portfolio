#Fibonacci
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610

def fibonacci(limit):
    a, b = 0, 1
    while a< limit:
        yield a
        a, b = b, a+b
for num in fibonacci(1000):
    print(num)