#Sistema de alquiler de carros

#Clase carro
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.available = True

    def alquilar(self):
        if self.available:
            self.available = False
            print(f"Has alquilado el {self.brand}")
        else:
            print(f"El carro {self.brand} ya está alquilado")

    def devolver(self):
        self.available = True
        print(f" Has devuelto el carro {self.brand}")

#Clase usuario
class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.rented_cars = []

    def rent_car(self, car):
        if car.available:
            car.alquilar()
            self.rented_cars.append(car)
        else:
            print(f"El carro {car.brand} No está disponible")

    def return_car(self, car):
        if car in self.rented_cars:
            car.devolver()
            self.rented_cars.remove(car)
        else:
            print(f"El carro {car.brand} no está en la lista de prestados")

class Dealership:
    def __init__(self):
        self.cars = []
        self.users = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"El carro {car.brand} ha sido agregado")

    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado")

    def show_available_cars(self):
        print("Carros disponibles")
        for car in self.cars:
            if car.available:
                print(f"El {car.brand} modelo {car.model} está disponible")

#Crear carros
car1 = Car("Kya", "Picanto")
car2 = Car("Honda", "Civic")

#Crear usuarios
user = User("Víctor Rojas", 14296042)

#Crear concesionario
dealership = Dealership()
dealership.add_car(car1)
dealership.add_car(car2)
dealership.register_user(user)

#Carros disponibles
dealership.show_available_cars()

#Alquilar carro
user.rent_car(car1)

#Carros disponibles
dealership.show_available_cars()

#Devolver carro
user.return_car(car1)

#Carros disponibles
dealership.show_available_cars()