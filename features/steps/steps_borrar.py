from behave import *
import requests

# Escenario de borrar registro
@given('a {entidad} and {id} to borrar un registro')
def step_impl(context, entidad, id):
    session = requests.Session()
    response = session.get(url="http://localhost:5000/nav/" + entidad, headers="")
    context.antes = response.text
    context.api_url = 'http://localhost:5000/borrar/' + entidad + '/' + id
    print('url :'+context.api_url)

@when('el registro es borrado de la entidad')
def step_impl(context):
    session = requests.Session()
    response = session.get(url=context.api_url, headers="")
    context.resultado = response.text

@then('el registro no esta en la respuesta')
def step_impl(context):
    assert (context.antes != context.resultado)