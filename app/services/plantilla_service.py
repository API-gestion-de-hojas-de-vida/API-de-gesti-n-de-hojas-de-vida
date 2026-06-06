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


class PlantillaService:
    def __init__(self, repo: PlantillaRepository):
        self.repo = repo

    def crear_plantilla(self, datos: PlantillaCreate, rol_usuario: str):
        if rol_usuario != "Administrador":
            raise AutorizacionException("Solo el rol Administrador puede consumir este endpoint")

        existente = self.repo.obtener_por_nombre(datos.nombre)
        if existente:
            raise DuplicadoException("Ya existe una plantilla con ese nombre")

        return self.repo.crear(
            nombre=datos.nombre,
            secciones=datos.secciones,
            categoria=datos.categoria
        )

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

    # Método unificado para HU-09 y HU-10 con validación de categorías permitidas
    def obtener_catalogo(self, page: int, size: int, categoria: str = None):
        if page < 1 or size < 1:
            raise CamposInvalidosException("Los parámetros de paginación deben ser números positivos")

        if categoria and categoria not in ["Gratis", "Plus", "Pro"]:
            raise CamposInvalidosException("Categoría no válida. Debe ser Gratis, Plus o Pro")

        return self.repo.obtener_paginadas(page, size, categoria)