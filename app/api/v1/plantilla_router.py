# app/api/v1/plantilla_router.py
from fastapi import APIRouter, HTTPException, status, Header
from pydantic import ValidationError
from app.domain.plantilla import PlantillaCreate
from app.services.plantilla_service import PlantillaService, DuplicadoException, AutorizacionException
from app.repositories.plantilla_repository import plantilla_repository

router = APIRouter(
    prefix="/api/v1/plantillas",
    tags=["Plantillas"]
)

service = PlantillaService(repo=plantilla_repository)

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_plantilla(datos: PlantillaCreate, x_user_role: str = Header(..., description="Simulación del rol del Token")):
    try:
        nueva_plantilla = service.crear_plantilla(datos, rol_usuario=x_user_role)
        
        # Estructura JSON solicitada para Éxito
        return {
            "message": "Plantilla creada exitosamente",
            "data": nueva_plantilla.to_dict(),
            "success": True
        }
        
    except AutorizacionException as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))
        
    except DuplicadoException:
        # Caso 2: Estructura JSON solicitada para Duplicado (409 Conflict)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={
                "message": "Ya existe una plantilla con ese nombre",
                "data": None,
                "success": False
            }
        )