class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if new_salary < 0:
            raise ValueError("Salary must be positive")
        self._salary = new_salary
        
    @salary.deleter
    def salary(self):
        print(f"The salary of {self.name} has been deleted")
        del self._salary
        
employee = Employee("Carlos", 50000)
print(employee.salary)
employee.salary = 60000
print(employee.salary)
employee.salary =2
print(employee.salary)

del employee.salary