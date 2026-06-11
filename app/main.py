# app/main.py
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

# 1. Importación de los routers
from app.api.v1.plantilla_router import router as plantilla_router
from app.api.v1.hoja_de_vida_router import router as hoja_de_vida_router

# 2. Importación del repositorio para sembrar datos de prueba
from app.repositories.hoja_de_vida_repository import hoja_de_vida_repository

app = FastAPI(
    title="API de Gestión de Hojas de Vida",
    description="Backend oficial aplicando Arquitectura de Capas",
    version="1.0.0"
)

# ==========================================
# MANEJADORES DE EXCEPCIONES GLOBALES
# ==========================================
# Capturar errores de validación de Pydantic (Caso 3: Secciones vacías)
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc):
    # Extrae el mensaje real que causó el error (ej: "Input should be 'Gratis', 'Plus' or 'Pro'")
    error_real = exc.errors()[0]["msg"] if exc.errors() else "Error de validación de datos"
    
    return JSONResponse(
        status_code=400,
        content={
            "message": f"Dato inválido: {error_real}",
            "data": None,
            "success": False
        }
    )

# ==========================================
# REGISTRO DE RUTAS (ENDPOINTS)
# ==========================================
app.include_router(plantilla_router)
app.include_router(hoja_de_vida_router)

# ==========================================
# SEMILLERO DE DATOS TEMPORAL (Para Pruebas)
# ==========================================
# Creamos una hoja de vida para el usuario 1 vinculada a la plantilla 1
hoja_de_vida_repository.crear_prueba(usuario_id=1, plantilla_id=1)