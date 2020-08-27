from behave import *
import requests

# Escenario de registrar tipos de categoria
@given('a {nombre} to registrar un tipo de categoria')
def step_impl(context, nombre):
    context.api_url = 'http://localhost:5000/crear/Tipos de categoria'
    context.formulario = {"tca_nombre" : nombre}
    print('url :'+context.api_url)

# Escenario de registrar Categorias
@given('a {nombre} and a {tipo} to registrar una categoria')
def step_impl(context, nombre, tipo):
    context.api_url = 'http://localhost:5000/crear/Categorias'
    context.formulario = {"cat_nombre" : nombre, "cat_tipo" : tipo}
    print('url :'+context.api_url)

# Escenario de registrar Preguntas
@given('a {texto}, {categoria}, {tipo} and a {competencia} to registrar una pregunta')
def step_impl(context, texto, categoria, tipo, competencia):
    context.api_url = 'http://localhost:5000/crear/Preguntas'
    context.formulario = {"pre_texto" : texto, "cat_id" : categoria, "com_id" : competencia, "tpr_id" : tipo}
    print('url :'+context.api_url)

# Escenario de registrar Competencias
@given('a {nombre}, {tipo} and a {descripcion} to registrar una competencia')
def step_impl(context, nombre, tipo, descripcion):
    context.api_url = 'http://localhost:5000/crear/Competencias'
    context.formulario = {"com_nombre" : nombre, "com_tipo" : tipo, "com_desc" : descripcion}
    print('url :'+context.api_url)

# Escenario de registrar tipos de competencia
@given('a {nombre} to registrar un tipo de competencia')
def step_impl(context, nombre):
    context.api_url = 'http://localhost:5000/crear/Tipos de competencia'
    context.formulario = {"tco_nombre" : nombre}
    print('url :'+context.api_url)

# Escenario de registrar tipos de pregunta
@given('a {nombre} to registrar un tipo de pregunta')
def step_impl(context, nombre):
    context.api_url = 'http://localhost:5000/crear/Tipos de pregunta'
    context.formulario = {"tpp_nombre" : nombre}
    print('url :'+context.api_url)

# Escenario de registrar Respuestas
@given('a {texto} to registrar una respuesta')
def step_impl(context, texto):
    context.api_url = 'http://localhost:5000/crear/Respuestas'
    context.formulario = {"res_texto" : texto}
    print('url :'+context.api_url)

# Escenario de registrar Usuarios
@given('a {nombre}, {apellido}, {passw}, {email}, {proyecto}, {codigo} and a {rol} to registrar un usuario')
def step_impl(context, nombre, apellido, passw, email, proyecto, codigo, rol):
    context.api_url = 'http://localhost:5000/crear/Usuarios'
    context.formulario = {"user_nombre" : nombre, "user_apellido" : apellido, "user_passw" :passw, "user_email" : email, "user_proy" : proyecto, "user_cod" : codigo, "rol_id" : rol}
    print('url :'+context.api_url)

# Escenario de registrar Roles
@given('a {nombre} to registrar un rol')
def step_impl(context, nombre):
    context.api_url = 'http://localhost:5000/crear/Roles'
    context.formulario = {"rol_nombre" : nombre}
    print('url :'+context.api_url)

# Escenario de registrar Evaluaciones
@given('a {nombre}, {pporPag}, {maxPuntos}, {puntosP}, {pregunta_id} and a {conjunta} to registrar una evaluacion')
def step_impl(context, nombre, pporPag, maxPuntos, puntosP, pregunta_id, conjunta):
    context.api_url = 'http://localhost:5000/crear/Evaluaciones'
    context.formulario = {"eval_nombre" : nombre, "eval_pporPag" : pporPag, "eval_maxPuntos" :maxPuntos, "eval_puntosP" : puntosP, "pregunta_id" : pregunta_id, "eval_conjunta" : conjunta}
    print('url :'+context.api_url)

# pasos en comun para todos los escenarios
@when('la entidad es registrada')
def step_impl(context):
    session = requests.Session()
    response = session.get(url=context.api_url, headers="", data=context.formulario)
    context.resultado = response.text

@then('el resultado contiene {resultado}')
def step_impl(context, resultado):
    assert (resultado in context.resultado)
