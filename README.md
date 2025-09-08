
# CRUDRESTAPI - Horarios
**Python** | **Flask** | **SQLite**

Este proyecto es una **API RESTful** desarrollada en Python usando **Flask**, diseñada para gestionar información de horarios académicos.  
Los datos se almacenan en una base de datos SQLite (a través de SQLAlchemy) y la API permite realizar operaciones **CRUD** sobre los horarios.

---

## 📂 Estructura del Proyecto

```
src/
│── app.py                   # Punto de entrada de la aplicación Flask
│
├── config/
│   └── database.py          # Configuración de la base de datos SQLite con SQLAlchemy
│
├── models/
│   └── horario.py           # Modelo de datos del horario
│
├── repositories/
│   └── horario_repository.py # Acceso a datos y funciones CRUD
│
├── services/
│   └── horario_service.py   # Lógica de negocio y reglas de validación
│
└── controllers/
    └── horario_controller.py # Endpoints de la API (Flask)
```

Adicionalmente:  
- `requirements.txt`: Lista de dependencias necesarias para ejecutar el proyecto.  
- `curl_examples.sh`: Ejemplos de comandos **curl** para probar la API.  

---

## 🚀 Endpoints disponibles

### Obtener todos los horarios
```http
GET /api/horarios
```

### Obtener un horario por ID
```http
GET /api/horarios/<id>
```

### Crear un nuevo horario
```http
POST /api/horarios
```
**Cuerpo (JSON):**
```json
{
  "materia": "Programación Web",
  "dia": "Lunes",
  "hora": "08:00",
  "estudiante_id": 1
}
```

### Actualizar un horario existente
```http
PUT /api/horarios/<id>
```
**Cuerpo (JSON):**
```json
{
  "materia": "Bases de Datos",
  "dia": "Martes",
  "hora": "10:00"
}
```

### Eliminar un horario
```http
DELETE /api/horarios/<id>
```

---

## 🧪 Ejemplos de uso con curl

Obtener todos los horarios:
```bash
curl -i http://localhost:5000/api/horarios
```

Obtener un horario por ID:
```bash
curl -i http://localhost:5000/api/horarios/1
```

Crear un nuevo horario:
```bash
curl -i -X POST http://localhost:5000/api/horarios -H "Content-Type: application/json" -d '{"materia":"Programación Web","dia":"Lunes","hora":"08:00","estudiante_id":1}'
```

Actualizar un horario:
```bash
curl -i -X PUT http://localhost:5000/api/horarios/1 -H "Content-Type: application/json" -d '{"materia":"Bases de Datos","dia":"Martes","hora":"10:00"}'
```

Eliminar un horario:
```bash
curl -i -X DELETE http://localhost:5000/api/horarios/1
```

---

## 📋 Requisitos

- Python 3.12+
- Flask
- Flask-SQLAlchemy

Instalar dependencias:
```bash
pip install -r requirements.txt
```

---

## ⚡ Instalación y Ejecución

1. Inicializa la base de datos y configura el entorno:
```bash
bash setup.sh
```

2. Levanta el servidor Flask:
```bash
python src/app.py
```

3. Abre en el navegador:
```
http://localhost:5000/api/horarios
```

---

## 📝 Notas

- Los datos se almacenan en SQLite en el archivo `horarios.db`.
- Los endpoints devuelven respuestas en formato **JSON** y usan los códigos de error HTTP apropiados.
- Puedes extender el modelo para agregar más campos (ej. profesor, grupo, semestre).

---

## 📄 `requirements.txt`
```txt
flask==3.0.0
flask_sqlalchemy==3.1.1
sqlalchemy==2.0.20
```

---

## 📄 `setup.sh`
```bash
#!/bin/bash

echo "🚀 Iniciando configuración del proyecto..."

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt

# Crear carpeta de base de datos si no existe
if [ ! -d "src/config" ]; then
  mkdir -p src/config
fi

# Crear base de datos SQLite vacía
if [ ! -f "horarios.db" ]; then
  echo "📦 Creando base de datos horarios.db..."
  touch horarios.db
fi

echo "✅ Configuración finalizada. Ejecuta: python src/app.py"

