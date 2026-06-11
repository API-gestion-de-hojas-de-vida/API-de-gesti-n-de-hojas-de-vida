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


@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_plantilla(datos: PlantillaCreate, x_user_role: str = Header(..., description="Simulacion del rol del Token")):
    try:
        nueva_plantilla = service.crear_plantilla(datos, rol_usuario=x_user_role)
        return JSONResponse(status_code=201, content={
            "message": "Plantilla creada exitosamente",
            "data": nueva_plantilla.to_dict(),
            "success": True
        })
    except AutorizacionException:
        return JSONResponse(status_code=403, content={"message": "Solo el rol Administrador puede consumir este endpoint", "data": None, "success": False})
    except DuplicadoException:
        return JSONResponse(status_code=409, content={"message": "Ya existe una plantilla con ese nombre", "data": None, "success": False})


@router.patch("/{id}/campos-obligatorios", status_code=200)
def actualizar_campos_obligatorios(
    id: int,
    datos: PlantillaUpdateObligatorios,
    x_user_role: str = Header(..., description="Simulacion del rol del Token")
):
    try:
        plantilla = service.actualizar_campos_obligatorios(id, datos.campos_obligatorios, x_user_role)
        return JSONResponse(status_code=200, content={
            "message": "Campos obligatorios actualizados exitosamente",
            "data": {"id": plantilla.id, "nombre": plantilla.nombre, "camposObligatorios": plantilla.campos_obligatorios},
            "success": True
        })
    except AutorizacionException:
        return JSONResponse(status_code=403, content={"message": "Solo el rol Administrador puede consumir este endpoint", "data": None, "success": False})
    except NoEncontradoException:
        return JSONResponse(status_code=404, content={"message": "Plantilla no encontrada", "data": None, "success": False})
    except CamposInvalidosException:
        return JSONResponse(status_code=400, content={"message": "Los campos enviados no existen en la plantilla", "data": None, "success": False})


@router.patch("/{id}/categoria", status_code=200)
def categorizar_plantilla(
    id: int,
    datos: PlantillaUpdateCategoria,
    x_user_role: str = Header(..., description="Simulacion del rol del Token")
):
    try:
        plantilla = service.actualizar_categoria_plantilla(id, datos.categoria.value, x_user_role)
        return JSONResponse(status_code=200, content={
            "message": "Categoria asignada exitosamente",
            "data": {"id": plantilla.id, "nombre": plantilla.nombre, "categoria": plantilla.categoria},
            "success": True
        })
    except AutorizacionException:
        return JSONResponse(status_code=403, content={"message": "Solo el rol Administrador puede consumir este endpoint", "data": None, "success": False})
    except NoEncontradoException:
        return JSONResponse(status_code=404, content={"message": "Plantilla no encontrada", "data": None, "success": False})


@router.patch("/{id}/desactivar", status_code=200)
def desactivar_plantilla(id: int, x_user_role: str = Header(..., description="Simulacion del rol del Token")):
    try:
        resultado = service.desactivar_plantilla_obsoleta(id=id, rol_usuario=x_user_role)
        return JSONResponse(status_code=200, content=resultado)
    except AutorizacionException:
        return JSONResponse(status_code=403, content={"message": "Solo el rol Administrador puede consumir este endpoint", "data": None, "success": False})
    except NoEncontradoException:
        return JSONResponse(status_code=404, content={"message": "Plantilla no encontrada", "data": None, "success": False})
    except ConflictoException:
        return JSONResponse(status_code=409, content={"message": "La plantilla ya se encuentra inactiva", "data": None, "success": False})


@router.get("", status_code=status.HTTP_200_OK)
def obtener_catalogo_paginado(
    page: int = Query(1, description="Numero de pagina"),
    size: int = Query(10, description="Cantidad de registros por pagina"),
    categoria: str = Query(None, description="Filtrar por plan (Gratis, Plus, Pro)"),
    buscar: str = Query(None, description="Buscar por palabra clave")
):
    try:
        if buscar is not None:
            try:
                resultados = service.buscar_plantillas(buscar)
            except CamposInvalidosException as e:
                return JSONResponse(status_code=400, content={"message": str(e), "data": None, "success": False})
            if not resultados:
                return JSONResponse(status_code=200, content={"message": "No se encontraron plantillas con ese termino", "data": [], "success": True})
            lista = [{"id": p.id, "nombre": p.nombre, "categoria": p.categoria} for p in resultados]
            return JSONResponse(status_code=200, content={"message": "Busqueda realizada exitosamente", "data": lista, "success": True})

        total, plantillas_paginadas = service.obtener_catalogo(page, size, categoria)
        lista_formateada = [{"id": p.id, "nombre": p.nombre, "categoria": p.categoria} for p in plantillas_paginadas]

        if categoria:
            if total == 0:
                return JSONResponse(status_code=200, content={"message": "No hay plantillas disponibles para este plan", "data": [], "success": True})
            return JSONResponse(status_code=200, content={"message": "Filtro aplicado exitosamente", "data": lista_formateada, "success": True})

        return JSONResponse(status_code=200, content={
            "message": "Catalogo obtenido exitosamente",
            "data": {"pagina": page, "tamano": size, "total": total, "plantillas": lista_formateada},
            "success": True
        })

    except CamposInvalidosException as e:
        return JSONResponse(status_code=400, content={"message": str(e), "data": None, "success": False})


@router.get("/catalogo-indicador", status_code=200)
def obtener_catalogo_con_indicador(
    x_authorization: str = Header(None, alias="x-authorization", description="Bearer token")
):
    try:
        resultado = service.obtener_catalogo_con_indicador(x_authorization)
        if not resultado:
            return JSONResponse(status_code=200, content={"message": "No hay plantillas disponibles", "data": [], "success": True})
        return JSONResponse(status_code=200, content={"message": "Catalogo obtenido exitosamente", "data": resultado, "success": True})
    except AutorizacionException:
        return JSONResponse(status_code=401, content={"message": "No autorizado. Debe iniciar sesion", "data": None, "success": False})
    except Exception:
        return JSONResponse(status_code=500, content={"message": "No fue posible obtener el catalogo", "data": None, "success": False})


@router.get("/{id}/preview", status_code=200)
def obtener_preview(id: int):
    try:
        data = service.obtener_preview(id)
        return JSONResponse(status_code=200, content={"message": "Plantilla obtenida exitosamente", "data": data, "success": True})
    except NoEncontradoException as e:
        return JSONResponse(status_code=404, content={"message": str(e), "data": None, "success": False})
