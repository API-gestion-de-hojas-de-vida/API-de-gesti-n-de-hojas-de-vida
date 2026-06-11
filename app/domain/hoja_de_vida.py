# app/domain/hoja_de_vida.py

from pydantic import BaseModel
from typing import Optional


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
