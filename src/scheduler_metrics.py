from typing import List, Dict
from src.proceso import Proceso
from src.scheduler import GanttEntry

def calcular_metricas(procesos: List[Proceso], gantt: List[GanttEntry]) -> Dict[str, float]:
    """
    Calcula métricas de tiempo de respuesta, retorno y espera.
    :param procesos: Lista de objetos Proceso.
    :param gantt: Lista de GanttEntry representando el diagrama de Gantt.
    :return: Diccionario con métricas promedio.
    """
    tiempos_respuesta = []
    tiempos_retorno = []
    tiempos_espera = []

    for proceso in procesos:
        tiempo_respuesta = proceso.tiempo_inicio - proceso.tiempo_llegada
        tiempo_retorno = proceso.tiempo_fin - proceso.tiempo_llegada
        tiempo_espera = tiempo_retorno - proceso.duracion

        tiempos_respuesta.append(tiempo_respuesta)
        tiempos_retorno.append(tiempo_retorno)
        tiempos_espera.append(tiempo_espera)

    return {
        "tiempo_respuesta_promedio": sum(tiempos_respuesta) / len(tiempos_respuesta),
        "tiempo_retorno_promedio": sum(tiempos_retorno) / len(tiempos_retorno),
        "tiempo_espera_promedio": sum(tiempos_espera) / len(tiempos_espera),
    }

def imprimir_diagrama_gantt(gantt: List[GanttEntry]) -> None:
    """
    Imprime el diagrama de Gantt en formato legible.
    :param gantt: Lista de GanttEntry representando el diagrama de Gantt.
    """
    print("Diagrama de Gantt:")
    for pid, tiempo_inicio, tiempo_fin in gantt:
        print(f"Proceso {pid}: Inicio = {tiempo_inicio}, Fin = {tiempo_fin}")
