# Capa de Repositorios en un Sistema de Gestión de Horarios

En el desarrollo de aplicaciones con arquitectura por capas, la **capa de repositorios** juega un rol fundamental al encargarse de la comunicación con la base de datos. En este proyecto, los repositorios se implementan para gestionar las entidades **Estudiante** y **Horario**, aplicando operaciones CRUD mediante SQLAlchemy.

## ¿Qué es la capa de repositorios?
La capa de repositorios es el puente entre la lógica de negocio y la base de datos. En ella se encapsulan las consultas y operaciones sobre las entidades, lo que permite que el resto de la aplicación trabaje de forma desacoplada y clara.

En este proyecto, el repositorio se encuentra en:

### Responsabilidades principales
- Implementar operaciones **CRUD** (crear, leer, actualizar y eliminar).
- Proveer funciones reutilizables para manejar estudiantes y horarios.
- Centralizar la lógica de acceso a datos para mayor organización.
- Garantizar independencia de la lógica de negocio frente a los detalles de persistencia.

## Ejemplo de operaciones CRUD

### Estudiante
- `crear_estudiante(db, nombre, carrera)` → Agrega un nuevo estudiante.
- `obtener_estudiantes(db)` → Lista todos los estudiantes.
- `actualizar_estudiante(db, estudiante_id, nombre, carrera)` → Actualiza los datos de un estudiante.
- `eliminar_estudiante(db, estudiante_id)` → Elimina un estudiante y sus horarios asociados.

### Horario
- `crear_horario(db, materia, dia, hora, estudiante_id)` → Asigna un horario a un estudiante.
- `obtener_horarios(db)` → Lista todos los horarios.
- `actualizar_horario(db, horario_id, materia, dia, hora)` → Modifica un horario existente.
- `eliminar_horario(db, horario_id)` → Elimina un horario específico.

## Ventajas de usar un ORM (SQLAlchemy)
- **Abstracción de SQL:** Permite trabajar con clases y objetos en lugar de sentencias SQL directas.
- **Manejo de relaciones:** Simplifica la gestión de relaciones (un estudiante puede tener múltiples horarios).
- **Portabilidad:** Facilita cambiar entre distintos motores de base de datos.
- **Seguridad:** Reduce riesgos de inyección SQL al generar consultas seguras.
- **Productividad:** Acelera el desarrollo evitando consultas manuales.

## Separación de responsabilidades
Gracias al uso de repositorios:
- La **lógica de negocio** no depende de SQL ni del motor de base de datos.
- Se facilita la **mantenibilidad**, ya que cada capa tiene una función clara.
- Se mejora la **escalabilidad**, permitiendo agregar nuevas consultas o funcionalidades sin alterar la lógica central.
- Es más sencillo realizar **pruebas unitarias**, ya que los repositorios pueden simularse con facilidad.

## Conclusión
La capa de repositorios es esencial en este sistema de gestión de horarios. Permite mantener un código organizado, desacoplado y escalable, asegurando que la lógica de negocio (controladores y servicios) esté completamente separada de la lógica de persistencia en base de datos.
