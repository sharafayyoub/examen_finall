from typing import List
from src.scheduler import Scheduler, GanttEntry
from src.proceso import Proceso

class RoundRobinScheduler(Scheduler):
    def __init__(self, quantum: int):
        if quantum <= 0:
            raise ValueError("El quantum debe ser un entero positivo.")
        self.quantum = quantum

    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        """
        Planifica los procesos según el algoritmo Round-Robin.
        :param procesos: Lista de objetos Proceso a planificar.
        :return: Lista de GanttEntry representando el diagrama de Gantt.
        """
        tiempo_actual = 0
        gantt = []
        cola = procesos[:]  # Copia de la lista de procesos

        while cola:
            proceso = cola.pop(0)
            tiempo_inicio = tiempo_actual
            tiempo_ejecutado = min(proceso.tiempo_restante, self.quantum)
            tiempo_actual += tiempo_ejecutado
            proceso.tiempo_restante -= tiempo_ejecutado
            gantt.append((proceso.pid, tiempo_inicio, tiempo_actual))

            # Si el proceso no ha terminado, vuelve a la cola
            if proceso.tiempo_restante > 0:
                cola.append(proceso)
            else:
                # Actualizar atributos del proceso terminado
                proceso.tiempo_inicio = proceso.tiempo_inicio or tiempo_inicio
                proceso.tiempo_fin = tiempo_actual

        return gantt
