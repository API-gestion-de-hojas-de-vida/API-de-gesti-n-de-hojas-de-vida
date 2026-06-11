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
    except NoEncontradoException:
        return JSONResponse(status_code=404, content={
            "message": "Plantilla no encontrada",
            "data": None,
            "success": False
        })

# ==========================================
# ENDPOINT DE TUS COMPAÑEROS
# ==========================================
@router.patch("/{id}/desactivar", status_code=200)
def desactivar_plantilla(
    id: int,
    x_user_role: str = Header(..., description="Simulación del rol del Token")
):
    try:
        resultado = service.desactivar_plantilla_obsoleta(id=id, rol_usuario=x_user_role)
        return JSONResponse(status_code=200, content=resultado)
    except AutorizacionException:
        return JSONResponse(status_code=403, content={
            "message": "Solo el rol Administrador puede consumir este endpoint",
            "data": None,
            "success": False
        })
    except NoEncontradoException:
        return JSONResponse(status_code=404, content={
            "message": "Plantilla no encontrada",
            "data": None,
            "success": False
        })
    except ConflictoException:
        return JSONResponse(status_code=409, content={
            "message": "La plantilla ya se encuentra inactiva",
            "data": None,
            "success": False
        })

# ==========================================
# TUS ENDPOINTS DE LAS HU-09 Y HU-10
# ==========================================
@router.get("", status_code=status.HTTP_200_OK)
def obtener_catalogo_paginado(
    page: int = Query(1, description="Número de página"),
    size: int = Query(10, description="Cantidad de registros por página"),
    categoria: str = Query(None, description="Filtrar por plan (Gratis, Plus, Pro)")
):
    try:
        total, plantillas_paginadas = service.obtener_catalogo(page, size, categoria)
        lista_formateada = [{"id": p.id, "nombre": p.nombre, "categoria": p.categoria} for p in plantillas_paginadas]
        
        # Estructura de respuesta de la HU-10 (Si se envía el filtro de categoría)
        if categoria:
            if total == 0:
                return JSONResponse(status_code=200, content={
                    "message": "No hay plantillas disponibles para este plan",
                    "data": [],
                    "success": True
                })
            return JSONResponse(status_code=200, content={
                "message": "Filtro aplicado exitosamente",
                "data": lista_formateada,
                "success": True
            })

        # Estructura de respuesta de la HU-09 (Catálogo paginado general sin filtro)
        return JSONResponse(status_code=200, content={
            "mensaje": "Catálogo obtenido exitosamente",
            "data": {
                "pagina": page,
                "tamano": size,
                "total": total,
                "plantillas": lista_formateada
            },
            "success": True
        })
        
    except CamposInvalidosException as e:
        return JSONResponse(status_code=400, content={
            "mensaje": str(e),
            "data": None,
            "success": False
        })