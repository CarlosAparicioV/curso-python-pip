import requests


def get_categories():
    # API de Platzi
    r = requests.get("https://api.escuelajs.co/api/v1/categories")
    print(r.status_code)  # Obtener el estado del request
    print(r.text)  # Obtener la respuesta (el retorno) de esta API
    print(type(r.text))
    categories = r.json()  # Transforma el retorno en un formato JSON para poder iterar
    for category in categories:
        print(category["name"])


''' Nota: Obtener un 200 es r.status_code significa que todo está bien en idioma de
    HTTP.
    Método JSON: El resultado de r.text lo devuelve en formato de string, por lo que para
    iterar hay que transformarlo. El formato JSON automáticamente transforma la
    salida en una lista que Python va a reconocer y los elementos adentro
    serán diccionarios. Con esto podemos hacer iteraciones.'''
