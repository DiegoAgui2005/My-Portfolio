class Employee:
    def __init__(self, name, *args, **kwargs) -> None:
        self.name = name
        self.skills = args
        self.detail = kwargs
        
    def show_employee(self):
        print(f"Name: {self.name}")
        print(f"Skills: {self.skills}")
        print(f"Details: {self.detail}")
        
employee = Employee("Carlos", "Python", "Java", "C++", age = 30, city = "Bogota")
employee.show_employee() # Printing the employee information