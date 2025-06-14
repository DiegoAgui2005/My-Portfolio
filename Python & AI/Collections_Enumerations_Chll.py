from enum import Enum
from collections import defaultdict

class Frutas(Enum):
  MANZANA = 1
  PERA = 2
  CIRUELA = 3
  NANCE = 4
  NARANJA = 5
  UVA = 6
  KIWI = 7
  BANANA = 8

class Pedido(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3

class Fruteria:
    def __init__(self):
        self.stock = defaultdict(int)
        self.pedido: Pedido = None

    def añadir_fruta(self, fruta:Frutas, cantidad):
        if not isinstance(fruta, Frutas):
            raise ValueError("La fruta debe ser una instancia de la clase Frutas") 
        if cantidad <=0:
            raise ValueError("La cantidad debe ser un numero positivo")
        self.stock[fruta] += cantidad

    def contar_frutas(self) -> defaultdict:
        if not self.stock:
            return "No hay frutas en la frutería."
        lista_frutas = ""
        for fruta, cantidad in self.stock.items():
            lista_frutas += f"- {fruta}: {cantidad}\n"
        return lista_frutas.strip() # Se imprime con strip para evitar el ultimo salto de linea

    def fruta_no_disponible(self, fruta:Frutas):
        return fruta not in self.stock or self.stock[fruta] <= 0

    def hacer_pedido_de_fruta(self, fruta:Frutas, cantidad):
        if not isinstance(fruta, Frutas):
            raise ValueError("La fruta debe ser una instancia de la clase Frutas") 
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser un numero positivo") 

        if self.fruta_no_disponible(fruta):
            return f"No nos queda {fruta.name}"
        
        if self.pedido is None or self.pedido == Pedido.ENTREGADO:
            if self.stock[fruta] < cantidad:
               return f"No hay suficiente stock de {fruta.name}. Solo quedan {self.stock[fruta]} unidades."

            self.pedido = Pedido.PENDIENTE
            self.stock[fruta] -= cantidad  

            if self.stock[fruta] == 0:
                del self.stock[fruta]

            return f"Su pedido de {cantidad} {fruta.name}(s) se está realizando."
        else:
            return "Ahora mismo estamos haciendo un pedido, vuelva más tarde."         

    def avanzar_pedido(self):
        if self.pedido is None:
            return "No hay pedidos por el momento."
        elif self.pedido == Pedido.ENTREGADO:
            return "El pedido ya ah sido entregado, inicie otro"
        elif self.pedido == Pedido.PENDIENTE:
            self.pedido = Pedido.ENVIADO
            return "Su paquete sera enviado pronto."
        elif self.pedido == Pedido.ENVIADO:
            self.pedido = Pedido.ENTREGADO
            return "Su paquete sera entregado pronto"

    def chequear_pedido(self):
        if self.pedido is None:
            return "No hay ningun pedido"
        else: 
            return f"El estado de su pedido es: {self.pedido.name}"