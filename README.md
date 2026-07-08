 # API de Libros — Trabajo Práctico DevOps

API REST desarrollada en Python con FastAPI que gestiona un catálogo de libros. El objetivo principal del proyecto no fue solo desarrollar la lógica de la API, sino aplicar prácticas DevOps reales: containerización, CI/CD automatizado, pruebas unitarias y monitoreo en producción.

---

## Stack tecnológico

| Herramienta | Rol |
|---|---|
| Python + FastAPI | API REST |
| pytest | Tests unitarios |
| Docker | Containerización (multi-stage build) |
| GitHub Actions | CI/CD automatizado |
| Render | Deploy automático en producción |
| Docker Hub | Registry de imágenes |
| New Relic | Monitoreo y APM |

---

## Endpoints

| Método | Endpoint | Descripción |
|---|---|---|
| GET | `/` | Estado de la API |
| GET | `/health` | Health check |
| GET | `/libros` | Listar todos los libros |
| GET | `/libros/{id}` | Obtener un libro por ID |
| POST | `/libros` | Agregar un libro nuevo |

---

## Correr localmente

**Con Docker Compose:**
```bash
docker compose up
```

**Sin Docker:**
```bash
pip install -r requirements.txt
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

La API queda disponible en `http://localhost:8000`. La documentación interactiva se genera automáticamente en `http://localhost:8000/docs`.

---

## Tests

```bash
pip install -r requirements.txt
python3 -m pytest tests/ -v
```

Resultado esperado: **4 passed, 0 failed**.

---

## Pipeline CI/CD

El pipeline se configura con GitHub Actions en `.github/workflows/`:

- **ci.yml** — se dispara en cada push y Pull Request a `main`. Instala dependencias, corre los tests y buildea la imagen Docker. Si algún test falla, el build se detiene.
- **cd.yml** — se dispara al mergear a `main`. Construye la imagen Docker, la publica en Docker Hub con tag `latest` y versión `v1.0.X`, y hace deploy automático a Render.

---

## Estructura del proyecto
```
devops-tp/
├── app/
│   └── main.py              # API con 5 endpoints REST
├── tests/
│   └── test_main.py         # 4 tests unitarios con pytest
├── .github/
│   └── workflows/
│       ├── ci.yml           # Pipeline CI: tests + build
│       └── cd.yml           # Pipeline CD: push a Docker Hub
├── Dockerfile               # Multi-stage build
├── docker-compose.yml       # Orquestación local con healthcheck
├── newrelic.ini             # Configuración del agente de monitoreo
└── requirements.txt
```

## Imagen Docker

La imagen está publicada en Docker Hub y se actualiza automáticamente en cada merge a main:

```bash
docker pull moraotegui/devops-tp:latest
docker run -p 8000:8000 moraotegui/devops-tp:latest
```
---
## Deploy en producción

La API está deployada automáticamente en Render:

**URL pública:** https://devops-tp-u988.onrender.com

Endpoints disponibles en producción:
- https://devops-tp-u988.onrender.com/libros
- https://devops-tp-u988.onrender.com/docs

> El deploy se dispara automáticamente desde GitHub Actions cada vez que se mergea a main.
---

## Monitoreo

El agente de New Relic está integrado en la API y registra automáticamente cada request: tiempo de respuesta, throughput, errores y trazas de ejecución.

---
