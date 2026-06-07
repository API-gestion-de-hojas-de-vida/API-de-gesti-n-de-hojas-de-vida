# app/api/v1/usuario_router.py
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.services.usuarioapi import (
    UsuarioService,
    EmailDuplicadoError,
    ContrasenaInvalidaError,
    CredencialesInvalidasError,
    CorreoNoRegistradoError,
    CamposObligatoriosError,
)
from app.repositories.usuarioapi import UsuarioRepositoryMemoria
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/usuarios", tags=["Usuarios"])

_repositorio = UsuarioRepositoryMemoria()
_servicio = UsuarioService(_repositorio)


class RegistroRequest(BaseModel):
    nombre: str
    email: str
    contrasena: str


class LoginRequest(BaseModel):
    email: str
    contrasena: str


@router.post("/registro")
def registrar(body: RegistroRequest):
    try:
        usuario = _servicio.registrar_usuario(
            nombre=body.nombre,
            email=body.email,
            contrasena=body.contrasena,
        )
        return JSONResponse(status_code=201, content={
            "message": "Usuario registrado exitosamente",
            "data": {"id": usuario.id, "nombre": usuario.nombre, "email": usuario.email},
            "success": True,
        })
    except CamposObligatoriosError:
        return JSONResponse(status_code=400, content={
            "message": "Todos los campos son obligatorios",
            "data": None,
            "success": False,
        })
    except ContrasenaInvalidaError as e:
        return JSONResponse(status_code=400, content={
            "message": str(e),
            "data": None,
            "success": False,
        })
    except EmailDuplicadoError:
        return JSONResponse(status_code=409, content={
            "message": "El correo ya está registrado",
            "data": None,
            "success": False,
        })


@router.post("/login")
def login(body: LoginRequest):
    try:
        resultado = _servicio.iniciar_sesion(
            email=body.email,
            contrasena=body.contrasena,
        )
        return JSONResponse(status_code=200, content={
            "message": "Inicio de sesión exitoso",
            "data": resultado,
            "success": True,
        })
    except CamposObligatoriosError:
        return JSONResponse(status_code=400, content={
            "message": "Todos los campos son obligatorios",
            "data": None,
            "success": False,
        })
    except CorreoNoRegistradoError:
        return JSONResponse(status_code=404, content={
            "message": "Correo o contraseña incorrectos",
            "data": None,
            "success": False,
        })
    except CredencialesInvalidasError:
        return JSONResponse(status_code=401, content={
            "message": "Correo o contraseña incorrectos",
            "data": None,
            "success": False,
        })