# controllers/horario_controller.py
from flask import Blueprint, request, jsonify
from config.database import SessionLocal
from services import horario_service

horario_bp = Blueprint("horario", __name__, url_prefix="/api")


# ----------------------------
# Estudiantes
# ----------------------------

@horario_bp.route("/estudiantes", methods=["POST"])
def crear_estudiante():
    db = SessionLocal()
    data = request.get_json()
    try:
        estudiante = horario_service.crear_estudiante(db, data["nombre"], data["carrera"])
        return jsonify({"message": "Estudiante creado", "data": {
            "id": estudiante.id, "nombre": estudiante.nombre, "carrera": estudiante.carrera
        }}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()


@horario_bp.route("/estudiantes", methods=["GET"])
def listar_estudiantes():
    db = SessionLocal()
    estudiantes = horario_service.listar_estudiantes(db)
    db.close()
    return jsonify([{"id": e.id, "nombre": e.nombre, "carrera": e.carrera} for e in estudiantes])


@horario_bp.route("/estudiantes/<int:estudiante_id>", methods=["PUT"])
def actualizar_estudiante(estudiante_id):
    db = SessionLocal()
    data = request.get_json()
    try:
        estudiante = horario_service.actualizar_estudiante(
            db, estudiante_id, data.get("nombre"), data.get("carrera")
        )
        return jsonify({"message": "Estudiante actualizado", "data": {
            "id": estudiante.id, "nombre": estudiante.nombre, "carrera": estudiante.carrera
        }})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()


@horario_bp.route("/estudiantes/<int:estudiante_id>", methods=["DELETE"])
def eliminar_estudiante(estudiante_id):
    db = SessionLocal()
    try:
        horario_service.eliminar_estudiante(db, estudiante_id)
        return jsonify({"message": "Estudiante eliminado"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()


# ----------------------------
# Horarios
# ----------------------------

@horario_bp.route("/horarios", methods=["POST"])
def crear_horario():
    db = SessionLocal()
    data = request.get_json()
    try:
        horario = horario_service.crear_horario(
            db, data["materia"], data["dia"], data["hora"], data["estudiante_id"]
        )
        return jsonify({"message": "Horario creado", "data": {
            "id": horario.id, "materia": horario.materia, "dia": horario.dia, "hora": horario.hora,
            "estudiante_id": horario.estudiante_id
        }}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()


@horario_bp.route("/horarios", methods=["GET"])
def listar_horarios():
    db = SessionLocal()
    horarios = horario_service.listar_horarios(db)
    db.close()
    return jsonify([{
        "id": h.id, "materia": h.materia, "dia": h.dia, "hora": h.hora, "estudiante_id": h.estudiante_id
    } for h in horarios])


@horario_bp.route("/horarios/<int:horario_id>", methods=["PUT"])
def actualizar_horario(horario_id):
    db = SessionLocal()
    data = request.get_json()
    try:
        horario = horario_service.actualizar_horario(
            db, horario_id, data.get("materia"), data.get("dia"), data.get("hora")
        )
        return jsonify({"message": "Horario actualizado", "data": {
            "id": horario.id, "materia": horario.materia, "dia": horario.dia, "hora": horario.hora,
            "estudiante_id": horario.estudiante_id
        }})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()


@horario_bp.route("/horarios/<int:horario_id>", methods=["DELETE"])
def eliminar_horario(horario_id):
    db = SessionLocal()
    try:
        horario_service.eliminar_horario(db, horario_id)
        return jsonify({"message": "Horario eliminado"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
    finally:
        db.close()
