from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from typing import Optional
from service.planes_service import PlanesService

router = APIRouter(prefix="/api/v1/planes", tags=["Planes"])
planes_service = PlanesService(usuario_repo=None)

@router.get("/plus")
def obtener_plan_plus(
    x_user_id: Optional[int] = Header(None, alias="X-User-Id"),
    x_user_plan: Optional[str] = Header("Gratis", alias="X-User-Plan")
):
    try:
        resultado = planes_service.obtener_informacion_plus(usuario_id=x_user_id, plan_actual=x_user_plan)
        return JSONResponse(
            status_code=resultado["status_code"],
            content=resultado["response"]
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "mensaje": f"Error interno al procesar la solicitud del plan: {str(e)}",
                "data": None,
                "success": False
            }
        )