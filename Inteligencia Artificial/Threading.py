import threading

saldo = 0
lock = threading.Lock()  # 'Lock()' should be capitalized

def depositar(dinero):
    global saldo
    for _ in range(100000):
        with lock:  # Ensuring thread safety
            saldo += dinero

hilos = []
for _ in range(2):
    hilo = threading.Thread(target=depositar, args=(1,))  # Fix 'targe' -> 'target'
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print(f"Saldo final: {saldo}")
