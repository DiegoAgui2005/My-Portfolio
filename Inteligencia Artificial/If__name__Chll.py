'''
Implemetar un archivo gestion_empleados.py que contenga
    1.Funciona para agregar y eliminar empleados de una lista

    2. Un bloque 'if __name__' == "main" que permita probar el
    funcionamiento del script ejecuatado directamente
'''

employeers = [
    {'name': 'Carlos', 'role': 'admin'},
    {'name': 'Juan', 'role': 'employee'},
    {'name': 'Jose', 'role': 'employee'},
    {'name': 'Ana', 'role': 'employee'}
]


def delete_employeer(employeers: list[dict], name_employeer: str):
    for employeer in employeers:
        if (employeer["name"] == name_employeer):
            employeers.remove(employeer)
            return True
    return False


def add_amployeer(employeers: list[dict], name: str, role: str):
    employeers.append({"name": name,"role": role})

if __name__ == "__main__":
    print(delete_employeer(employeers, "Juan"))
    print(employeers)
    add_amployeer(employeers, "Antonio", "admin")
    print(employeers)