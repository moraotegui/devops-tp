API de Libros — Trabajo Práctico DevOps
API REST desarrollada en Python con FastAPI que gestiona un catálogo de libros. El objetivo principal del proyecto no fue solo desarrollar la lógica de la API, sino aplicar prácticas DevOps reales: containerización, CI/CD automatizado, pruebas unitarias y monitoreo en producción.

Stack tecnológico
HerramientaRolPython + FastAPIAPI RESTpytestTests unitariosDockerContainerización (multi-stage build)GitHub ActionsCI/CD automatizadoDocker HubRegistry de imágenesNew RelicMonitoreo y APM

Endpoints
MétodoEndpointDescripciónGET/Estado de la APIGET/healthHealth checkGET/librosListar todos los librosGET/libros/{id}Obtener un libro por IDPOST/librosAgregar un libro nuevo

Correr localmente
Con Docker Compose:
bashdocker compose up
Sin Docker:
bashpip install -r requirements.txt
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000
La API queda disponible en http://localhost:8000. La documentación interactiva se genera automáticamente en http://localhost:8000/docs.

Tests
bashpip install -r requirements.txt
python3 -m pytest tests/ -v
Resultado esperado: 4 passed, 0 failed.

Pipeline CI/CD
El pipeline se configura con GitHub Actions en .github/workflows/:

ci.yml — se dispara en cada push y Pull Request a main. Instala dependencias, corre los tests y buildea la imagen Docker. Si algún test falla, el build se detiene.
cd.yml — se dispara al mergear a main. Construye la imagen Docker y la publica automáticamente en Docker Hub como moraotegui/devops-tp:latest.


Estructura del proyecto
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

Imagen Docker
La imagen está publicada en Docker Hub y se actualiza automáticamente en cada merge a main:
bashdocker pull moraotegui/devops-tp:latest
docker run -p 8000:8000 moraotegui/devops-tp:latest

Monitoreo
El agente de New Relic está integrado en la API y registra automáticamente cada request: tiempo de respuesta, throughput, errores y trazas de ejecución.
