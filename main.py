from fastapi import FastAPI

app = FastAPI(title="API de Gestión de Hojas de Vida")

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Gestión de Hojas de Vida", "status": "Ready"}