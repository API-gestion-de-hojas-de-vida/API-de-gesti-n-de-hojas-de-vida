# app/api/v1/plantilla_router.py
from fastapi import APIRouter, HTTPException, status, Header
from pydantic import ValidationError
from app.domain.plantilla import PlantillaCreate
from app.services.plantilla_service import PlantillaService, DuplicadoException, AutorizacionException
from app.repositories.plantilla_repository import plantilla_repository
from app.domain.plantilla import PlantillaCreate, PlantillaUpdateObligatorios
from app.services.plantilla_service import (
    PlantillaService, DuplicadoException, AutorizacionException, 
    NoEncontradoException, CamposInvalidosException
)

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

@router.patch("/{id}/campos-obligatorios", status_code=status.HTTP_200_OK)
def actualizar_campos_obligatorios(
    id: int,
    datos: PlantillaUpdateObligatorios,
    x_user_role: str = Header(..., description="Simulación del rol del Token")
):
    try:
        plantilla_actualizada = service.actualizar_campos_obligatorios(id, datos.campos_obligatorios, x_user_role)
        
        # Caso 1: Actualización exitosa
        return {
            "mensaje": "Campos obligatorios actualizados exitosamente",
            "data": {
                "id": plantilla_actualizada.id,
                "nombre": plantilla_actualizada.nombre,
                "camposObligatorios": plantilla_actualizada.campos_obligatorios
            },
            "success": True
        }
        
    except AutorizacionException as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))
        
    except NoEncontradoException as e:
        # Caso 2: Plantilla no encontrada (404)
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "mensaje": str(e),
                "data": None,
                "success": False
            }
        )
        
    except CamposInvalidosException as e:
        # Caso 3: Campos inválidos (400)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={
                "mensaje": str(e),
                "data": None,
                "success": False
            }
        )