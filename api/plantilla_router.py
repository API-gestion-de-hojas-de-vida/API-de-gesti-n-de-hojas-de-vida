from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse
from domain.plantilla import PlantillaResponse
from service.plantilla_service import PlantillaService
from repository.plantilla_repository import plantilla_repository

router = APIRouter(
    prefix="/api/v1/plantillas",
    tags=["Plantillas"],
)

service = PlantillaService(repo=plantilla_repository)

@router.patch("/{id}/desactivar")
def desactivar_plantilla(id: int):
    """Desactiva una plantilla por su ID (borrado lógico)."""
    try:
        resultado = service.desactivar(id)
        if not resultado.success:
            if "no encontrada" in resultado.message:
                return JSONResponse(
                    status_code=404,
                    content=resultado.dict()
                )
            if "ya se encuentra" in resultado.message:
                return JSONResponse(
                    status_code=409,
                    content=resultado.dict()
                )
        return JSONResponse(
            status_code=200,
            content=resultado.dict()
        )
    except Exception:
        return JSONResponse(
            status_code=500,
            content={
                "message": "No fue posible desactivar la plantilla",
                "data": None,
                "success": False
            }
        )