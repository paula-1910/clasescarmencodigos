import threading
import queue
import time
import random

# Número de asistentes y porteros
num_asistentes = 20
num_porteros = 2

# Diccionario de usuarios
usuarios_concierto = {
    f"TICKET-{i:03d}": f"Asistente_{i}"
    for i in range(1, num_asistentes + 1)
}

# Cola FIFO
cola = queue.Queue()

# Añadir usuarios a la cola
for entrada, usuario in usuarios_concierto.items():
    cola.put((entrada, usuario))

# Diccionario para contar entradas por portero
entradas_porteros = {}
lock = threading.Lock()


# Función de los porteros
def portero(nombre):
    contador = 0

    while True:
        try:
            entrada, usuario = cola.get_nowait()
        except queue.Empty:
            break

        print(f"{nombre} está comprobando la entrada {entrada} de {usuario}")

        time.sleep(random.uniform(0.5, 1.5))

        print(f"{nombre} permite el acceso a {usuario}")

        contador += 1
        cola.task_done()

    with lock:
        entradas_porteros[nombre] = contador


# Crear hilos de porteros
hilos = []

for i in range(1, num_porteros + 1):
    hilo = threading.Thread(
        target=portero,
        args=(f"Portero_{i}",)
    )
    hilos.append(hilo)
    hilo.start()

# Esperar a que terminen todos los hilos
for hilo in hilos:
    hilo.join()

# Mostrar resultados
print("\n--- RESULTADOS ---")

for portero, cantidad in entradas_porteros.items():
    print(f"{portero} ha gestionado {cantidad} entradas")

print(f"Total de entradas gestionadas: {sum(entradas_porteros.values())}")