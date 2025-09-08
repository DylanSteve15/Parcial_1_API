# main.py
from flask import Flask
from controllers.horario_controller import horario_bp
from config.database import Base, engine

def inicializar_bd():
    """
    Crea las tablas en la base de datos si no existen.
    """
    print("🔄 Creando base de datos y tablas...")
    Base.metadata.create_all(bind=engine)
    print("✅ Base de datos y tablas listas.")

app = Flask(__name__)
app.register_blueprint(horario_bp)

if __name__ == "__main__":
    inicializar_bd()
    app.run(debug=True)
