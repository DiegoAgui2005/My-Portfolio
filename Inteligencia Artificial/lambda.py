add = lambda a,b: a+b
print(add(10,4))

multiply = lambda a,b: a*b
print(multiply(10,4)) 

divide = lambda a,b,c: a/b/c
print(divide(10,4,2))

#Cuadrado de cada número
numbers = range(11)
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)


#Pares
even_numbers = list(filter(lambda x: x%2==0, numbers))
print(even_numbers)

#Impares
odd_numbers = list(filter(lambda x: x%2!=0, numbers))
print(odd_numbers)