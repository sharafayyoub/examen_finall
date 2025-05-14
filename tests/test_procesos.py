import pytest
from src.proceso import Proceso

def test_creacion_proceso_valido():
    proceso = Proceso(pid="P1", duracion=10, prioridad=1)
    assert proceso.pid == "P1"
    assert proceso.duracion == 10
    assert proceso.prioridad == 1

def test_pid_duplicado():
    Proceso.procesos_existentes.clear()
    Proceso(pid="P1", duracion=10, prioridad=1)
    with pytest.raises(ValueError, match="El PID debe ser único y no vacío."):
        Proceso(pid="P1", duracion=5, prioridad=2)

def test_duracion_invalida():
    with pytest.raises(ValueError, match="La duración debe ser un entero positivo."):
        Proceso(pid="P2", duracion=0, prioridad=1)

def test_prioridad_invalida():
    with pytest.raises(ValueError, match="La prioridad debe ser un entero."):
        Proceso(pid="P3", duracion=10, prioridad="alta")
