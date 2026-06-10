# app/api/v1/plantilla_router.py
from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from app.domain.plantilla import PlantillaCreate
from app.services.plantilla_service import PlantillaService, DuplicadoException, AutorizacionException
from app.repositories.plantilla_repository import plantilla_repository

router = APIRouter(
    prefix="/api/v1/plantillas",
    tags=["Plantillas"]
)

service = PlantillaService(repo=plantilla_repository)

@router.post("/", status_code=201)
def crear_plantilla(datos: PlantillaCreate, x_user_role: str = Header(..., description="Simulación del rol del Token")):
    try:
        nueva_plantilla = service.crear_plantilla(datos, rol_usuario=x_user_role)
        return JSONResponse(status_code=201, content={
            "message": "Plantilla creada exitosamente",
            "data": nueva_plantilla.to_dict(),
            "success": True
        })
    except AutorizacionException:
        return JSONResponse(status_code=403, content={
            "message": "Solo el rol Administrador puede consumir este endpoint",
            "data": None,
            "success": False
        })
    except DuplicadoException:
        return JSONResponse(status_code=409, content={
            "message": "Ya existe una plantilla con ese nombre",
            "data": None,
            "success": False
        })