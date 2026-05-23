# app/main.py
from fastapi import FastAPI
from app.api.v1.plantilla_router import router as plantilla_router
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

app = FastAPI(
    title="API de Gestión de Hojas de Vida",
    description="Backend oficial aplicando Arquitectura de Capas",
    version="1.0.0"
)

# Capturar errores de validación de Pydantic (Caso 3: Secciones vacías)
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={
            "message": "Las secciones no pueden estar vacías",
            "data": None,
            "success": False
        }
    )

app.include_router(plantilla_router)