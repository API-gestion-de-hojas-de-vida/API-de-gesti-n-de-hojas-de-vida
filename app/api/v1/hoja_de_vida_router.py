# app/api/v1/hoja_de_vida_router.py
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