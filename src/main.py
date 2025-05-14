import argparse
import sys
import os

# Asegurar que el directorio src esté en el PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.proceso import Proceso
from src.repositorio_procesos import RepositorioProcesos
from src.scheduler_fcfs import FCFSScheduler
from src.scheduler_rr import RoundRobinScheduler
from src.scheduler_metrics import calcular_metricas, imprimir_diagrama_gantt

def main():
    parser = argparse.ArgumentParser(description="Simulador de planificación de procesos.")
    parser.add_argument("--algoritmo", choices=["fcfs", "rr"], required=True, help="Algoritmo de planificación (fcfs o rr).")
    parser.add_argument("--quantum", type=int, help="Quantum para Round-Robin (requerido si se usa rr).")
    parser.add_argument("--archivo", required=True, help="Archivo CSV o JSON con los procesos.")
    parser.add_argument("--formato", choices=["csv", "json"], required=True, help="Formato del archivo (csv o json).")
    args = parser.parse_args()

    # Cargar procesos
    print("Cargando procesos...")
    repo = RepositorioProcesos()
    if args.formato == "csv":
        repo.cargar_csv(args.archivo)
    else:
        repo.cargar_json(args.archivo)

    procesos = repo.listar_procesos()
    print(f"Procesos cargados: {procesos}")

    # Seleccionar algoritmo
    print(f"Seleccionando algoritmo: {args.algoritmo}")
    if args.algoritmo == "fcfs":
        scheduler = FCFSScheduler()
    elif args.algoritmo == "rr":
        if not args.quantum:
            raise ValueError("El quantum es obligatorio para el algoritmo Round-Robin.")
        scheduler = RoundRobinScheduler(quantum=args.quantum)

    # Planificar y calcular métricas
    print("Planificando procesos...")
    gantt = scheduler.planificar(procesos)
    imprimir_diagrama_gantt(gantt)
    metricas = calcular_metricas(procesos, gantt)

    # Mostrar métricas
    print("\nMétricas:")
    for key, value in metricas.items():
        print(f"{key}: {value:.2f}")

if __name__ == "__main__":
    main()
