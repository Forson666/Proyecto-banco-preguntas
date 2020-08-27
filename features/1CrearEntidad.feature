Feature: 1 Crear entidad

Scenario Outline: registrar Tipos de categoria
  Given a <nombre> to registrar un tipo de categoria
  When la entidad es registrada
  Then el resultado contiene <resultado>

  Examples: nombres
  | nombre           | resultado |
  | Espacio academico | Se ha registrado en Tipos de categoria |
  | Unidad tematica   | Se ha registrado en Tipos de categoria |

Scenario Outline: registrar Tipos de competencia
  Given a <nombre> to registrar un tipo de competencia
  When la entidad es registrada
  Then el resultado contiene <resultado>

  Examples: nombres
  | nombre    | resultado |
  | practicas | Se ha registrado en Tipos de competencia |
  | teorica   | Se ha registrado en Tipos de competencia |

Scenario Outline: registrar Tipos de pregunta
  Given a <nombre> to registrar un tipo de pregunta
  When la entidad es registrada
  Then el resultado contiene <resultado>

  Examples: nombres
  | nombre              | resultado |
  | Abierta             | Se ha registrado en Tipos de pregunta |
  | opcion multiple     | Se ha registrado en Tipos de pregunta |

Scenario Outline: registrar Categorias
  Given a <nombre> and a <tipo> to registrar una categoria
  When la entidad es registrada
  Then el resultado contiene <resultado>

  Examples: nombres y tipos
  | nombre              | tipo | resultado |
  | Ciencias 2          | 1    | Se ha registrado en Categorias |
  | Modelo de proceso   | 2    | Se ha registrado en Categorias |

Scenario Outline: registrar Competencias
  Given a <nombre>, <tipo> and a <descripcion> to registrar una competencia
  When la entidad es registrada
  Then el resultado contiene <resultado>

  Examples: nombres, tipos y descripcion
  | nombre              | tipo | descripcion | resultado |
  | competencia de prueba 1  | 1    | probando la creacion | Se ha registrado en Competencias |
  | competencia de prueba 2   | 2   | probando la creacion otra vez | Se ha registrado en Competencias |

Scenario Outline: registrar Preguntas
  Given a <texto>, <categoria>, <tipo> and a <competencia> to registrar una pregunta
  When la entidad es registrada
  Then el resultado contiene <resultado>

  Examples: Preguntas
  | texto          | categoria | tipo | competencia | resultado |
  | ¿Que es una metodologia agil? | 1 | 1 | 1 | Se ha registrado en Preguntas |
  | ¿Que es la automatizacion de pruebas? | 2 | 2 | 2 | Se ha registrado en Preguntas |

Scenario Outline: registrar Respuestas
  Given a <texto> to registrar una respuesta
  When la entidad es registrada
  Then el resultado contiene <resultado>

  Examples: textos
  | texto              | resultado |
  | un enfoque estructurado para el desarrollo | Se ha registrado en Respuestas |
  | una herramienta para el desarrollo de software | Se ha registrado en Respuestas |

Scenario Outline: registrar Roles
  Given a <nombre> to registrar un rol
  When la entidad es registrada
  Then el resultado contiene <resultado>

  Examples: nombres
  | nombre              | resultado |
  | Administrador       | Se ha registrado en Roles |
  | Profesor            | Se ha registrado en Roles |

Scenario Outline: registrar Usuarios
  Given a <nombre>, <apellido>, <passw>, <email>, <proyecto>, <codigo> and a <rol> to registrar un usuario
  When la entidad es registrada
  Then el resultado contiene <resultado>

  Examples: Usuarios
  | nombre | apellido | passw | email | proyecto | codigo | rol | resultado |
  | Pepito | perez | 1234 | algo@otracosa.com | ing. sistemas | 202012 | 1 | Se ha registrado en Usuarios |
  | Pablo | rodriguez | clave | algo2@otracosa.com | ing. electronica | 111111 | 2 | Se ha registrado en Usuarios |

Scenario Outline: registrar Evaluaciones
  Given a <nombre>, <pporPag>, <maxPuntos>, <puntosP>, <pregunta_id> and a <conjunta> to registrar una evaluacion
  When la entidad es registrada
  Then el resultado contiene <resultado>

  Examples: Usuarios
  | nombre            | pporPag | maxPuntos | puntosP | pregunta_id | conjunta | resultado |
  | Parcial final Fis | 5       | 50        | 1       | 1           | false    | Se ha registrado en Evaluaciones |
  | Parcial 2 ciber 1 | 2       | 10        | 1       | 2           | true     | Se ha registrado en Evaluaciones |