from behave import *
import requests

# Escenario de borrar registro
@given('a {entidad} and {id} to borrar un registro')
def step_impl(context, entidad, id):
    context.api_url = 'http://localhost:5000/borrar/' + entidad + '/' + id
    print('url :'+context.api_url)

@when('el registro es borrado de la entidad')
def step_impl(context):
    session = requests.Session()
    response = session.get(url=context.api_url, headers="")
    context.resultado = response.text

@then('el resultado es {resultado}')
def step_impl(context, resultado):
    assert (resultado in context.resultado)