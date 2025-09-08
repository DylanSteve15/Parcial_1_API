# Uso de Modelos en un Patrón Arquitectónico por Capas

En el desarrollo de aplicaciones modernas, utilizar un **patrón arquitectónico por capas** es fundamental para mantener el software organizado, mantenible y escalable. Una de las capas esenciales en este patrón es la **capa de modelos**.

---

## ¿Qué es la capa de modelos?
La **capa de modelos** representa y gestiona los **datos de la aplicación**. Define las entidades del sistema (en este caso, **estudiantes** y **horarios**) y las relaciones entre ellas.  

En un sistema de gestión de horarios académicos:
- El modelo **Estudiante** almacena información básica como el nombre y el correo del alumno.  
- El modelo **Horario** guarda la materia, el día y la hora de clase.  
- La relación entre ellos es de **uno a muchos**: un estudiante puede tener varios horarios asignados.

De esta forma, los modelos actúan como un puente entre la base de datos y la lógica de negocio, evitando que las capas superiores dependan directamente de consultas SQL.

---

## Ventajas de usar un ORM (Object Relational Mapper)
En este proyecto utilizamos **SQLAlchemy** como ORM. Algunas de sus ventajas son:

- **Abstracción de la base de datos:** trabajamos con clases y objetos en Python, en lugar de escribir SQL manualmente.  
- **Portabilidad:** es posible cambiar de motor de base de datos (por ejemplo, de SQLite a MySQL) sin modificar los modelos.  
- **Gestión de relaciones:** facilita definir relaciones como **uno a muchos** (un estudiante → varios horarios).  
- **Seguridad:** reduce el riesgo de inyección SQL, ya que genera consultas seguras automáticamente.  
- **Mantenimiento:** las operaciones sobre datos se realizan a través de métodos y atributos, lo que hace el código más limpio y fácil de entender.

---

## Separación de la lógica de negocio y la base de datos
La capa de modelos no contiene lógica de negocio. Su única responsabilidad es representar los datos.  
La lógica de negocio se ubica en capas superiores (por ejemplo, servicios y controladores).  

### Beneficios:
- **Independencia tecnológica:** se puede cambiar de base de datos sin modificar la lógica de negocio.  
- **Reutilización:** la lógica de negocio se puede aplicar en diferentes proyectos.  
- **Pruebas más simples:** es posible simular los modelos sin necesidad de usar una base de datos real.  
- **Mantenimiento claro:** cada capa tiene un rol definido, lo que reduce la complejidad.

---

## Conclusión
En este sistema de **gestión de horarios para estudiantes**, los modelos son la base que define cómo se estructuran y relacionan los datos. Gracias al uso de **SQLAlchemy como ORM**, se consigue un desarrollo más seguro, portable y escalable, siguiendo las buenas prácticas de un patrón arquitectónico por capas.
