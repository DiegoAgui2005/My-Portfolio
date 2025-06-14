def check_Access(func):
    def wrapper(employee):
        if employee["role"] == "admin":
            return func(employee)
        else:
            print("No tiene permisos para acceder")
    return wrapper

@check_Access
def delete_employee(employee):
    print(f'Employee {employee["name"]}')
    
admin = {"name": "John", "role": "admin"}
employee = {"name": "Jane", "role": "employee"}

delete_employee(admin)  # Output: Employee John
delete_employee(employee)  # Output: No tiene permisos para acceder