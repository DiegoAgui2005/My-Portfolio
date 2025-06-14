def numeros_impares(limite):
    a = 1
    while a < limite:
        yield a
        a += 2

def numeros_pares(limite):
    a = 0
    while a < limite:
        yield a
        a += 2        

print("\nNumeros Impares\n")

for num in numeros_impares(20):
    print(num)

print("\nNumeros pares\n")

for num in numeros_pares(20):
    print(num)