employees = [
    {"name": "Juan", "age": 28, "salary": 3500},
    {"name": "María", "age": 32, "salary": 4200},
    {"name": "Carlos", "age": 25, "salary": 3100},
    {"name": "Ana", "age": 40, "salary": 5000},
    {"name": "Luis", "age": 30, "salary": 3900},
]

def filter_salary():
    """
    Filtra a los empleados que ganan más de 4000 USD

    Sin parámetros

    Retorna:
    list: Una lista de empleados
    """
    return list(filter(lambda employe: employe['salary'] >= 4000, employees))

print(f'Esta es la lista de todos los empleados: {employees}')
print(f'Los empleados que ganan 4000 o más USD al mes son: {filter_salary()}')