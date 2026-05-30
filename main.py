from fastapi import FastAPI
from api.usuario_router import router as usuario_router
from api.plantilla_router import router as plantilla_router

app = FastAPI(
    title="API Gestión Hojas de Vida",
    description="API REST con arquitectura de capas — FastAPI",
    version="1.0.0",
)

app.include_router(usuario_router)
app.include_router(plantilla_router)

@app.get("/", tags=["Root"])
def root():
    return {
        "message": "API corriendo correctamente 🚀",
        "docs": "http://127.0.0.1:8000/docs",
        "version": "1.0.0",
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)