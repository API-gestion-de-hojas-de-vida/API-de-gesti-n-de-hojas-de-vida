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

class CatalogoResponse(BaseModel):
    message: str
    data: list
    success: bool

class Plantilla:
    def __init__(self, id: int, nombre: str, categoria: str, estado: str = "activo"):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria
        self.estado = estado

    def esta_activa(self) -> bool:
        return self.estado == "activo"

    def desactivar(self):
        self.estado = "inactivo"

    def es_de_pago(self) -> bool:
        return self.categoria in ["Plus", "Pro"]

    def to_response(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "estado": self.estado
        }

    def to_catalogo(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "esDePago": self.es_de_pago()
        }