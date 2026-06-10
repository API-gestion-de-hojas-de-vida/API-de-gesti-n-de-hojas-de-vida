# app/api/v1/validacion_router.py

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.domain.validacion import ValidacionRequest, ValidacionResponse
from app.services.validacion_service import ValidacionService
from app.repositories.hoja_repository import hoja_repository


router = APIRouter(
    prefix="/api/v1/hojas-de-vida",
    tags=["Validacion"],
)

service = ValidacionService(repo=hoja_repository)


@router.post(
    "/{id}/validar",
    summary="Validar formulario de hoja de vida",
)
def validar_formulario(id: int, datos: ValidacionRequest):

    resultado = service.validar_formulario(hoja_id=id, datos=datos)

    if not resultado.success and resultado.data is None:
        # Hoja de vida no existe
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message": resultado.message,
                "data": None,
                "success": False,
            },
        )

    if not resultado.success:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "message": resultado.message,
                "data": resultado.data,
                "success": False,
            },
        )

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": resultado.message,
            "data": None,
            "success": True,
        },
    )