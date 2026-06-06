from fastapi import APIRouter
from fastapi.responses import JSONResponse
from domain.usuario import LoginRequest, LogoutRequest
from service.usuario_service import usuario_service

router = APIRouter(
    prefix="/api/v1/usuarios",
    tags=["Usuarios"],
)

@router.post("/login")
def login(datos: LoginRequest):
    """Endpoint para el inicio de sesión de usuarios (HU-02)."""
    try:
        resultado = usuario_service.login(datos)
        if not resultado.success:
            return JSONResponse(status_code=401, content=resultado.dict())
        return JSONResponse(status_code=200, content=resultado.dict())
    except Exception:
        return JSONResponse(
            status_code=500,
            content={
                "message": "No fue posible iniciar sesión",
                "data": None,
                "success": False
            }
        )

@router.post("/logout")
def logout(datos: LogoutRequest):
    """Endpoint para el cierre de sesión de usuarios (HU-03)."""
    try:
        resultado = usuario_service.logout(datos)
        if not resultado.success:
            return JSONResponse(status_code=400, content=resultado.dict())
        return JSONResponse(status_code=200, content=resultado.dict())
    except Exception:
        return JSONResponse(
            status_code=500,
            content={
                "message": "No fue posible cerrar sesión",
                "data": None,
                "success": False
            }
        )