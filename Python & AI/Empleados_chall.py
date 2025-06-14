def lista_empleados(lista_empleados:list, limite_salario:float)-> list:
    return [emp['nombre'] for emp in lista_empleados if emp['sueldo'] > limite_salario]


lista = [
    {"nombre": "Maria La del Barrio",
     "edad": 30,
     "sueldo": 30000
     },
    {"nombre": "Luis Miguel",
     "edad": 25,
     "sueldo": 25000
     },
    {"nombre": "Ana Bolena",
     "edad": 20,
     "sueldo": 20000
     },
     {"nombre": "Pepe Grillo",
     "edad": 20,
     "sueldo": 50000
     }
]

print(lista_empleados(lista, 25000))
def lista_empleados(lista_empleados: list, limite_salario: float) -> list:
    return [emp['nombre'] for emp in lista_empleados if emp['sueldo'] > limite_salario]

lista = [
    {"nombre": "Maria La del Barrio", "edad": 30, "sueldo": 30000},
    {"nombre": "Luis Miguel", "edad": 25, "sueldo": 25000},
    {"nombre": "Ana Bolena", "edad": 20, "sueldo": 20000},
    {"nombre": "Pepe Grillo", "edad": 20, "sueldo": 50000}
]

print(lista_empleados(lista, 25000))