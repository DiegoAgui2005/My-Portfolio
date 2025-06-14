def add(a,b):
    return a+b
def substract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def calculator():
    while True:
        print("Seleccione una operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División") 
        print("5. Salir")
        
        option = int(input("Ingresa una opción: (1,2,3,4,5) "))
        
        if option == 5:
            print("Saliendo de la calculadora")
            
        if option in [1,2,3,4]:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
            if option == 1:
                print("Resultado: ", add(num1,num2))
            elif option == 2:
                print("Resultado: ", substract(num1,num2))
            elif option == 3:
                print("Resultado: ", multiply(num1,num2))
            elif option == 4:
                print("Resultado: ", divide(num1,num2))	
        else:
            print("Opción no válida, intenta de nuevo")
            break
        
calculator()