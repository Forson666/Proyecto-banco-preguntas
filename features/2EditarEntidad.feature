Feature: 2 Editar entidad

Scenario Outline: editar Tipos de categoria
  Given a nuevo <nombre> to editar el tipo de categoria <id>
  When la entidad es editada
  Then el resultado contiene <resultado>

  Examples: nombres
  | nombre  | id | resultado |
  | Espacio | 1 | Se ha editado un registro de Tipos de categoria |
  | Unidad  | 2 | Se ha editado un registro de Tipos de categoria |

Scenario Outline: editar Tipos de competencia
  Given a <nombre> to editar el tipo de competencia <id>
  When la entidad es editada
  Then el resultado contiene <resultado>

  Examples: nombres
  | nombre                            | id | resultado |
  | resolucion de problemas aplicados | 1  | Se ha editado un registro de Tipos de competencia |
  | resolucion de problemas teoricos  | 2  | Se ha editado un registro de Tipos de competencia |

Scenario Outline: editar Tipos de pregunta
  Given a <nombre> to editar el tipo de pregunta <id>
  When la entidad es editada
  Then el resultado contiene <resultado>

  Examples: nombres
  | nombre              | id | resultado |
  | de respuesta extendida | 1 | Se ha editado un registro de Tipos de pregunta |
  | tipo icfes     | 2 | Se ha editado un registro de Tipos de pregunta |

Scenario Outline: editar Categorias
  Given a <nombre> and a <tipo> to editar la categoria <id>
  When la entidad es editada
  Then el resultado contiene <resultado>

  Examples: nombres y tipos
  | nombre              | id | tipo | resultado |
  | Ciencias de la computacion 2 | 1 | 1    | Se ha editado un registro de Categorias |
  | modelos   | 2 | 2    | Se ha editado un registro de Categorias |

Scenario Outline: editar Preguntas
  Given a <texto>, <categoria>, <tipo> and a <competencia> to editar la pregunta <id>
  When la entidad es editada
  Then el resultado contiene <resultado>

  Examples: Preguntas
  | texto          | categoria | tipo | competencia | id | resultado |
  | ¿Que es una metodologia? | 1 | 1 | 1 | 1 | Se ha editado un registro de Preguntas |
  | ¿Para que sirve la automatizacion de pruebas? | 2 | 2 | 2 | 2 | Se ha editado un registro de Preguntas |

Scenario Outline: editar Competencias
  Given a <nombre>, <tipo> and a <descripcion> to editar la competencia <id>
  When la entidad es editada
  Then el resultado contiene <resultado>

  Examples: nombres, tipos y descripcion
  | nombre              | tipo | descripcion | id | resultado |
  | competencia 1 editada  | 1    | probando la edicion | 1 | Se ha editado un registro de Competencias |
  | competencia 2 editada | 2   | probando la edicion otra vez | 2 | Se ha editado un registro de Competencias |

Scenario Outline: editar Respuestas
  Given a <texto> to editar la respuesta <id>
  When la entidad es editada
  Then el resultado contiene <resultado>

  Examples: textos
  | texto              | id | resultado |
  | un enfoque estructurado y editado | 1 | Se ha editado un registro de Respuestas |
  | una herramienta para editar | 2 | Se ha editado un registro de Respuestas |

Scenario Outline: editar Roles
  Given a <nombre> to editar el rol <id>
  When la entidad es editada
  Then el resultado contiene <resultado>

  Examples: nombres
  | nombre      | id | resultado |
  | Admin       | 1 | Se ha editado un registro de Roles |
  | Teacher     | 2 | Se ha editado un registro de Roles |

Scenario Outline: editar Usuarios
  Given a <nombre>, <apellido>, <passw>, <email>, <proyecto>, <codigo> and a <rol> to editar el usuario <id>
  When la entidad es editada
  Then el resultado contiene <resultado>

  Examples: Usuarios
  | nombre | apellido | passw | email | proyecto | codigo | rol | id | resultado |
  | Pepito | El editado | 1234 | algo@otracosa.com | ing. sistemas | 202012 | 1 | 1 | Se ha editado un registro de Usuarios |
  | Pablo | con cambio | clave | algo2@otracosa.com | ing. electronica | 111111 | 2 | 2 | Se ha editado un registro de Usuarios |

Scenario Outline: editar Evaluaciones
  Given a <nombre>, <pporPag>, <maxPuntos>, <puntosP>, <pregunta_id> and a <conjunta> to editar la evaluacion <id>
  When la entidad es editada
  Then el resultado contiene <resultado>

  Examples: Usuarios
  | nombre                  | pporPag | maxPuntos | puntosP | pregunta_id | conjunta | id | resultado |
  | Parcial casi dinal Fis  | 5       | 50        | 1       | 1           | false    | 1  | Se ha editado un registro de Evaluaciones |
  | Parcial 2 cibernetica 1 | 2       | 10        | 1       | 1           | true     | 2  | Se ha editado un registro de Evaluaciones |