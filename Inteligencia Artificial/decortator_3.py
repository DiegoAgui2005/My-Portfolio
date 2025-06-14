# Decorator that checks if an employee has a specific role
def check_access(required_role):
    def decorator(func):
        def wrapper(employee):
            # Check if the employee has the required role
            if employee.get("role") == required_role:
                return func(employee)
            else:
                print(f"Access denied to {employee['name']}")
                return None
        return wrapper
    return decorator

def log_action(func):
    def wrapper(employee):
        print(f"Action performed by {employee['name']}")
        return func(employee)
    return wrapper

@check_access("admin")
@log_action
def delete_employee(employee):
    print(f"Deleting employee {employee['name']} from the database")

admin = {"name": "John", "role": "admin"}
employee = {"name": "Jane", "role": "employee"}

delete_employee(admin)  # Output: Action performed by John, Deleting employee John from the database
delete_employee(employee) # Output: Access denied to Jane