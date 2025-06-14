from datetime import datetime
"""
Implementa un decorador llamado log_employee_action
que registre cualquier acción realizada por un empleado en un archivo de texto.

"""
# Función decorador que será la de escribir en el archivo de texto las acciones de los empleados
def log_empleados(func):
    def wrapper(empleado):
        print('Log de la transaccion...')
        with open('log.txt', 'a') as file:
            file.write(f'{func(empleado)}\n')
        print('Log terminado...')
    return wrapper

# Función decorador que será la de escribir en el archivo de texto las acciones de los admin
# La diferencia es la cantidad de parámetros, todos se registra en el mismo log.txt
def log_admin(func):
    def wrapper(empleado, admin):
        print('Log de la transaccion...')
        with open('log.txt', 'a') as file:
            file.write(f'{func(empleado, admin)}\n')
        print('Log terminado...')
    return wrapper


# Función que permite al rol admin eliminar un empleado
@log_admin
def eliminar_empleado(empleado, admin):
    print(f"{datetime.now()} El administrador {admin['nombre']} ha eliminado al empleado {empleado['nombre']}")
    return f"{datetime.now()} El administrador {admin['nombre']} ha eliminado al empleado {empleado['nombre']}"

# Función que permite al rol admin registrar un empleado
@log_admin
def registrar_empleado(empleado, admin):
    print(f"{datetime.now()} El administrador {admin['nombre']} ha registrado al empleado {empleado['nombre']}")
    return f"{datetime.now()} El administrador {admin['nombre']} ha registrado al empleado {empleado['nombre']}"

# Función que permite al rol empleado ingresar al sistema
@log_empleados
def ingresar_al_sistema(empleado):
    print(f"{datetime.now()} El empleado {empleado['nombre']} ha ingresado al sistema")
    return f"{datetime.now()} El empleado {empleado['nombre']} ha ingresado al sistema"

# Función que permite al rol empleado salir del sistema
@log_empleados
def salir_del_sistema(empleado):
    print(f"{datetime.now()} El empleado {empleado['nombre']} ha salido al sistema")
    return f"{datetime.now()} El empleado {empleado['nombre']} ha salido del sistema"

# Ejemplo de uso
# Se crea un admin y 3 empleados
admin = {'nombre': 'Iris', 'rol': 'admin'}
e1 = {'nombre': 'Jose', 'rol': 'empleado'}
e2 = {'nombre': 'Ana', 'rol': 'empleado'}
e3 = {'nombre': 'Samuel', 'rol': 'empleado'}

ingresar_al_sistema(e1) # José ingresa al sistema
ingresar_al_sistema(e3) # Samuel ingresa al sistema
salir_del_sistema(e3) # Samuel sale del sistema
eliminar_empleado(e3, admin) # El admin Iris elimina al empleado Samuel
registrar_empleado(e2, admin) # El admin Iris registra al empleado Ana