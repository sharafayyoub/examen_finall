import json
import csv
from typing import List, Optional
from src.proceso import Proceso

class RepositorioProcesos:
    def __init__(self):
        self.procesos = {}

    def agregar_proceso(self, proceso: Proceso) -> None:
        """
        Agrega un proceso al repositorio, verificando que el PID sea único.
        :param proceso: Objeto Proceso a agregar.
        """
        if proceso.pid in self.procesos:
            raise ValueError(f"Ya existe un proceso con el PID '{proceso.pid}'.")
        self.procesos[proceso.pid] = proceso

    def listar_procesos(self) -> List[Proceso]:
        """
        Retorna una lista de todos los procesos registrados.
        :return: Lista de objetos Proceso.
        """
        return list(self.procesos.values())

    def eliminar_proceso(self, pid: str) -> None:
        """
        Elimina un proceso del repositorio dado su PID.
        :param pid: Identificador único del proceso a eliminar.
        """
        if pid not in self.procesos:
            raise ValueError(f"No se encontró un proceso con el PID '{pid}'.")
        del self.procesos[pid]

    def obtener_proceso(self, pid: str) -> Optional[Proceso]:
        """
        Obtiene un proceso dado su PID.
        :param pid: Identificador único del proceso.
        :return: Objeto Proceso o None si no existe.
        """
        return self.procesos.get(pid)

    def guardar_json(self, filepath: str) -> None:
        """
        Guarda los procesos en un archivo JSON.
        :param filepath: Ruta del archivo JSON.
        """
        with open(filepath, 'w') as file:
            json.dump([proceso.__dict__ for proceso in self.procesos.values()], file)

    def cargar_json(self, filepath: str) -> None:
        """
        Carga los procesos desde un archivo JSON, reemplazando los existentes.
        :param filepath: Ruta del archivo JSON.
        """
        with open(filepath, 'r') as file:
            procesos_data = json.load(file)
        self.procesos = {data['pid']: Proceso(**data) for data in procesos_data}

    def guardar_csv(self, filepath: str) -> None:
        """
        Guarda los procesos en un archivo CSV.
        :param filepath: Ruta del archivo CSV.
        """
        with open(filepath, 'w', newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['pid', 'duracion', 'prioridad', 'tiempo_restante', 'tiempo_llegada', 'tiempo_inicio', 'tiempo_fin'])
            for proceso in self.procesos.values():
                writer.writerow([proceso.pid, proceso.duracion, proceso.prioridad, proceso.tiempo_restante, 
                                 proceso.tiempo_llegada, proceso.tiempo_inicio, proceso.tiempo_fin])

    def cargar_csv(self, filepath: str) -> None:
        """
        Carga los procesos desde un archivo CSV, reemplazando los existentes.
        :param filepath: Ruta del archivo CSV.
        """
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file, delimiter=';')
            self.procesos = {}
            for row in reader:
                self.procesos[row['pid']] = Proceso(
                    pid=row['pid'],
                    duracion=int(row['duracion']),
                    prioridad=int(row['prioridad'])
                )
                # Actualizar atributos adicionales
                self.procesos[row['pid']].tiempo_restante = int(row['tiempo_restante'])
                self.procesos[row['pid']].tiempo_llegada = int(row['tiempo_llegada'])
                self.procesos[row['pid']].tiempo_inicio = int(row['tiempo_inicio']) if row['tiempo_inicio'] != 'None' else None
                self.procesos[row['pid']].tiempo_fin = int(row['tiempo_fin']) if row['tiempo_fin'] != 'None' else None
