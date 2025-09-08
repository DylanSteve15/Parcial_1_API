# repositories/horario_repository.py
from sqlalchemy.orm import Session
from models.horario_model import Estudiante, Horario


# ----------------------------
# CRUD Estudiante
# ----------------------------

def crear_estudiante(db: Session, nombre: str, carrera: str):
    nuevo_estudiante = Estudiante(nombre=nombre, carrera=carrera)
    db.add(nuevo_estudiante)
    db.commit()
    db.refresh(nuevo_estudiante)
    return nuevo_estudiante


def obtener_estudiantes(db: Session):
    return db.query(Estudiante).all()


def actualizar_estudiante(db: Session, estudiante_id: int, nombre: str = None, carrera: str = None):
    estudiante = db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
    if estudiante:
        if nombre:
            estudiante.nombre = nombre
        if carrera:
            estudiante.carrera = carrera
        db.commit()
        db.refresh(estudiante)
    return estudiante


def eliminar_estudiante(db: Session, estudiante_id: int):
    estudiante = db.query(Estudiante).filter(Estudiante.id == estudiante_id).first()
    if estudiante:
        db.delete(estudiante)
        db.commit()
    return estudiante


# ----------------------------
# CRUD Horario
# ----------------------------

def crear_horario(db: Session, materia: str, dia: str, hora: str, estudiante_id: int):
    nuevo_horario = Horario(materia=materia, dia=dia, hora=hora, estudiante_id=estudiante_id)
    db.add(nuevo_horario)
    db.commit()
    db.refresh(nuevo_horario)
    return nuevo_horario


def obtener_horarios(db: Session):
    return db.query(Horario).all()


def actualizar_horario(db: Session, horario_id: int, materia: str = None, dia: str = None, hora: str = None):
    horario = db.query(Horario).filter(Horario.id == horario_id).first()
    if horario:
        if materia:
            horario.materia = materia
        if dia:
            horario.dia = dia
        if hora:
            horario.hora = hora
        db.commit()
        db.refresh(horario)
    return horario


def eliminar_horario(db: Session, horario_id: int):
    horario = db.query(Horario).filter(Horario.id == horario_id).first()
    if horario:
        db.delete(horario)
        db.commit()
    return horario
