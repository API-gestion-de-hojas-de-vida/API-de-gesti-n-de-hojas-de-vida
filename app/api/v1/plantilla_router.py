# app/api/v1/plantilla_router.py
from fastapi import APIRouter, Header, Query, status
from fastapi.responses import JSONResponse
from app.domain.plantilla import PlantillaCreate, PlantillaUpdateObligatorios, PlantillaUpdateCategoria
from app.services.plantilla_service import (
    PlantillaService, DuplicadoException, AutorizacionException,
    NoEncontradoException, CamposInvalidosException, ConflictoException
)
from app.repositories.plantilla_repository import plantilla_repository

router = APIRouter(
    prefix="/api/v1/plantillas",
    tags=["Plantillas"]
)

service = PlantillaService(repo=plantilla_repository)

# ==========================================
# 1. POST - CREAR PLANTILLA (HU-04)
# ==========================================
@router.post("/", status_code=201)
def crear_plantilla(datos: PlantillaCreate, x_user_role: str = Header(..., description="Simulación del rol del Token")):
    try:
        nueva_plantilla = service.crear_plantilla(datos, rol_usuario=x_user_role)
        return JSONResponse(status_code=201, content={
            "message": "Plantilla creada exitosamente",
            "data": nueva_plantilla.to_dict(),
            "success": True
        })
    except AutorizacionException:
        return JSONResponse(status_code=403, content={
            "message": "Solo el rol Administrador puede consumir este endpoint",
            "data": None,
            "success": False
        })
    except DuplicadoException:
        return JSONResponse(status_code=409, content={
            "message": "Ya existe una plantilla con ese nombre",
            "data": None,
            "success": False
        })

# ==========================================
# 2. PATCH - CAMPOS OBLIGATORIOS (HU-05)
# ==========================================
@router.patch("/{id}/campos-obligatorios", status_code=200)
def actualizar_campos_obligatorios(
    id: int,
    datos: PlantillaUpdateObligatorios,
    x_user_role: str = Header(..., description="Simulación del rol del Token")
):
    try:
        plantilla = service.actualizar_campos_obligatorios(id, datos.campos_obligatorios, x_user_role)
        return JSONResponse(status_code=200, content={
            "message": "Campos obligatorios actualizados exitosamente",
            "data": {
                "id": plantilla.id,
                "nombre": plantilla.nombre,
                "camposObligatorios": plantilla.campos_obligatorios
            },
            "success": True
        })
    except AutorizacionException:
        return JSONResponse(status_code=403, content={
            "message": "Solo el rol Administrador can consumir este endpoint",
            "data": None,
            "success": False
        })
    except NoEncontradoException:
        return JSONResponse(status_code=404, content={
            "message": "Plantilla no encontrada",
            "data": None,
            "success": False
        })
    except CamposInvalidosException:
        return JSONResponse(status_code=400, content={
            "message": "Los campos enviados no existen en la plantilla",
            "data": None,
            "success": False
        })


# ==========================================
# 3. PATCH - CATEGORIZAR PLANTILLA (HU-06)
# ==========================================
@router.patch("/{id}/categoria", status_code=200)
def categorizar_plantilla(
    id: int,
    datos: PlantillaUpdateCategoria,
    x_user_role: str = Header(..., description="Simulación del rol del Token")
):
    try:
        plantilla = service.actualizar_categoria_plantilla(id, datos.categoria.value, x_user_role)
        return JSONResponse(status_code=200, content={
            "message": "Categoría asignada exitosamente",
            "data": {
                "id": plantilla.id,
                "nombre": plantilla.nombre,
                "categoria": plantilla.categoria
            },
            "success": True
        })
    except AutorizacionException:
        return JSONResponse(status_code=403, content={
            "message": "Solo el rol Administrador puede consumir este endpoint",
            "data": None,
            "success": False
        })