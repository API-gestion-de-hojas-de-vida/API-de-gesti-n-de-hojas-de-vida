from fastapi import APIRouter
from fastapi.responses import JSONResponse
from domain.plantilla import PlantillaResponse, ReporteUsoResponse, CatalogoResponse
from service.plantilla_service import PlantillaService
from repository.plantilla_repository import plantilla_repository

router = APIRouter(
    prefix="/api/v1/plantillas",
    tags=["Plantillas"],
)

service = PlantillaService(repo=plantilla_repository)

@router.get("")
def obtener_catalogo():
    """Retorna el catálogo de plantillas activas con indicador de pago."""
    try:
        resultado = service.obtener_catalogo()
        if not resultado.success:
            return JSONResponse(status_code=500, content=resultado.dict())
        return JSONResponse(status_code=200, content=resultado.dict())
    except Exception:
        return JSONResponse(
            status_code=500,
            content={
                "message": "No fue posible obtener el catálogo",
                "data": [],
                "success": False
            }
        )

@router.get("/reporte-uso")
def reporte_uso():
    """Retorna el reporte de uso de todas las plantillas."""
    try:
        resultado = service.reporte_uso()
        if not resultado.success:
            return JSONResponse(status_code=500, content=resultado.dict())
        return JSONResponse(status_code=200, content=resultado.dict())
    except Exception:
        return JSONResponse(
            status_code=500,
            content={
                "message": "No fue posible generar el reporte",
                "data": [],
                "success": False
            }
        )

@router.patch("/{id}/desactivar")
def desactivar_plantilla(id: int):
    """Desactiva una plantilla por su ID (borrado lógico)."""
    try:
        resultado = service.desactivar(id)
        if not resultado.success:
            if "no encontrada" in resultado.message:
                return JSONResponse(status_code=404, content=resultado.dict())
            if "ya se encuentra" in resultado.message:
                return JSONResponse(status_code=409, content=resultado.dict())
        return JSONResponse(status_code=200, content=resultado.dict())
    except Exception:
        return JSONResponse(
            status_code=500,
            content={
                "message": "No fue posible desactivar la plantilla",
                "data": None,
                "success": False
            }
        )