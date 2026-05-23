from fastapi import APIRouter, HTTPException, status
from domain.usuario import LoginRequest, LoginResponse, LogoutRequest, LogoutResponse
from service.usuario_service import UsuarioService
from repository.usuario_repository import usuario_repository

router = APIRouter(
    prefix="/api/v1/usuarios",
    tags=["Usuarios"],
)

service = UsuarioService(repo=usuario_repository)

@router.post("/login", response_model=LoginResponse)
def login(datos: LoginRequest):
    """Autentica un usuario con email y contraseña."""
    try:
        return service.login(datos)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

        from domain.usuario import LoginRequest, LoginResponse, LogoutRequest, LogoutResponse

@router.post("/logout", response_model=LogoutResponse)
def logout(datos: LogoutRequest):
    """Cierra la sesión invalidando el token activo."""
    try:
        return service.logout(datos.token)
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )