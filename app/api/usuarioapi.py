# app/api/usuarioapi.py

from typing import Any, Optional

from fastapi import APIRouter, Depends, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, Field, field_validator, model_validator

from app.services.usuarioapi import (
    ContrasenaInvalidaError,
    EmailDuplicadoError,
    UsuarioService,
)
from app.repositories.usuarioapi import UsuarioRepositoryMemoria


router = APIRouter(prefix="/api/v1/usuarios", tags=["Usuarios"])


# ─── Schemas Pydantic ─────────────────────────────────────────────────────────

class RegistroRequestSchema(BaseModel):

    nombre: str = Field(..., min_length=1)
    email: EmailStr = Field(...)
    contrasena: str = Field(..., min_length=1)

    @model_validator(mode="before")
    @classmethod
    def campos_no_vacios(cls, valores: dict) -> dict:
        campos = ["nombre", "email", "contrasena"]
        for campo in campos:
            valor = valores.get(campo)
            if valor is None or str(valor).strip() == "":
                raise ValueError("Todos los campos son obligatorios")
        return valores

    @field_validator("nombre", mode="before")
    @classmethod
    def limpiar_nombre(cls, v: str) -> str:
        return v.strip()

    @field_validator("email", mode="before")
    @classmethod
    def limpiar_email(cls, v: str) -> str:
        return v.strip().lower()


class UsuarioResponseData(BaseModel):
    id: int
    nombre: str
    email: str
    rol: str


class APIResponse(BaseModel):
    message: str
    data: Optional[UsuarioResponseData]
    success: bool


# ─── Inyección de dependencias ────────────────────────────────────────────────

_repositorio = UsuarioRepositoryMemoria()

def get_usuario_service() -> UsuarioService:
    return UsuarioService(_repositorio)

# ─── Endpoint ─────────────────────────────────    
@router.post(
    "/registro",
    status_code=status.HTTP_201_CREATED,
    response_model=APIResponse,
    summary="Registro de nuevo usuario",
)
async def registrar_usuario(
    payload: RegistroRequestSchema,
    service: UsuarioService = Depends(get_usuario_service),
) -> Any:
    try:
        usuario = service.registrar_usuario(
            nombre=payload.nombre,
            email=str(payload.email),
            contrasena=payload.contrasena,
        )
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": "Registro exitoso",
                "data": {
                    "id": usuario.id,
                    "nombre": usuario.nombre,
                    "email": usuario.email,
                    "rol": usuario.rol,
                },
                "success": True,
            },
        )

    except ContrasenaInvalidaError as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "message": str(e),
                "data": None,
                "success": False,
            },
        )

    except EmailDuplicadoError as e:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={
                "message": str(e),
                "data": None,
                "success": False,
            },
        )