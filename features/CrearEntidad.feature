Feature: Crear entidad

Scenario Outline: registrar entidad
  Given a <entidad> to registrar
  When la entidad es registrada
  Then el resultado contiene <resultado>

  Examples: entidades
  | entidad            | resultado |
  | Tipos de categoria | Se ha registrado en Tipos de categoria |
  | Categorias   | Se ha registrado en Categorias |
