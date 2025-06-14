numbers = {1: "uno", 2: "dos", 3: "tres", 4: "cuatro", 5: "cinco"}
print(numbers[2])
information = {"nombre": "Diego",
               "Apellido": "Aguilar",
               "Edad": 19,
               "Sexo": "Masculino",
               "Altura": 1.70}
print(information)
del information["Altura"]
print(information)
claves = information.keys()
print(claves)
print(type(claves))

values = information.values()
print(values)
print(type(values))

pairs = information.items()
print(pairs)

contacts = {"Carla": {"Apellido": "Florida",
            "Altura": 1.60,
            "Edad": 29},
            "Diego": {"Apellido": "Aguilar",    
          "Altura": 1.70,
          "Edad": 19}}
print(contacts)
            