"""
Actividad.
1. Crea un metodo estatico para verificar si el monto de un pedido es mayor a un minimo permitido (por ejemplo, $50)
2. Crea un metodo de clase que permita crear un pedido aplicando un descuento global.
"""
class Order:
    global_discount = 10
    
    def __init__(self, amount):
        self.amount = amount
        
    @staticmethod
    def validate_order_amount(amount):
        """
        Verifica si el monto del pedido es mayor al mínimo permitido
        """
        min_amount = 50
        if amount < min_amount:
            return False, f"El monto mínimo de pedido debe ser ${min_amount}"
        return True, "Monto de pedido válido"
    
    @classmethod
    def create_with_discount(cls, amount):
        """
        Crea un pedido aplicando el descuento global
        """
        discounted_amount = amount * (1 - cls.global_discount / 100)
        return cls(discounted_amount)
    
    def __str__(self):
        return f"Pedido por ${self.amount:.2f}"

# Verificar si un monto es válido
is_valid, message = Order.validate_order_amount(30)
print(f"{is_valid}: {message}")

is_valid, message = Order.validate_order_amount(75)
print(f"{is_valid}: {message}")

# Crear pedido con descuento global
Order.global_discount = 15
order = Order.create_with_discount(100)
print(order)  # Debería mostrar el monto con 15% de descuento