# app/services/plantilla_service.py
from app.domain.plantilla import PlantillaCreate
from app.repositories.plantilla_repository import PlantillaRepository

class DuplicadoException(Exception):
    pass

class AutorizacionException(Exception):
    pass

class PlantillaService:
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