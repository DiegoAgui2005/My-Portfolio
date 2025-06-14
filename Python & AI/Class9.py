matrix = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
print(matrix)
print(matrix[0])
print(matrix[2][1])
numbers = (1,3,4,5,6,7,8,9,10)
print(type(numbers))
print(numbers[0])
numbers[0] = "unos"
print(numbers) # It is not possible to change the values of a tuple
# Tuples are immutable

checkers_board = [
    [0, 'b', 0, 'b', 0, 'b', 0, 'b'],
    ['b', 0, 'b', 0, 'b', 0, 'b', 0],
    [0, 'b', 0, 'b', 0, 'b', 0, 'b'],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    ['w', 0, 'w', 0, 'w', 0, 'w', 0],
    [0, 'w', 0, 'w', 0, 'w', 0, 'w'],
    ['w', 0, 'w', 0, 'w', 0, 'w', 0]
]

print(checkers_board)