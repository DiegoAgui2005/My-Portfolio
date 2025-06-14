squares = [x**2 for x in range(1,11)    ]
#print("Cuadrados:",squares)

celsius = [0,10,20,30,40,50]
fahrenheit = [(temp*(9/5)+32) for temp in celsius]
print("Temperatura en F:",fahrenheit)

#Numeros pares
evens = [x for x in range(1,21) if x%2 == 0]
print(evens)
odd = [x for x in range(1,21) if x%2 == 1]
print(evens)

matrix = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]	
print(matrix)
print(transposed)




#Doble de los Números

numeros = [1, 2, 3, 4, 5]
dobles = [x * 2 for x in numeros]
print("Dobles:", dobles)
#Filtrar y Transformar en un Solo Paso


palabras = ["sol", "mar", "montaña", "rio", "estrella"]
palabras_filtradas = [palabra.upper() for palabra in palabras if len(palabra) > 3]
print("Palabras filtradas y en mayúsculas:", palabras_filtradas)
#Crear un Diccionario con List Comprehension


claves = ["nombre", "edad", "ocupación"]
valores = ["Juan", 30, "Ingeniero"]

diccionario = {claves[i]: valores[i] for i in range(len(claves))}
print("Diccionario creado:", diccionario)
#Anidación de List Comprehensions


matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

transpuesta_comprehension = [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]
print("Transpuesta con List Comprehension:", transpuesta_comprehension)
#Extraer Información de una Lista de Diccionarios


personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Ana", "edad": 32, "ciudad": "Madrid"},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona"},
    {"nombre": "Laura", "edad": 40, "ciudad": "Madrid"}
]

nombres_madrid = [persona["nombre"] for persona in personas if persona["ciudad"] == "Madrid" and persona["edad"] > 30]
print("Nombres de personas en Madrid mayores de 30 años:", nombres_madrid)
#List Comprehension con un else


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
transformados = [x * 2 if x % 2 == 0 else x for x in numeros]
print("Números transformados:", transformados)