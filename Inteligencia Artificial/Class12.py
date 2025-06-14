numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    print("Aquí i es igual a:", i + 1)

for i in range(10):
    print(i)
    
for i in range(3, 10):
    print(i)
    
fruits = ["apple", "banana", "cherry", "orange"]
for fruit in fruits:
    print(fruit)
    if fruit == "orange":
        print("Orange is in the list")
        
x = 0
while x<5:
    if x == 3:
        break
    x += 1
    print(x)
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in numbers:
    if i == 5:
        break
    print("Aquí i es igual a:", i + 1)