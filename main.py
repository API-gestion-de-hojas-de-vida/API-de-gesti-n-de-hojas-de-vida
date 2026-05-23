# main.py

from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.api.usuarioapi import router as usuario_router


app = FastAPI(
    title="API Gestión Hojas de Vida",
    description="API REST con arquitectura de capas — FastAPI",
    version="1.0.0",
)


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

@app.get("/", tags=["Root"])
def root():
    return {
        "mensaje": "API corriendo correctamente",
        "docs": "http://127.0.0.1:8000/docs",
        "version": "1.0.0",
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)