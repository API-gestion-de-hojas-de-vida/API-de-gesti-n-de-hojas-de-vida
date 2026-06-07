# app/domain/plantilla.py
from pydantic import BaseModel, Field, field_validator
from typing import Optional, List

# Schema de Entrada: Valida lo que envía el cliente
class PlantillaCreate(BaseModel):
    nombre: str = Field(..., description="Nombre de la plantilla")
    secciones: List[str] = Field(..., description="Lista de secciones que componen la plantilla")
    categoria: str = Field("Gratis", description="Categoría de la plantilla")

    # Criterio de Aceptación: Aplicar trim al nombre
    @field_validator("nombre")
    @classmethod
    def limpiar_nombre(cls, v):
        return v.strip()

    # Criterio de Aceptación: Al menos un elemento y sin strings vacíos
    @field_validator("secciones")
    @classmethod
    def validar_secciones(cls, v):
        if not v or len(v) == 0:
            raise ValueError("Las secciones no pueden estar vacías")
        if any(not seccion.strip() for seccion in v):
            raise ValueError("Las secciones no pueden contener elementos vacíos")
        return [seccion.strip() for seccion in v]

# Entidad del Modelo de Negocio
class Plantilla:
    def __init__(self, id: int, nombre: str, secciones: List[str], categoria: str):
        self.id = id
        self.nombre = nombre
        self.secciones = secciones
        self.categoria = categoria

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "secciones": self.secciones,
            "categoria": self.categoria
        }