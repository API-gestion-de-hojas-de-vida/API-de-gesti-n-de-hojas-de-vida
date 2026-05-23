# main.py

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.api.usuarioapi import router as usuario_router


app = FastAPI(title="API de Gestión de Hojas de Vida")


# ─── Manejador global de errores de validación Pydantic ──────────────────────

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={
            "message": "Todos los campos son obligatorios",
            "data": None,
            "success": False,
        },
    )


# ─── Routers ──────────────────────────────────────────────────────────────────

app.include_router(usuario_router)


# ─── Ruta raíz ────────────────────────────────────────────────────────────────

@app.get("/")
def read_root():
    return {
        "message": "Bienvenido a la API de Gestión de Hojas de Vida",
        "status": "Ready"
    }