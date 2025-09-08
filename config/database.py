# config/database.py
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Ruta a la base de datos SQLite
RUTA_BD = "sqlite:///horarios.db"

# Crear el motor de conexión (engine)
engine = create_engine(RUTA_BD, echo=True)

# Crear la clase base para los modelos
Base = declarative_base()

# Crear una fábrica de sesiones
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
