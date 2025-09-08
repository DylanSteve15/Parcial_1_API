# main.py
from config.database import Base, engine, SessionLocal
from models.horario_model import Estudiante, Horario

def inicializar_bd():
    """
    Crea todas las tablas definidas en los modelos dentro de la base de datos.
    Si el archivo horarios.db no existe, lo genera automáticamente.
    """
    print("🔄 Creando base de datos y tablas...")
    Base.metadata.create_all(bind=engine)
    print("✅ Base de datos y tablas listas.")

if __name__ == "__main__":
    inicializar_bd()

    # Probar conexión creando una sesión
    db = SessionLocal()
    try:
        print("📡 Conexión exitosa a la base de datos.")
    finally:
        db.close()
