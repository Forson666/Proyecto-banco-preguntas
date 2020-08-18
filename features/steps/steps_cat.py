from behave import *
import requests

# Escenario de creacion de tipos de categoria
@given('a {nombre} to crear tipo de categoria')
def step_impl(context, nombre):
    context.api_url = 'http://localhost:5000/crearTipoCategoria/' + nombre
    print('url :'+context.api_url)

@when('el tipo de categoria es creado')
def step_impl(context):
    session = requests.Session()
    response = session.get(url=context.api_url, headers="")
    context.resultado = response.text

@then('el tipo de categoria {nombre} se ha creado')
def step_impl(context, nombre):
    assert (nombre in context.resultado)

# Escenario de creacion de categorias
@given('a {nombre} and a {tipo} to crear categoria')
def step_impl(context, nombre, tipo):
    context.api_url = 'http://localhost:5000/crearCategoria/' + nombre + '/' + tipo
    print('url :'+context.api_url)

@when('la categoria es creada')
def step_impl(context):
    session = requests.Session()
    response = session.get(url=context.api_url, headers="")
    context.resultado = response.text
    print(response.text)

@then('la categoria {nombre} de tipo {tipo} fue creada')
def step_impl(context, nombre, tipo):
    assert (nombre in context.resultado and tipo in context.resultado)
