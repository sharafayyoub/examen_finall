from typing import List
from src.scheduler import Scheduler, GanttEntry
from src.proceso import Proceso

class FCFSScheduler(Scheduler):
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        """
        Planifica los procesos según el algoritmo FCFS.
        :param procesos: Lista de objetos Proceso a planificar.
        :return: Lista de GanttEntry representando el diagrama de Gantt.
        """
        tiempo_actual = 0
        gantt = []

        for proceso in procesos:
            tiempo_inicio = tiempo_actual
            tiempo_fin = tiempo_inicio + proceso.duracion
            gantt.append((proceso.pid, tiempo_inicio, tiempo_fin))
            tiempo_actual = tiempo_fin

            # Actualizar atributos del proceso
            proceso.tiempo_inicio = tiempo_inicio
            proceso.tiempo_fin = tiempo_fin

        return gantt
