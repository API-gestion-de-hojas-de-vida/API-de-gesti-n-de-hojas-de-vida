# app/api/v1/plantilla_router.py
from fastapi import APIRouter, HTTPException, status, Header, Query
from pydantic import ValidationError

from app.domain.plantilla import PlantillaCreate, PlantillaUpdateObligatorios, PlantillaUpdateCategoria
from app.services.plantilla_service import (
    PlantillaService, DuplicadoException, AutorizacionException, 
    NoEncontradoException, CamposInvalidosException
)
from app.repositories.plantilla_repository import plantilla_repository

router = APIRouter(
    prefix="/api/v1/plantillas",
    tags=["Plantillas"]
)

service = PlantillaService(repo=plantilla_repository)

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_plantilla(datos: PlantillaCreate, x_user_role: str = Header(..., description="Simulación del rol del Token")):
    try:
        nueva_plantilla = service.crear_plantilla(datos, rol_usuario=x_user_role)
        return {
            "message": "Plantilla creada exitosamente",
            "data": nueva_plantilla.to_dict(),
            "success": True
        }
    except AutorizacionException as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))
    except DuplicadoException:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={"message": "Ya existe una plantilla con ese nombre", "data": None, "success": False}
        )

@router.patch("/{id}/campos-obligatorios", status_code=status.HTTP_200_OK)
def actualizar_campos_obligatorios(
    id: int,
    datos: PlantillaUpdateObligatorios,
    x_user_role: str = Header(..., description="Simulación del rol del Token")
):
    try:
        plantilla_actualizada = service.actualizar_campos_obligatorios(id, datos.campos_obligatorios, x_user_role)
        return {
            "mensaje": "Campos obligatorios actualizados exitosamente",
            "data": {
                "id": plantilla_actualizada.id,
                "nombre": plantilla_actualizada.nombre,
                "camposObligatorios": plantilla_actualizada.campos_obligatorios
            },
            "success": True
        }
    except AutorizacionException as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))
    except NoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"mensaje": str(e), "data": None, "success": False})
    except CamposInvalidosException as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail={"mensaje": str(e), "data": None, "success": False})

@router.patch("/{id}/categoria", status_code=status.HTTP_200_OK)
def categorizar_plantilla(
    id: int,
    datos: PlantillaUpdateCategoria,
    x_user_role: str = Header(..., description="Simulación del rol del Token")
):
    try:
        plantilla_actualizada = service.actualizar_categoria_plantilla(id, datos.categoria.value, x_user_role)
        return {
            "mensaje": "Categoría asignada exitosamente",
            "data": {
                "id": plantilla_actualizada.id,
                "nombre": plantilla_actualizada.nombre,
                "categoria": plantilla_actualizada.categoria
            },
            "success": True
        }
    except AutorizacionException as e:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=str(e))
    except NoEncontradoException as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"mensaje": str(e), "data": None, "success": False})

# Endpoint unificado de consulta GET (HU-09 y HU-10)
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
                return {
                    "message": "No hay plantillas disponibles para este plan",
                    "data": [],
                    "success": True
                }
            return {
                "message": "Filtro aplicado exitosamente",
                "data": lista_formateada,
                "success": True
            }

        # Estructura de respuesta de la HU-09 (Catálogo paginado general)
        return {
            "mensaje": "Catálogo obtenido exitosamente",
            "data": {
                "pagina": page,
                "tamano": size,
                "total": total,
                "plantillas": lista_formateada
            },
            "success": True
        }
        
    except CamposInvalidosException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail={"mensaje": str(e), "data": None, "success": False}
        )