# models/horario_model.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.database import Base

"""
La clase Estudiante representa a un alumno dentro del sistema.
Cada estudiante tiene un identificador único, un nombre y una carrera.
Además, se relaciona con la tabla de horarios para ver qué clases tiene asignadas.
"""
class Estudiante(Base):
    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False, index=True)
    carrera = Column(String(255), nullable=False)

    # Relación con la tabla Horario
    horarios = relationship("Horario", back_populates="estudiante", cascade="all, delete-orphan")


"""
La clase Horario representa una materia inscrita por un estudiante en un día y hora específicos.
Cada horario pertenece a un único estudiante mediante una clave foránea.
"""
class Horario(Base):
    __tablename__ = "horarios"

    id = Column(Integer, primary_key=True, index=True)
    materia = Column(String(255), nullable=False)
    dia = Column(String(50), nullable=False, index=True)   # Ejemplo: "Lunes"
    hora = Column(String(50), nullable=False)              # Ejemplo: "08:00 AM"

    estudiante_id = Column(Integer, ForeignKey("estudiantes.id"))

    # Relación inversa con Estudiante
    estudiante = relationship("Estudiante", back_populates="horarios")
