#!/bin/bash

BASE_URL="http://127.0.0.1:5000/api"

echo "============================"
echo "📌 INICIANDO PRUEBAS API"
echo "============================"

# === 1. Crear estudiantes ===
echo "📌 Creando estudiantes..."
curl -s -X POST -H "Content-Type: application/json" \
-d '{"nombre":"Dylan Rodriguez","carrera":"Ingeniería de Sistemas"}' \
$BASE_URL/estudiantes
echo -e "\n---"

curl -s -X POST -H "Content-Type: application/json" \
-d '{"nombre":"Jose Luis Martinez","carrera":"Big Data"}' \
$BASE_URL/estudiantes
echo -e "\n---"

curl -s -X POST -H "Content-Type: application/json" \
-d '{"nombre":"Juan Sebastian Pinzon","carrera":"Deportes"}' \
$BASE_URL/estudiantes
echo -e "\n============================\n"

# === 2. Listar estudiantes ===
echo "📌 Listando estudiantes..."
curl -s $BASE_URL/estudiantes
echo -e "\n============================\n"

# === 3. Buscar estudiante por ID (ejemplo: 1) ===
echo "📌 Buscando estudiante con ID=1..."
curl -s $BASE_URL/estudiantes/1
echo -e "\n============================\n"

# === 4. Crear horarios para estudiantes ===
echo "📌 Creando horarios..."
curl -s -X POST -H "Content-Type: application/json" \
-d '{"materia":"Desarrollo Web","dia":"Lunes","hora":"08:00-10:00","estudiante_id":1}' \
$BASE_URL/horarios
echo -e "\n---"

curl -s -X POST -H "Content-Type: application/json" \
-d '{"materia":"Big Data","dia":"Martes","hora":"09:00-12:00","estudiante_id":2}' \
$BASE_URL/horarios
echo -e "\n---"

curl -s -X POST -H "Content-Type: application/json" \
-d '{"materia":"Futbol","dia":"Viernes","hora":"14:00-16:00","estudiante_id":3}' \
$BASE_URL/horarios
echo -e "\n============================\n"

# === 5. Listar todos los horarios ===
echo "📌 Listando todos los horarios..."
curl -s $BASE_URL/horarios
echo -e "\n============================\n"

# === 6. Buscar horario por ID (ejemplo: 1) ===
echo "📌 Buscando horario con ID=1..."
curl -s $BASE_URL/horarios/1
echo -e "\n============================\n"

# === 7. Eliminar estudiante por ID (ejemplo: 1) ===
echo "📌 Eliminando estudiante con ID=1..."
curl -s -X DELETE $BASE_URL/estudiantes/1
echo -e "\n============================\n"

# === 8. Listar estudiantes después de eliminar ===
echo "📌 Estudiantes después de eliminar:"
curl -s $BASE_URL/estudiantes
echo -e "\n============================\n"

# === 9. Listar horarios después de eliminar estudiante (cascada) ===
echo "📌 Horarios después de eliminar estudiante 1:"
curl -s $BASE_URL/horarios
echo -e "\n============================\n"

echo "✅ PRUEBAS TERMINADAS"
