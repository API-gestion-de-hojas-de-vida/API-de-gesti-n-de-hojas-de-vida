from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/api/v1/plantillas", tags=["Plantillas"])
service = None # Se asume inyección externa o inicialización global previa

@router.get("/{id}/preview")
def obtener_vista_previa_plantilla(id: int):
    try:
        resultado = service.obtener_preview(id)
        return JSONResponse(
            status_code=resultado["status_code"], 
            content=resultado["response"]
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "message": f"Error interno al procesar la vista previa: {str(e)}",
                "data": None,
                "success": False
            }
        )
