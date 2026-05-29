import newrelic.agent
newrelic.agent.initialize('newrelic.ini')

from fastapi import FastAPI

app = FastAPI(title="API de Libros")

libros = [
    {"id": 1, "titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "genero": "Realismo mágico"},
    {"id": 2, "titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "genero": "Ficción"},
    {"id": 3, "titulo": "1984", "autor": "George Orwell", "genero": "Distopía"},
    {"id": 4, "titulo": "Harry Potter y la piedra filosofal", "autor": "J.K. Rowling", "genero": "Fantasía"},
]

@app.get("/")
def root():
    return {"status": "ok", "message": "API de Libros funcionando"}

@app.get("/health")
def health():
    return {"healthy": True}

@app.get("/libros")
def get_libros():
    return {"libros": libros, "total": len(libros)}

@app.get("/libros/{libro_id}")
def get_libro(libro_id: int):
    libro = next((l for l in libros if l["id"] == libro_id), None)
    if not libro:
        return {"error": "Libro no encontrado"}
    return libro

@app.post("/libros")
def crear_libro(titulo: str, autor: str, genero: str):
    nuevo = {"id": len(libros) + 1, "titulo": titulo, "autor": autor, "genero": genero}
    libros.append(nuevo)
    return {"creado": True, "libro": nuevo}
