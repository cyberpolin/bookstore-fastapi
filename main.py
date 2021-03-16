from fastapi import FastAPI

app = FastAPI()

DB = {
    "libros": [
        {
            "id": 1,
            "nombre": "El amor en los tiempos del colera",
            "autores": [1]
        },
        {
            "id": 2,
            "nombre": "Quiubole con...",
            "autores": [2,3]
        },
        {
            "id": 3,
            "nombre": "Todo sobre la imagen del éxito",
            "autores": [2]
        },
        {
            "id": 4,
            "nombre": "El coronel no tiene quien le escriba",
            "autores": [1]
        },
        {
            "id": 5,
            "nombre": "Ojos de perro azul",
            "autores": [1]
        },
    ],
    "autores": [
        {
            "id": 1,
            "nombre": "Gabriel García Márquez",
            "libros": [1,4,5]
        },
        {
            "id": 2,
            "nombre": "Gaby Vargas",
            "libros": [2,3]
        },
        {
            "id": 3,
            "nombre": "Yordi Rosado",
            "libros": [2]
        }
    ]
}

@app.get('/')
def get_all_data():
    return DB

@app.get('/libros')
def get_all_libros():
    return DB['libros']

@app.get('/libros/{id}')
def get_single_libros(id:int):
    libros = DB['libros']
    for libro in libros:
        if libro['id'] == id:
            return libro

    return {
        "message": "libro no encontrado"
    }

@app.get('/libros/{libro_id}/autores')
def get_autores_from_libros(libro_id:int):
    libros = DB['libros']
    autores = DB['autores']
    autores_res = []
    for libro in libros:
        if libro['id'] == libro_id:
            for autor in libro['autores']:
                for autor_ext in autores:
                    if autor_ext['id'] == autor:
                        autores_res.append(autor_ext)

    return autores_res


@app.get('/autores')
def get_all_autores():
    return DB['autores']

@app.get('/autores/{id}')
def get_single_libros(id:int):
    autores = DB['autores']
    for autor in autores:
        if autor['id'] == id:
            return autor

    return {
        "message": "autor no encontrado"
    }

@app.get('/autores/{autor_id}/libros')
def get_libros_from_autores(autor_id:int):
    libros = DB['libros']
    autores = DB['autores']
    libros_res = []
    for autor in autores:
        if autor['id'] == autor_id:
            for libro in autor['libros']:
                for libro_data in libros:
                    if libro_data['id'] == libro:
                        libros_res.append(libro_data)

    return libros_res

