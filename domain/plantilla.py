from pydantic import BaseModel
from typing import Optional

class PlantillaResponse(BaseModel):
    message: str
    data: Optional[dict]
    success: bool

class ReporteUsoResponse(BaseModel):
    message: str
    data: list
    success: bool

class Plantilla:
    def __init__(self, id: int, nombre: str, estado: str = "activo"):
        self.id = id
        self.nombre = nombre
        self.estado = estado

    def esta_activa(self) -> bool:
        return self.estado == "activo"

    def desactivar(self):
        self.estado = "inactivo"

    def to_response(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "estado": self.estado
        }