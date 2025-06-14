# Description: This file contains the basic concepts of Object Oriented Programming (OOP) in Python.

# Class: A class is a blueprint for creating objects (a particular data structure), providing initial values for state (member variables or attributes), and implementations of behavior (member functions or methods).
# Basic example of a class

class Person:
    def __init__(self,name,age): #Constructor
        self.name = name #Atributo
        self.age = age #Atributo
        
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old") #Método
        
persona1 = Person("Diego", 19)
persona1.greet() #Hello, my name is Diego and I am 19 years old


#Example of a Constructor

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

person1 = Person("Diego", 19)
print(person1.name) #Diego
print(person1.age) #19


#Example of super() function

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
        
    def greet(self):
        print("Hello I am a person")
        
        
class Student(Person):
    def __init__(self, name, age, student_id):  # Corrected method name to __init__
        super().__init__(name, age)
        self.student_id = student_id
        
    def greet(self):
        super().greet()
        print(f"My student ID is {self.student_id}")
        
student = Student("Diego", 19, 12345)
student.greet()  # Hello I am a person
                 # My student ID is 12345
                 
                 
class LivingBeing:
    def __init__(self, name):
        self.name = name

class Person(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and my student ID is {self.student_id}")

# Crear instancia de Student
student = Student("Carlos", 21, "S54321")
student.introduce()  # Output: Hi, I'm Carlos, 21 years old, and my student ID is S54321


class LivingBeing:
    def __init__(self, name):
        self.name = name

class Person(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old, and my student ID is {self.student_id}")

# Crear instancia de Student
student = Student("Carlos", 21, "S54321")
student.introduce()  # Output: Hi, I'm Carlos, 21 years old, and my student ID is S54321


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} años"

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age})"

# Crear instancias de Person
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Uso de __str__
print(person1)  # Output: Alice, 30 años

# Uso de __repr__
print(repr(person1))  # Output: Person(name=Alice, age=30)