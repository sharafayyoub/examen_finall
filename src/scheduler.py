from abc import ABC, abstractmethod
from typing import List, Tuple
from src.proceso import Proceso

GanttEntry = Tuple[str, int, int]  # Definición de GanttEntry como una tupla (pid, tiempo_inicio, tiempo_fin)

class Scheduler(ABC):
    @abstractmethod
    def planificar(self, procesos: List[Proceso]) -> List[GanttEntry]:
        """
        Método abstracto para planificar la ejecución de procesos.
        :param procesos: Lista de objetos Proceso a planificar.
        :return: Lista de GanttEntry representando el diagrama de Gantt.
        """
        pass
