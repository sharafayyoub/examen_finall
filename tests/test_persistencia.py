import os
from src.proceso import Proceso
from src.repositorio_procesos import RepositorioProcesos

def test_guardar_y_cargar_json(tmp_path):
    repo = RepositorioProcesos()
    repo.agregar_proceso(Proceso(pid="P1", duracion=5, prioridad=1))
    filepath = os.path.join(tmp_path, "procesos.json")
    repo.guardar_json(filepath)

    nuevo_repo = RepositorioProcesos()
    nuevo_repo.cargar_json(filepath)
    assert len(nuevo_repo.listar_procesos()) == 1
    assert nuevo_repo.obtener_proceso("P1").duracion == 5

def test_guardar_y_cargar_csv(tmp_path):
    repo = RepositorioProcesos()
    repo.agregar_proceso(Proceso(pid="P1", duracion=5, prioridad=1))
    filepath = os.path.join(tmp_path, "procesos.csv")
    repo.guardar_csv(filepath)

    nuevo_repo = RepositorioProcesos()
    nuevo_repo.cargar_csv(filepath)
    assert len(nuevo_repo.listar_procesos()) == 1
    assert nuevo_repo.obtener_proceso("P1").duracion == 5
