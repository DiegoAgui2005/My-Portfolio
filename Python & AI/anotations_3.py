class Employee:
    name: str 
    age: int
    salary: float
    
    def __init__(self,name: str, age: int,salary: float):
        self.name = name
        self.age = age
        self.salary = salary
    
    def introduce(self) -> str:
        return f"Hello, my name is {self.name} I am {self.age} years old"
    
employee1 = Employee("Carlos", 30, 3500.0)
print(employee1.introduce())