# app/domain/hoja_de_vida.py
from pydantic import BaseModel, Field
from typing import Dict

class SeccionesUpdate(BaseModel):
    secciones: Dict[str, str] = Field(..., description="Diccionario con los nombres de las secciones y sus textos")

class HojaDeVida:
    def __init__(self, id: int, usuario_id: int, plantilla_id: int = None, datos: dict = None):
        self.id = id
        self.usuario_id = usuario_id
        self.plantilla_id = plantilla_id  # Puede inicializarse en None
        self.datos = datos if datos is not None else {}
        self.estado = "borrador"  # Estados: borrador, finalizada

    def to_dict(self):
        return {
            "id": self.id,
            "estado": self.estado
        }