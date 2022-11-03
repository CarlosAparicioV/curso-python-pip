import store
from fastapi import FastAPI
# Import para mandar HTML:
from fastapi.responses import HTMLResponse

app = FastAPI()  # Creamos una instancia de FastAPI


@app.get("/")  # Usamos un decorador al que le pasamos la ruta para ver desde la web
def get_list():
    return [1, 2, 3, 4]

# Para mandar un html al servidor:


@app.get("/contact", response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hola soy una página</h1>
        <p>Soy un párrafo</p>
    """


def run():
    store.get_categories()


if __name__ == "__main__":
    run()
