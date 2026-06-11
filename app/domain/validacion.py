# app/domain/validacion.py

from pydantic import BaseModel
from typing import Optional, List


class ErrorCampo(BaseModel):
    campo: str
    mensaje: str


class ValidacionRequest(BaseModel):
    nombre: Optional[str] = None
    email: Optional[str] = None
    telefono: Optional[str] = None
    experiencia: Optional[List[dict]] = None
    educacion: Optional[List[dict]] = None


class ValidacionResponse(BaseModel):
    message: str
    data: Optional[dict]
    success: bool