# app/api/v1/hoja_de_vida_router.py
<<<<<<< HEAD
from fastapi import APIRouter, Header, Response, status
from fastapi.responses import JSONResponse
from app.domain.hoja_de_vida import SeccionesUpdate
from app.services.hoja_de_vida_service import (
    HojaDeVidaService, NoEncontradoException, 
    CamposFaltantesException, LongitudInvalidaException, ExportacionInvalidaException
)
from app.repositories.hoja_de_vida_repository import hoja_de_vida_repository
from app.repositories.plantilla_repository import plantilla_repository

router = APIRouter(
    prefix="/api/v1/hojas-de-vida",
    tags=["Hojas de Vida"]
)

service = HojaDeVidaService(hoja_de_vida_repository, plantilla_repository)

@router.post("/{id}/secciones", status_code=200)
def guardar_secciones(id: int, datos: SeccionesUpdate):
    try:
        hv_actualizada = service.guardar_secciones(id, datos.secciones)
        return JSONResponse(status_code=200, content={
            "mensaje": "Información guardada exitosamente",
            "data": {"id": hv_actualizada.id},
            "success": True
        })
    except NoEncontradoException as e:
        return JSONResponse(status_code=404, content={"mensaje": str(e), "data": None, "success": False})
    except LongitudInvalidaException as e:
        return JSONResponse(status_code=400, content={"mensaje": str(e), "data": None, "success": False})

@router.post("/{id}/finalizar", status_code=200)
def finalizar_hoja_de_vida(id: int):
    try:
        hv_finalizada = service.finalizar_hoja_de_vida(id)
        return JSONResponse(status_code=200, content={
            "mensaje": "Hoja de vida finalizada exitosamente",
            "data": hv_finalizada.to_dict(),
            "success": True
        })
    except NoEncontradoException as e:
        return JSONResponse(status_code=404, content={"mensaje": str(e), "data": None, "success": False})
    except (CamposFaltantesException, ExportacionInvalidaException) as e:
        faltantes = e.faltantes if hasattr(e, 'faltantes') else None
        return JSONResponse(status_code=400, content={
            "mensaje": str(e),
            "data": {"camposFaltantes": faltantes} if faltantes else None,
            "success": False
        })

# ==========================================
# HU-21: ENDPOINT DE EXPORTACIÓN PDF
# ==========================================
@router.get("/{id}/exportar/pdf")
def exportar_hoja_de_vida_pdf(
    id: int,
    x_user_id: int = Header(1, description="ID del usuario autenticado"),
    x_user_name: str = Header("Fabian_Torres", description="Nombre del usuario para el archivo"),
    x_user_plan: str = Header("Gratis", description="Plan del usuario: Gratis, Plus, Pro")
):
    try:
        pdf_bytes, nombre_archivo = service.preparar_exportacion_pdf(
            id=id, 
            usuario_id=x_user_id, 
            plan_usuario=x_user_plan, 
            nombre_usuario=x_user_name
        )
        
        # Caso 1: Retorno exitoso del archivo binario descargable
        headers = {"Content-Disposition": f"attachment; filename={nombre_archivo}"}
        return Response(content=pdf_bytes, media_type="application/pdf", headers=headers)

    except NoEncontradoException as e:
        return JSONResponse(status_code=404, content={"mensaje": str(e), "data": None, "success": False})
        
    except ExportacionInvalidaException as e:
        # Casos 2 y 3: Validaciones de negocio fallidas (sin finalizar o sin plantilla)
        return JSONResponse(status_code=400, content={"mensaje": str(e), "data": None, "success": False})
=======

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
>>>>>>> origin/development
