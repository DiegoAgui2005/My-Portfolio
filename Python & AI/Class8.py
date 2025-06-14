to_do = ["Dirigirnos al hotel", "Hacer el check-in", "Dejar las maletas", "Ir a la playa", "Almorzar", "Descansar", "Cenar", "Dormir"]
print(to_do)
numbers = [1, 2, 3, 4, "5", "Cincos", 6, 7, 8, 9, 10]
print(numbers)
print(type(numbers))
mix = ["uno", 2 , 3.14, True, ["Hola","MundO"],5]
print(mix)
print(len(mix))
print("Primer elemento", mix[0])
print("Segundo elemento", mix[1])
print("Ultimo elemento", mix[-1])
print("Penultimo elemento", mix[-2])
String = "Hola Mundo"
print(String[0])
print(String[1])
print(mix[0:2]) # It does not consider number two
print(mix[2:])
print(mix[2:-2])

print(mix)
mix.append(False)   # It adds an element to the end of the list
print(mix)
mix.append(["a","b","c"])
print(mix)
mix.insert(1,["a","b","c"]) # We can add an element in a specific position
print(mix)
print(mix.index(3.14))

numbers = [1, 2, 100, 90, 5, 45, 3, 8, 9, 10]
print("Max:", max(numbers))
print("Min:", min(numbers))
print("The max number is:", numbers.index(max(numbers)))

del numbers [-1]
print(numbers)
del numbers 
print(numbers) # It deletes the list

numbers = 1
print(numbers)
