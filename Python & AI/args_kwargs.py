class Venta:
    def __init__(self, *args, **kwargs):
        self.prices = args
        self.discounts = kwargs

    def calcular_total(self) -> int:
        print("Calculando totales")
        if self.discounts: #comprobamos si un descuento fue pasado como kwarg
            for key, value in self.discounts.items(): #iteramos las claves y valores del diccionario kwarg
                discount = value #asignamos el valor encontrado en 'value' a discount
            return print(f"La suma total aplicando un descuento del {discount} % es: {sum(self.prices) * ((100 - discount) / 100)}")
        else:
            return print(f"La suma de total es: {sum(self.prices)}") #retornamos la suma de los 'args' si no hay descuento.

venta1 = Venta(200,300,400, discount=10)
venta2 = Venta(800,200)
venta1.calcular_total()
venta2.calcular_total()