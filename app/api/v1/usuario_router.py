from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from typing import Optional
from app.services.usuarioapi import (
    UsuarioService,
    EmailDuplicadoError,
    ContrasenaInvalidaError,
    CredencialesInvalidasError,
    CorreoNoRegistradoError,
    CamposObligatoriosError,
    TokenInvalidoError,
    SuscripcionException,
    NoAutenticadoException
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
            "message": "Registro exitoso",
            "data": {"id": usuario.id, "nombre": usuario.nombre, "email": usuario.email, "rol": usuario.rol},
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


class LogoutRequest(BaseModel):
    token: str

@router.post("/logout")
def logout(body: LogoutRequest):
    if not body.token:
        return JSONResponse(status_code=401, content={
            "message": "Sesión no válida o ya expirada",
            "data": None,
            "success": False,
        })
    token = body.token
    try:
        _servicio.cerrar_sesion(token)
        return JSONResponse(status_code=200, content={
            "message": "Sesión cerrada exitosamente",
            "data": None,
            "success": True,
        })
    except TokenInvalidoError:
        return JSONResponse(status_code=401, content={
            "message": "Sesión no válida o ya expirada",
            "data": None,
            "success": False,
        })


@router.post("/suscripcion/cancelar", status_code=200)
def cancelar_suscripcion(
    x_user_id: int = Header(..., description="ID del usuario obtenido del token"),
    x_autenticado: bool = Header(True, description="Simulación de estado de autenticación")
):
    try:
        resultado = _servicio.cancelar_suscripcion_plus(user_id=x_user_id, autenticado=x_autenticado)
        return JSONResponse(status_code=200, content=resultado)
    except NoAutenticadoException as e:
        return JSONResponse(
            status_code=401,
            content={"mensaje": str(e), "data": None, "success": False}
        )
    except SuscripcionException as e:
        return JSONResponse(
            status_code=409,
            content={"mensaje": str(e), "data": None, "success": False}
        )