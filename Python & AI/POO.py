class Person:
    """
    A class to represent a person.
    Attributes
    ----------
    name : str
        the name of the person
    age : int
        the age of the person
    Methods
    -------
    greet():
        Prints a greeting message with the person's name and age.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age} años")

person1 = Person("Diego", 25)
person2 = Person("Juan", 30)   

person1.greet()
person2.greet()