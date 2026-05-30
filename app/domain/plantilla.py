# app/domain/plantilla.py
from enum import Enum
from pydantic import BaseModel, Field
from typing import List

# =====================================================================
# ENUMS (HU-06)
# =====================================================================
class CategoriaPlan(str, Enum):
    GRATIS = "Gratis"
    PLUS = "Plus"
    PRO = "Pro"

# =====================================================================
# ESQUEMAS DE PETICIÓN (PYDANTIC)
# =====================================================================
class PlantillaCreate(BaseModel):
    nombre: str = Field(..., description="Nombre de la plantilla")
    secciones: List[str] = Field(..., description="Lista de secciones generales")
    categoria: CategoriaPlan = Field(default=CategoriaPlan.GRATIS, description="Categoría inicial de la plantilla")

class PlantillaUpdateObligatorios(BaseModel):
    campos_obligatorios: List[str] = Field(..., description="Lista de campos que serán obligatorios")

class PlantillaUpdateCategoria(BaseModel):
    categoria: CategoriaPlan = Field(..., description="Nueva categoría asignada a la plantilla (Gratis, Plus, Pro)")

# =====================================================================
# ENTIDAD DE DOMINIO (OBJETO DE NEGOCIO)
# =====================================================================
class Plantilla:
    def __init__(self, id: int, nombre: str, secciones: List[str], categoria: str):
        self.id = id
        self.nombre = nombre
        self.secciones = secciones
        self.categoria = categoria
        self.campos_obligatorios: List[str] = [] 
        self.activa: bool = True  # <--- Agregado para la HU-09

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "secciones": self.secciones,
            "categoria": self.categoria,
            "camposObligatorios": self.campos_obligatorios,
            "activa": self.activa
        }