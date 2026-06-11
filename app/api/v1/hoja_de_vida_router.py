# app/api/v1/hoja_de_vida_router.py

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from app.domain.hoja_de_vida import SeccionRequest
from app.services.hoja_de_vida_service import HojaDeVidaService
from app.repositories.hoja_repository import hoja_repository


router = APIRouter(
    prefix='/api/v1/hojas-de-vida',
    tags=['Hojas de Vida'],
)

service = HojaDeVidaService(repo=hoja_repository)


@router.post('/{id}/secciones', summary='Guardar secciones de hoja de vida con validacion de longitud')
def guardar_secciones(id: int, datos: SeccionRequest):

    resultado = service.guardar_secciones(hoja_id=id, datos=datos)

    if not resultado.success and 'no existe' in resultado.message:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': resultado.message, 'data': None, 'success': False})

    if not resultado.success:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': resultado.message, 'data': None, 'success': False})

    return JSONResponse(status_code=status.HTTP_200_OK, content={'message': resultado.message, 'data': resultado.data, 'success': True})

from app.domain.hoja_de_vida import ExperienciaRequest, EducacionRequest

@router.post('/{id}/experiencia', summary='Agregar bloque de experiencia laboral')
def agregar_experiencia(id: int, datos: ExperienciaRequest):
    resultado = service.agregar_experiencia(hoja_id=id, datos=datos)
    if not resultado.success and 'no existe' in resultado.message:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': resultado.message, 'data': None, 'success': False})
    if not resultado.success:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': resultado.message, 'data': None, 'success': False})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={'message': resultado.message, 'data': resultado.data, 'success': True})

@router.post('/{id}/educacion', summary='Agregar bloque de educacion')
def agregar_educacion(id: int, datos: EducacionRequest):
    resultado = service.agregar_educacion(hoja_id=id, datos=datos)
    if not resultado.success and 'no existe' in resultado.message:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': resultado.message, 'data': None, 'success': False})
    if not resultado.success:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': resultado.message, 'data': None, 'success': False})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={'message': resultado.message, 'data': resultado.data, 'success': True})

@router.post('/{id}/finalizar', summary='Finalizar hoja de vida')
def finalizar(id: int):
    resultado = service.finalizar(hoja_id=id)
    if not resultado.success and 'no encontrada' in resultado.message:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={'message': resultado.message, 'data': None, 'success': False})
    if not resultado.success:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={'message': resultado.message, 'data': resultado.data, 'success': False})
    return JSONResponse(status_code=status.HTTP_200_OK, content={'message': resultado.message, 'data': resultado.data, 'success': True})
