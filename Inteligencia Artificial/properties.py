class Product:
    def __init__(self, name: str, stock: int, price: int):
        self.name = name
        self._stock = stock
        self._price = price

    @property
    def stock(self):
        return self._stock
    
    @property
    def price(self):
        return self._price
    
    @stock.setter
    def stock(self, new_stock: int):
        if new_stock < 0:
            raise ValueError("Stock cannot be negative")
        self._stock = new_stock

    @price.setter
    def price(self, new_price: int):
        if new_price < 0:
            raise ValueError("Price need to be a possitive number")
        self._price = new_price

    @stock.deleter
    def stock(self):
        print(f"Stock of '{self.name}' product has been deleted")
        del self._stock

    @price.deleter
    def price(self):
        print(f"Price of '{self.name}' product has been deleted.")
        del self._price

    def print_info(self):
        print(f"Producto: {self.name} - Stock: {self.stock if hasattr(self, '_stock') else 'N/A'} - $ {self.price if hasattr(self, '_price') else 'N/A'}")

#crear instancia de producto
producto1 = Product("Harina",4,1000)
producto1.print_info()

#modificar stock, precio y nombre de producto controladamente
producto1.stock = 6
producto1.price = 1200
producto1.name = "Arroz"
producto1.print_info()

#intentar establecer stock o precio negativo
#producto1.stock = -6
#producto1.price = -600

#Eliminar un stock y un precio
del producto1.stock
del producto1.price
producto1.print_info()