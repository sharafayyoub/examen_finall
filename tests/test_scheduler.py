from src.proceso import Proceso
from src.scheduler_fcfs import FCFSScheduler
from src.scheduler_rr import RoundRobinScheduler

def test_fcfs_scheduler():
    procesos = [Proceso(pid="P1", duracion=5, prioridad=1), Proceso(pid="P2", duracion=3, prioridad=2)]
    scheduler = FCFSScheduler()
    gantt = scheduler.planificar(procesos)
    assert gantt == [("P1", 0, 5), ("P2", 5, 8)]

def test_round_robin_scheduler():
    procesos = [Proceso(pid="P1", duracion=5, prioridad=1), Proceso(pid="P2", duracion=3, prioridad=2)]
    scheduler = RoundRobinScheduler(quantum=2)
    gantt = scheduler.planificar(procesos)
    assert gantt == [("P1", 0, 2), ("P2", 2, 4), ("P1", 4, 6), ("P2", 6, 7), ("P1", 7, 8)]
