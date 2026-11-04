import threading
import time
import random

condicion = threading.Condition()

class Cita:
    def paciente(self, nombre):
        print(f"El paciente {nombre} está esperando una cita.")
        print(f"{nombre} tiene su cita.")

    def doctor(self, nombre, especialidad):
        print(f"{nombre}, de {especialidad}, está consultando su agenda")
        time.sleep(1)
        hora = random.randint(8, 13)
        print("Agenda comprobada")
        print(f"La hora de la cita es {hora}")


cita = Cita()

threading.Thread(target=cita.paciente, args=("Pepe Pérez",)).start()
threading.Thread(target=cita.doctor, args=("Dr. Juan Gómez", "Traumatología")).start()