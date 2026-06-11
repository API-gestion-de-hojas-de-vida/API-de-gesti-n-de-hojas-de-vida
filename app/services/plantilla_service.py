# app/services/plantilla_service.py
from typing import List
from app.domain.plantilla import PlantillaCreate
from app.repositories.plantilla_repository import PlantillaRepository

class DuplicadoException(Exception):
    pass

class AutorizacionException(Exception):
    pass

class NoEncontradoException(Exception):
    pass

class CamposInvalidosException(Exception):
    pass

class ConflictoException(Exception):
    pass

class PlantillaService:
    def __init__(self, repo: PlantillaRepository):
        self.repo = repo

    def crear_plantilla(self, datos: PlantillaCreate, rol_usuario: str):
        if rol_usuario != "Administrador":
            raise AutorizacionException("Solo el rol Administrador puede consumir este endpoint")

        existente = self.repo.obtener_por_nombre(datos.nombre)
        if existente:
            raise DuplicadoException("Ya existe una plantilla con ese nombre")

        return self.repo.crear(nombre=datos.nombre, secciones=datos.secciones, categoria=datos.categoria)

    def actualizar_campos_obligatorios(self, id: int, campos: List[str], rol_usuario: str):
        if rol_usuario != "Administrador":
            raise AutorizacionException("Solo el rol Administrador puede consumir este endpoint")

        plantilla = self.repo.obtener_por_id(id)
        if not plantilla:
            raise NoEncontradoException("Plantilla no encontrada")

        secciones_validas = set(plantilla.secciones)
        for campo in campos:
            if campo not in secciones_validas:
                raise CamposInvalidosException("Los campos enviados no existen en la plantilla")

        return self.repo.actualizar_campos(id, campos)

    def actualizar_categoria_plantilla(self, id: int, categoria: str, rol_usuario: str):
        if rol_usuario != "Administrador":
            raise AutorizacionException("Solo el rol Administrador puede consumir este endpoint")

        plantilla = self.repo.obtener_por_id(id)
        if not plantilla:
            raise NoEncontradoException("Plantilla no encontrada")

        return self.repo.actualizar_categoria(id, categoria)

    def desactivar_plantilla_obsoleta(self, id: int, rol_usuario: str):
        if rol_usuario != "Administrador":
            raise AutorizacionException("Solo el rol Administrador puede consumir este endpoint")

        plantilla = self.repo.obtener_por_id(id)
        if not plantilla:
            raise NoEncontradoException("Plantilla no encontrada")

        if not plantilla.activa:
            raise ConflictoException("La plantilla ya se encuentra inactiva")

        self.repo.desactivar_logico(id)
        return {
            "mensaje": "Plantilla desactivada correctamente",
            "data": {"id": id, "estado": "inactivo"},
            "success": True
        }

    # ==========================================
    # HU-09, HU-10 y HU-13: CATÁLOGO, FILTRO Y BÚSQUEDA
    # ==========================================
    def obtener_catalogo(self, page: int, size: int, categoria: str = None, buscar: str = None):
        if page < 1 or size < 1:
            raise CamposInvalidosException("Los parámetros de paginación deben ser números positivos")

        if categoria and categoria not in ["Gratis", "Plus", "Pro"]:
            raise CamposInvalidosException("Categoría no válida. Debe ser Gratis, Plus o Pro")

        # Validación HU-13: Que no envíen espacios vacíos en la búsqueda
        if buscar is not None and len(buscar.strip()) == 0:
            raise CamposInvalidosException("El término de búsqueda no puede estar vacío")

        return self.repo.obtener_paginadas(page, size, categoria, buscar)
