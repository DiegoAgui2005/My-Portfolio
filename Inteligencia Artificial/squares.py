numbers = [1,2,3,4,5,6,7,8,9,10]

squares = []

for number in numbers:
    square = number **2
    squares.append(square)
    
print(squares) 


numbers = [1,2,3,4,5,6,7,8,9,10]
squares = [x**2 for x in numbers]

print(squares)  # Outputs: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
