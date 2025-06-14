try:
    divisor = int(input("Ingresa un número divisor:"))
    result = 100/divisor
    print(result)
except ZeroDivisionError as e:
    print("Error, El divisor no puede ser cero")
    print("Ha ocurrido un error: ", e)
except ValueError as e:
    print("Error, Debes ingresar un número")
    print("Ha ocurrido un error: ", e)