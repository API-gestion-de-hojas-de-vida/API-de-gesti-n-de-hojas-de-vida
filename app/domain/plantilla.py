# app/domain/plantilla.py
from enum import Enum
from pydantic import BaseModel, Field, field_validator
from typing import List


class CategoriaPlan(str, Enum):
    GRATIS = "Gratis"
    PLUS = "Plus"
    PRO = "Pro"


class PlantillaCreate(BaseModel):
    nombre: str = Field(..., description="Nombre de la plantilla")
    secciones: List[str] = Field(..., description="Lista de secciones que componen la plantilla")
    categoria: str = Field("Gratis", description="Categoría de la plantilla")

    @field_validator("nombre")
    @classmethod
    def limpiar_nombre(cls, v):
        return v.strip()

    @field_validator("secciones")
    @classmethod
    def validar_secciones(cls, v):
        if not v or len(v) == 0:
            raise ValueError("Las secciones no pueden estar vacías")
        if any(not seccion.strip() for seccion in v):
            raise ValueError("Las secciones no pueden contener elementos vacíos")
        return [seccion.strip() for seccion in v]


class PlantillaUpdateObligatorios(BaseModel):
    campos_obligatorios: List[str] = Field(..., description="Lista de campos obligatorios")


class PlantillaUpdateCategoria(BaseModel):
    categoria: CategoriaPlan = Field(..., description="Nueva categoría: Gratis, Plus o Pro")


class Plantilla:
    def __init__(self, id: int, nombre: str, secciones: List[str], categoria: str):
        self.id = id
        self.nombre = nombre
        self.secciones = secciones
        self.categoria = categoria
        self.campos_obligatorios: List[str] = []
        self.activa: bool = True

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "secciones": self.secciones,
            "categoria": self.categoria,
            "camposObligatorios": self.campos_obligatorios,
            "activa": self.activa
        }