Feature: 3 Borrar Entidad

Scenario Outline: borrar un registro
  Given a <entidad> and <id> to borrar un registro
  When el registro es borrado de la entidad
  Then el resultado es <resultado>

  Examples: entidades
  | entidad      | id | resultado |
  | Evaluaciones | 1 | Se ha borrado un registro de Evaluaciones |
  | Preguntas    | 1 | Se ha borrado un registro de Preguntas |
  | Categorias | 1 | Se ha borrado un registro de Categorias |
  | Usuarios | 1 | Se ha borrado un registro de Usuarios |
  | Competencias | 1 | Se ha borrado un registro de Competencias |
  | Tipos de competencia    | 1 | Se ha borrado un registro de Tipos de competencia |
  | Tipos de pregunta | 1 | Se ha borrado un registro de Tipos de pregunta |
  | Respuestas    | 1 | Se ha borrado un registro de Respuestas |
  | Roles    | 1 | Se ha borrado un registro de Roles |
  