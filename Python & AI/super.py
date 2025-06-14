#Atributos = Caraterísticas de una clase
#Métodos = Funciones de una clase
#Constructor = Método especial que se llama cuando se instancia un objeto de una clase

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def greet(self):
        print("Hello, my name is", self.name, "and I am", self.age, "years old")
        
class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self.student_id =student_id
        
    def greet(self):
        super().greet()
        print(f"My student Id is {self.student_id}")

student = Student("Diego", 25, 12345)
student.greet()       
        