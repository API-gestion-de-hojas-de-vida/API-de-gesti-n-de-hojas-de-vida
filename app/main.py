# app/main.py

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.api.v1.plantilla_router import router as plantilla_router
from app.api.v1.hoja_de_vida_router import router as hoja_de_vida_router
from app.api.v1.validacion_router import router as validacion_router
from app.repositories.hoja_de_vida_repository import hoja_de_vida_repository
from app.repositories.plantilla_repository import plantilla_repository


app = FastAPI(
    title="API de Gestion de Hojas de Vida",
    description="Backend oficial aplicando Arquitectura de Capas",
    version="1.0.0"
)


@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc):
    errors = exc.errors()
    first_error = errors[0] if errors else {}
    loc = str(first_error.get("loc", ""))
    msg = str(first_error.get("msg", ""))
    if "categoria" in loc or "enum" in msg.lower() or "gratis" in msg.lower():
        return JSONResponse(
            status_code=400,
            content={
                "message": "Categoria no valida. Debe ser Gratis, Plus o Pro",
                "data": None,
                "success": False
            }
        )
    return JSONResponse(
        status_code=400,
        content={
            "message": "Las secciones no pueden estar vacias",
            "data": None,
            "success": False
        }
    )


app.include_router(plantilla_router)
app.include_router(hoja_de_vida_router)
app.include_router(validacion_router)

# Seed de plantillas
plantilla_repository.crear(nombre="Plantilla Moderna", secciones=["nombre", "perfil", "experiencia"], categoria="Gratis")
plantilla_repository.crear(nombre="Plantilla Plus", secciones=["nombre", "perfil", "experiencia", "educacion"], categoria="Plus")

# Hoja de vida 1: con plantilla, en borrador
hoja_de_vida_repository.crear_prueba(usuario_id=1, plantilla_id=1)
# Hoja de vida 2: sin plantilla, para probar Caso 3
hoja_de_vida_repository.crear_prueba(usuario_id=1, plantilla_id=None)
# Hoja de vida 3: con plantilla, ya finalizada, para probar Caso 1
hv_finalizada = hoja_de_vida_repository.crear_prueba(usuario_id=1, plantilla_id=1)
hv_finalizada.estado = "finalizada"
