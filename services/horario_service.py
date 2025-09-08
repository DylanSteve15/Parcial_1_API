# services/horario_service.py
from sqlalchemy.orm import Session
from repositories import horario_repository


# ----------------------------
# Estudiantes
# ----------------------------

def crear_estudiante(db: Session, nombre: str, carrera: str):
    if not nombre or not carrera:
        raise ValueError("El nombre y la carrera son obligatorios")
    return horario_repository.crear_estudiante(db, nombre, carrera)


def listar_estudiantes(db: Session):
    return horario_repository.obtener_estudiantes(db)


def actualizar_estudiante(db: Session, estudiante_id: int, nombre: str = None, carrera: str = None):
    estudiante = horario_repository.actualizar_estudiante(db, estudiante_id, nombre, carrera)
    if not estudiante:
        raise ValueError(f"El estudiante con id {estudiante_id} no existe")
    return estudiante


def eliminar_estudiante(db: Session, estudiante_id: int):
    estudiante = horario_repository.eliminar_estudiante(db, estudiante_id)
    if not estudiante:
        raise ValueError(f"El estudiante con id {estudiante_id} no existe")
    return estudiante


# ----------------------------
# Horarios
# ----------------------------

def crear_horario(db: Session, materia: str, dia: str, hora: str, estudiante_id: int):
    if not materia or not dia or not hora:
        raise ValueError("Materia, día y hora son obligatorios")
    return horario_repository.crear_horario(db, materia, dia, hora, estudiante_id)


def listar_horarios(db: Session):
    return horario_repository.obtener_horarios(db)


def actualizar_horario(db: Session, horario_id: int, materia: str = None, dia: str = None, hora: str = None):
    horario = horario_repository.actualizar_horario(db, horario_id, materia, dia, hora)
    if not horario:
        raise ValueError(f"El horario con id {horario_id} no existe")
    return horario


def eliminar_horario(db: Session, horario_id: int):
    horario = horario_repository.eliminar_horario(db, horario_id)
    if not horario:
        raise ValueError(f"El horario con id {horario_id} no existe")
    return horario
