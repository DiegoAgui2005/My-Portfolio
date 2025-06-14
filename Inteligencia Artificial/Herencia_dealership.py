from Dealership import Customer


class Vehicle:
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True
    
    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehiculo {self.brand} ha sido vendido")
        else:
            print(f"El vehiculo {self.brand} no está disponible")
            
    def check_available(self):
        return self.is_available 
    
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
    def stop_engine(self):
        raise NotImplementedError("Este metodo debe ser implementado por la subclase")
    
class Car(Vehicle):
        def start_engine(self):
            if not self.is_available:
                return f"El motor del coche {self.band} está en marcha"
            else:
                return f"El coche {self.brand} no está disponible" 
        
        def stop_engine(self):
            if self.is_available:
                return f"El motor del coche {self.brand} se ha detenido"
            else:
                return f"El coche {self.brand} no está disponible"
            
            
class Bike(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"La bicicleta {self.brand} está en marcha"
        else:
            return f"La bicicleta {self.brand} no está disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"La bicicleta {self.brand} se ha detenido"
        else:
            return f"La bicicleta {self.brand} no está disponible"
        
class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del camión {self.brand} está en marcha"
        else:
            return f"El camión {self.brand} no está disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"El motor del camión {self.brand} se ha detenido"
        else:
            return f"El camión {self.brand} no está disponible"
        
class Avion(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del avión {self.brand} está en marcha"
        else:
            return f"El avión {self.brand} no está disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"El motor del avión {self.brand} se ha detenido"
        else:
            return f"El avión {self.brand} no está disponible"
        
    class Customer:
        def __init__(self, name):
            self.name = name
            self.purchased_vehicles = []
            
        def buy_vehicle(self, vehicle: Vehicle):
            if vehicle.check_available():
                vehicle.sell()
                self.purchased_vehicles.append(Vehicle)
            else:
                print(f"Lo siento, {vehicle.brand} no está disponible")
                
                
        def inquire_vehicle(self, vehicle: Vehicle):
            if vehicle.check_available():
                print(f"El vehiculo {vehicle.brand} está disponible")
            else:
                print(f"El vehiculo {vehicle.brand} no está disponible")
            print(f"El precio del vehiculo es {vehicle.get_price()}")
        
class Dealership:
    def __init__(self):
        self.vehicles = []
        self.customers = []
        
    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)
        print(f"El vehiculo {vehicle.brand} ha sido agregado")
        
    def register_customer(self, customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} ha sido registrado")
        
    def show_available_vehicles(self):
        print("Vehiculos disponibles:")
        for vehicle in self.vehicles:
            if vehicle.is_available:
                print(f"{vehicle.brand} {vehicle.model}")
                
# Crear vehiculos
car1 = Car("Kia", "Picanto", 20000)
bike1 = Bike("Yamaha", "YZF-R3", 5000)
truck1 = Truck("Volvo", "FH16", 120000)
avion1 = Avion("Boeing", "747", 300000000)

# Crear concesionario
dealership = Dealership()

# Agregar vehiculos al concesionario
dealership.add_vehicle(car1)
dealership.add_vehicle(bike1)
dealership.add_vehicle(truck1)
dealership.add_vehicle(avion1)

# Mostrar vehiculos disponibles
dealership.show_available_vehicles()

# Crear cliente
customer1 = Customer("Diego")

# Registrar cliente en el concesionario
dealership.register_customer(customer1)

# Cliente compra un vehiculo
customer1.buy_vehicle(car1)

# Mostrar vehiculos disponibles despues de la compra
dealership.show_available_vehicles()


customer1.inquire_vehicle(avion1)
customer1.buy_vehicle(avion1)

# PILARES DE POO: Abstracción, Encapsulamiento, Herencia, Polimorfismo.