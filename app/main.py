# app/main.py
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
<<<<<<< HEAD

# 1. Importación de los routers
from app.api.v1.plantilla_router import router as plantilla_router
from app.api.v1.hoja_de_vida_router import router as hoja_de_vida_router

# 2. Importación del repositorio para sembrar datos de prueba
from app.repositories.hoja_de_vida_repository import hoja_de_vida_repository
=======
from app.api.v1.validacion_router import router as validacion_router
from app.api.v1.hoja_de_vida_router import router as hoja_de_vida_router
from app.api.v1.usuario_router import router as usuario_router
from app.api.v1.plantilla_router import router as plantilla_router
from app.api.v1.planes_router import router as planes_router
from app.api.v1.pagos_router import router as pagos_router
>>>>>>> origin/development

app = FastAPI(
    title="API de GestiÃƒÆ’Ã‚Â³n de Hojas de Vida",
    description="Backend oficial aplicando Arquitectura de Capas",
    version="1.0.0"
)

# ==========================================
# MANEJADORES DE EXCEPCIONES GLOBALES
# ==========================================
# Capturar errores de validación de Pydantic (Caso 3: Secciones vacías)
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request, exc):
<<<<<<< HEAD
    # Extrae el mensaje real que causó el error (ej: "Input should be 'Gratis', 'Plus' or 'Pro'")
    error_real = exc.errors()[0]["msg"] if exc.errors() else "Error de validación de datos"
    
    return JSONResponse(
        status_code=400,
        content={
            "message": f"Dato inválido: {error_real}",
=======
    errors = exc.errors()
    first_error = errors[0] if errors else {}
    loc = str(first_error.get("loc", ""))
    msg = str(first_error.get("msg", ""))

    if "categoria" in loc or "enum" in msg.lower() or "gratis" in msg.lower():
        return JSONResponse(
            status_code=400,
            content={
                "message": "CategorÃƒÆ’Ã‚Â­a no vÃƒÆ’Ã‚Â¡lida. Debe ser Gratis, Plus o Pro",
                "data": None,
                "success": False
            }
        )
    return JSONResponse(
        status_code=400,
        content={
            "message": "Las secciones no pueden estar vacÃƒÆ’Ã‚Â­as",
>>>>>>> origin/development
            "data": None,
            "success": False
        }
    )

<<<<<<< HEAD
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
=======
app.include_router(validacion_router)
app.include_router(hoja_de_vida_router)
app.include_router(usuario_router)
app.include_router(plantilla_router)
app.include_router(planes_router)
app.include_router(pagos_router)
>>>>>>> origin/development
