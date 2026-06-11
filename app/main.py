# app/main.py
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from app.api.v1.validacion_router import router as validacion_router
from app.api.v1.hoja_de_vida_router import router as hoja_de_vida_router
from app.api.v1.usuario_router import router as usuario_router
from app.api.v1.plantilla_router import router as plantilla_router

app = FastAPI(
    title="API de GestiÃ³n de Hojas de Vida",
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
                "message": "CategorÃ­a no vÃ¡lida. Debe ser Gratis, Plus o Pro",
                "data": None,
                "success": False
            }
        )
    return JSONResponse(
        status_code=400,
        content={
            "message": "Las secciones no pueden estar vacÃ­as",
            "data": None,
            "success": False
        }
    )

app.include_router(validacion_router)
app.include_router(hoja_de_vida_router)
app.include_router(usuario_router)
app.include_router(plantilla_router)