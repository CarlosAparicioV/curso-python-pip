import utils
import read_csv
import charts
import pandas as pd


def run():
    '''
    Pandas ya hace todo esto, por lo que no es necesario hacerlo manualmente!
    # Primero obtenemos los datos usando el módulo read_csv y su método read_csv.
    data = read_csv.read_csv("data.csv")
    data = list(
        filter(lambda item: item["Continent"] == "South America", data))

    countries = list(map(lambda x: x["Country/Territory"], data))
    percentages = list(map(lambda x: x["World Population Percentage"], data))
    '''
    # Leemos el csv. Sustituye al módulo read_csv antes creado
    df = pd.read_csv('data.csv')
    # Sustituimos al filter
    df = df[df['Continent'] == 'Africa']
    # Obtenemos los valores de la columna Country
    countries = df['Country/Territory'].values
    # Obtenemos los valores de la columna World Population Percentage
    percentages = df['World Population Percentage'].values
    # Generamos pie chart gracias a Pandas
    charts.generate_pie_chart(countries, percentages)

    # A partir de aquí ya no utilizamos Pandas
    data = read_csv.read_csv("data.csv")
    # Pedimos al usuario que nos diga el país del cual necesita información
    country = input("Type country: ")

    # Regresa una lista con el diccionario(s) que tenga en su key Country el valor del país que quiere el usuario.
    result = utils.population_by_country(data, country)

    if len(result) > 0:
        # Aquí de la lista creada anteormente, sacamos solo el diccionario que contiene. De forma que la variable country ahora guarda el diccionario que tiene toda la información del país que queremos.
        country = result[0]
        # Usamos el módulo get_population que lo que hace es filtrar de toda la información del país que tenemos en su diccionario, solamente rescatar la información de la población en cada año. Esto lo hace creando otro diccionario pero más pequeño, con la información de la población únicamente, y luego asignamos las keys y los values de ese nuevo diccionario como dos listas, una con los labels y otra con los values, respectivamente.
        labels, values = utils.get_population(country)
        # Usamos el módulo que tiene toda la lógica para realizar una gráfica de barras y le pasamos como parámetros la información de los labels y values, que son listas.
        charts.generate_bar_chart(country["Country/Territory"], labels, values)


# Este if le dice al archivo main.py que si es ejecutado desde la terminal, ejecute la función run(), pero si es ejecutado desde otro archivo, esto no se va a ejecutar.
if __name__ == "__main__":
    run()
