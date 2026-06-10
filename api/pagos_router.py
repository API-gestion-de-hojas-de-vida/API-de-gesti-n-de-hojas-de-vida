from fastapi import APIRouter, Header, Body
from fastapi.responses import JSONResponse
from typing import Optional
from service.pagos_service import PagosService

router = APIRouter(prefix="/api/v1/pagos", tags=["Pagos"])
pagos_service = PagosService()

@router.post(
    "/plantillas/{id}/comprar",
    status_code=201,
    summary="Compra de Plantilla Pro Individual",
    description="Permite a un usuario adquirir una plantilla Pro de forma individual con acceso permanente tras un pago exitoso."
)
def comprar_plantilla(
    id: int,
    x_user_id: Optional[int] = Header(1, alias="X-User-Id"), # Default usuario 1 para pruebas
    payload: dict = Body(...) # Recibe {"token_tarjeta": "xyz"}
):
    try:
        token = payload.get("token_tarjeta", "")
        if not token:
            return JSONResponse(
                status_code=400, 
                content={"mensaje": "El token de la tarjeta es requerido", "data": None, "success": False}
            )
            
        resultado = pagos_service.comprar_plantilla_pro(
            usuario_id=x_user_id, 
            plantilla_id=id, 
            token_tarjeta=token
        )
        return JSONResponse(
            status_code=resultado["status_code"],
            content=resultado["response"]
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "mensaje": f"Error interno en la pasarela de pagos: {str(e)}",
                "data": None,
                "success": False
            }
        )