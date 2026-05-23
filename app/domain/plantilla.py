# app/domain/plantilla.py
from pydantic import BaseModel, Field, field_validator
from typing import Optional, List

# app/domain/plantilla.py
# (Mantén tus importaciones actuales y la clase PlantillaCreate)

class PlantillaUpdateObligatorios(BaseModel):
    campos_obligatorios: List[str] = Field(..., description="Lista de campos que serán obligatorios")

# Actualiza tu entidad Plantilla para incluir el nuevo atributo
class Plantilla:
    def __init__(self, id: int, nombre: str, secciones: List[str], categoria: str):
        self.id = id
        self.nombre = nombre
        self.secciones = secciones
        self.categoria = categoria
        self.campos_obligatorios: List[str] = [] # Se inicializa vacío

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "secciones": self.secciones,
            "categoria": self.categoria,
            "camposObligatorios": self.campos_obligatorios
        }