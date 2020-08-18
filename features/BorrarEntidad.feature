Feature: BorrarEntidad

Scenario Outline: borrar un registro
  Given a <entidad> and <id> to borrar un registro
  When el registro es borrado de la entidad
  Then el registro no esta en la respuesta

  Examples: nombres
  | entidad      | id |
  | Categorias | 1 |
  | Tipos de categoria    | 1 |