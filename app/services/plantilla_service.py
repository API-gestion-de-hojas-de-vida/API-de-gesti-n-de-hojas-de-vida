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

    def actualizar_campos_obligatorios(self, id: int, campos: List[str], rol_usuario: str):
        # 1. Validar rol
        if rol_usuario != "Administrador":
            raise AutorizacionException("Solo el rol Administrador puede consumir este endpoint")

        # 2. Validar que la plantilla exista
        plantilla = self.repo.obtener_por_id(id)
        if not plantilla:
            raise NoEncontradoException("Plantilla no encontrada")

        # 3. Validar que los campos obligatorios existan en las secciones
        secciones_validas = set(plantilla.secciones)
        for campo in campos:
            if campo not in secciones_validas:
                raise CamposInvalidosException("Los campos enviados no existen en la plantilla")

        # Guardar cambios
        return self.repo.actualizar_campos(id, campos)


    def __init__(self, repo: PlantillaRepository):
        self.repo = repo

    def crear_plantilla(self, datos: PlantillaCreate, rol_usuario: str):
        # Criterio de Aceptación: Validar rol Administrador
        if rol_usuario != "Administrador":
            raise AutorizacionException("Solo el rol Administrador puede consumir este endpoint")

        # Criterio de Aceptación: Validar unicidad del nombre
        existente = self.repo.obtener_por_nombre(datos.nombre)
        if existente:
            raise DuplicadoException("Ya existe una plantilla con ese nombre")

        # Guardar si todo está OK
        return self.repo.crear(
            nombre=datos.nombre,
            secciones=datos.secciones,
            categoria=datos.categoria
        )
    def obtener_catalogo(self, page: int, size: int):
        # Validar que sean números positivos (Caso 3)
        if page < 1 or size < 1:
            raise CamposInvalidosException("Los parámetros de paginación deben ser números positivos")

        # Ir al repositorio por los datos
        return self.repo.obtener_paginadas(page, size)