# app/domain/hoja_de_vida.py

from pydantic import BaseModel, Field
from typing import Dict, Optional


class SeccionesUpdate(BaseModel):
    secciones: Dict[str, str] = Field(..., description="Diccionario con los nombres de las secciones y sus textos")


class SeccionRequest(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    titulo: Optional[str] = None
    telefono: Optional[str] = None
    email: Optional[str] = None
    direccion: Optional[str] = None
    perfil: Optional[str] = None
    habilidades: Optional[str] = None


class SeccionResponse(BaseModel):
    message: str
    data: Optional[dict]
    success: bool


class ExperienciaRequest(BaseModel):
    empresa: Optional[str] = None
    cargo: Optional[str] = None
    fechaInicio: Optional[str] = None
    fechaFin: Optional[str] = None


class EducacionRequest(BaseModel):
    institucion: Optional[str] = None
    titulo: Optional[str] = None
    fechaInicio: Optional[str] = None
    fechaFin: Optional[str] = None


class BloqueResponse(BaseModel):
    message: str
    data: Optional[dict]
    success: bool


class FinalizarResponse(BaseModel):
    message: str
    data: Optional[dict]
    success: bool


class HojaDeVida:
    def __init__(self, id: int, usuario_id: int, plantilla_id: int = None, datos: dict = None):
        self.id = id
        self.usuario_id = usuario_id
        self.plantilla_id = plantilla_id
        self.datos = datos if datos is not None else {}
        self.estado = "borrador"

    def to_dict(self):
        return {
            "id": self.id,
            "estado": self.estado
        }
