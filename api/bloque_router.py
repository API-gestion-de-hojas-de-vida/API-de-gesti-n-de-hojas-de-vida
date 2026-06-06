# api/bloque_router.py

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from domain.bloque import ExperienciaRequest, EducacionRequest, BloqueResponse
from service.bloque_service import BloqueService
from repository.bloque_repository import bloque_repository


router = APIRouter(
    prefix="/api/v1/hojas-de-vida",
    tags=["Bloques"],
)

service = BloqueService(repo=bloque_repository)


@router.post(
    "/{id}/experiencia",
    status_code=status.HTTP_201_CREATED,
    response_model=BloqueResponse,
    summary="Agregar bloque de experiencia laboral",
)
def agregar_experiencia(id: int, datos: ExperienciaRequest):
    resultado = service.agregar_experiencia(hoja_id=id, datos=datos)
    if not resultado.success:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message": resultado.message,
                "data": None,
                "success": False,
            },
        )
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "message": resultado.message,
            "data": resultado.data,
            "success": True,
        },
    )


@router.post(
    "/{id}/educacion",
    status_code=status.HTTP_201_CREATED,
    response_model=BloqueResponse,
    summary="Agregar bloque de educación",
)
def agregar_educacion(id: int, datos: EducacionRequest):
    resultado = service.agregar_educacion(hoja_id=id, datos=datos)
    if not resultado.success:
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={
                "message": resultado.message,
                "data": None,
                "success": False,
            },
        )
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "message": resultado.message,
            "data": resultado.data,
            "success": True,
        },
    )