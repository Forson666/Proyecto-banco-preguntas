Feature: GestionCategorias

Scenario Outline: crear tipo de categoria
  Given a <nombre> to crear tipo de categoria
  When el tipo de categoria es creado
  Then el tipo de categoria <nombre> se ha creado

  Examples: nombres
  | nombre      |
  | Espacio academico |
  | Unidad tematica    |

Scenario Outline: crear una categoria
  Given a <nombre> and a <tipo> to crear categoria
  When la categoria es creada
  Then la categoria <nombre> de tipo <tipo> fue creada

  Examples: nombres
  | nombre      | tipo              |
  | ciencias 2  | 1 |
  | entender    | competencia       |
  | FIS         | espacio academico |
  | Behave      | Competencia       |
