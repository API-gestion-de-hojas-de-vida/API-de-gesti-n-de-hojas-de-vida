# app/domain/plantilla.py
from enum import Enum
from pydantic import BaseModel, Field
from typing import List

# =====================================================================
# 1. ENUMS Y VALIDACIONES DE ESTRUCTURA (HU-06)
# =====================================================================

class CategoriaPlan(str, Enum):
    GRATIS = "Gratis"
    PLUS = "Plus"
    PRO = "Pro"


# =====================================================================
# 2. ESQUEMAS DE PETICIÓN (PYDANTIC MODELS)
# =====================================================================

# Restaurado: Esquema de creación que requería el enrutador (HU-04)
class PlantillaCreate(BaseModel):
    nombre: str = Field(..., description="Nombre de la plantilla")
    secciones: List[str] = Field(..., description="Lista de secciones generales")
    categoria: CategoriaPlan = Field(default=CategoriaPlan.GRATIS, description="Categoría inicial de la plantilla")

# Esquema para actualización de campos obligatorios (HU-05)
class PlantillaUpdateObligatorios(BaseModel):
    campos_obligatorios: List[str] = Field(..., description="Lista de campos que serán obligatorios")

# Nuevo: Esquema para actualización de categoría por plan (HU-06)
class PlantillaUpdateCategoria(BaseModel):
    categoria: CategoriaPlan = Field(..., description="Nueva categoría asignada a la plantilla (Gratis, Plus, Pro)")


# =====================================================================
# 3. ENTIDAD DE DOMINIO (OBJETO DE NEGOCIO)
# =====================================================================

class Plantilla:
    def __init__(self, id: int, nombre: str, secciones: List[str], categoria: str):
        self.id = id
        self.nombre = nombre
        self.secciones = secciones
        self.categoria = categoria
        self.campos_obligatorios: List[str] = []  # Se inicializa vacío (HU-05)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "secciones": self.secciones,
            "categoria": self.categoria,
            "camposObligatorios": self.campos_obligatorios
        }