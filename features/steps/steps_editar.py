from behave import *
import requests

# Escenario de editar Tipos de categoria
@given('a {nombre} to editar el tipo de categoria {id}')
def step_impl(context, nombre, id):
    context.api_url = 'http://localhost:5000/editar/Tipos de categoria/' + id
    context.formulario = { id + "tca_nombre" : nombre}
    print('url :'+context.api_url)

# Escenario de editar Categorias
@given('a {nombre} and a {tipo} to editar la categoria {id}')
def step_impl(context, nombre, tipo, id):
    context.api_url = 'http://localhost:5000/editar/Categorias/' + id
    context.formulario = {id + "cat_nombre" : nombre, id + "cat_tipo" : tipo}
    print('url :'+context.api_url)

# Escenario de editar Preguntas
@given('a {texto}, {categoria}, {tipo} and a {competencia} to editar la pregunta {id}')
def step_impl(context, texto, categoria, tipo, competencia, id):
    context.api_url = 'http://localhost:5000/editar/Preguntas/' + id
    context.formulario = {id + "pre_texto" : texto, id + "cat_id" : categoria, id + "com_id" : competencia, id + "tpr_id" : tipo}
    print('url :'+context.api_url)

# Escenario de editar Competencias
@given('a {nombre}, {tipo} and a {descripcion} to editar la competencia {id}')
def step_impl(context, nombre, tipo, descripcion, id):
    context.api_url = 'http://localhost:5000/editar/Competencias/' + id
    context.formulario = {id + "com_nombre" : nombre, id + "com_tipo" : tipo, id + "com_desc" : descripcion}
    print('url :'+context.api_url)

# Escenario de editar tipos de competencia
@given('a {nombre} to editar el tipo de competencia {id}')
def step_impl(context, nombre, id):
    context.api_url = 'http://localhost:5000/editar/Tipos de competencia/' + id
    context.formulario = {id + "tco_nombre" : nombre}
    print('url :'+context.api_url)

# Escenario de editar tipos de pregunta
@given('a {nombre} to editar el tipo de pregunta {id}')
def step_impl(context, nombre, id):
    context.api_url = 'http://localhost:5000/editar/Tipos de pregunta/' + id
    context.formulario = {id + "tpp_nombre" : nombre}
    print('url :'+context.api_url)

# Escenario de editar Respuestas
@given('a {texto} to editar la respuesta {id}')
def step_impl(context, texto, id):
    context.api_url = 'http://localhost:5000/editar/Respuestas/' + id
    context.formulario = {id + "res_texto" : texto}
    print('url :'+context.api_url)

# Escenario de editar Usuarios
@given('a {nombre}, {apellido}, {passw}, {email}, {proyecto}, {codigo} and a {rol} to editar el usuario {id}')
def step_impl(context, nombre, apellido, passw, email, proyecto, codigo, rol, id):
    context.api_url = 'http://localhost:5000/editar/Usuarios/' + id
    context.formulario = {id + "user_nombre" : nombre, id + "user_apellido" : apellido, id + "user_passw" :passw, id + "user_email" : email, id + "user_proy" : proyecto, id + "user_cod" : codigo, id + "rol_id" : rol}
    print('url :'+context.api_url)

# Escenario de editar Roles
@given('a {nombre} to editar el rol {id}')
def step_impl(context, nombre, id):
    context.api_url = 'http://localhost:5000/editar/Roles/' + id
    context.formulario = {id + "rol_nombre" : nombre}
    print('url :'+context.api_url)

# Escenario de editar Evaluaciones
@given('a {nombre}, {pporPag}, {maxPuntos}, {puntosP}, {pregunta_id} and a {conjunta} to editar la evaluacion {id}')
def step_impl(context, nombre, pporPag, maxPuntos, puntosP, pregunta_id, conjunta, id):
    context.api_url = 'http://localhost:5000/editar/Evaluaciones/' + id
    context.formulario = {id + "eval_nombre" : nombre, id + "eval_pporPag" : pporPag, id + "eval_maxPuntos" :maxPuntos, id + "eval_puntosP" : puntosP, id + "pregunta_id" : pregunta_id, id + "eval_conjunta" : conjunta}
    print('url :'+context.api_url)

# pasos en comun para todos los escenarios
@when('la entidad es editada')
def step_impl(context):
    session = requests.Session()
    response = session.get(url=context.api_url, headers="", data=context.formulario)
    context.resultado = response.text

