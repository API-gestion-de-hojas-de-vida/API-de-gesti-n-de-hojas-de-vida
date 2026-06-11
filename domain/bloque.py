# domain/bloque.py

from pydantic import BaseModel, field_validator
from typing import Optional
from datetime import date


class ExperienciaRequest(BaseModel):
    empresa: str
    cargo: str
    fechaInicio: str
    fechaFin: Optional[str] = None

    @field_validator("empresa", "cargo", mode="before")
    @classmethod
    def campos_obligatorios(cls, v):
        if not v or str(v).strip() == "":
            raise ValueError("Los campos empresa y cargo son obligatorios")
        return v.strip()

    @field_validator("fechaInicio", mode="before")
    @classmethod
    def fecha_inicio_valida(cls, v):
        try:
            date.fromisoformat(str(v))
        except ValueError:
            raise ValueError("El formato de fecha debe ser YYYY-MM-DD")
        return v


class EducacionRequest(BaseModel):
    institucion: str
    titulo: str
    fechaInicio: str
    fechaFin: Optional[str] = None

    @field_validator("institucion", "titulo", mode="before")
    @classmethod
    def campos_obligatorios(cls, v):
        if not v or str(v).strip() == "":
            raise ValueError("Los campos institucion y titulo son obligatorios")
        return v.strip()

    @field_validator("fechaInicio", mode="before")
    @classmethod
    def fecha_inicio_valida(cls, v):
        try:
            date.fromisoformat(str(v))
        except ValueError:
            raise ValueError("El formato de fecha debe ser YYYY-MM-DD")
        return v


class BloqueResponse(BaseModel):
    message: str
    data: Optional[dict]
    success: bool


class Bloque:
    def __init__(self, id: int, tipo: str, datos: dict):
        self.id = id
        self.tipo = tipo
        self.datos = datos

    def to_response(self) -> dict:
        return {"id": self.id, "tipo": self.tipo, **self.datos}