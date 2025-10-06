from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=200, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


# Área dos exemplos
@app.get('/ex1', response_class=HTMLResponse)
def read_root_ex1():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html> """
