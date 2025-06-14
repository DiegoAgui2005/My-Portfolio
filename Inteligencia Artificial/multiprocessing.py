import multiprocessing

def calcular_cuadrado(numeros, cola):
    for n in numeros:
        cola.put(n * n)

if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")  # ✅ Explicitly set the method for Windows

    numeros = [2, 3, 5]
    cola = multiprocessing.Queue()
    
    proceso = multiprocessing.Process(target=calcular_cuadrado, args=(numeros, cola))
    
    proceso.start()
    proceso.join()

    while not cola.empty():
        print(cola.get())  # Expected output: 4, 9, 25
