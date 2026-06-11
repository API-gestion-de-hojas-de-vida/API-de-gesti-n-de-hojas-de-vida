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

    # ==========================================
    # HU-09 Y HU-10: CATÃLOGO PAGINADO Y FILTRO
    # ==========================================
    def obtener_catalogo(self, page: int, size: int, categoria: str = None):
        if page < 1 or size < 1:
            raise CamposInvalidosException("Los parÃ¡metros de paginaciÃ³n deben ser nÃºmeros positivos")

        if categoria and categoria not in ["Gratis", "Plus", "Pro"]:
            raise CamposInvalidosException("CategorÃ­a no vÃ¡lida. Debe ser Gratis, Plus o Pro")

        return self.repo.obtener_paginadas(page, size, categoria)

    # ==========================================
    # LÃ“GICA DE TUS COMPAÃ‘EROS: DESACTIVAR
    # ==========================================
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
            "data": {
                "id": id,
                "estado": "inactivo"
            },
            "success": True
        }
    # ==========================================
    # HU-11: CATALOGO CON INDICADOR VISUAL
    # ==========================================
    def obtener_catalogo_con_indicador(self, authorization: str = None):
        if not authorization or not authorization.startswith('Bearer '):
            raise AutorizacionException('No autorizado. Debe iniciar sesion')
        plantillas = self.repo.obtener_activas()
        resultado = []
        for p in plantillas:
            resultado.append({
                'id': p.id,
                'nombre': p.nombre,
                'categoria': p.categoria,
                'esDePago': p.categoria in ['Plus', 'Pro']
            })
        return resultado
    # ==========================================
    # HU-12: VISTA PREVIA DE PLANTILLA
    # ==========================================
    def obtener_preview(self, id: int):
        plantilla = self.repo.obtener_por_id(id)
        if not plantilla:
            raise NoEncontradoException('Plantilla no encontrada')
        if not plantilla.activa:
            raise NoEncontradoException('Plantilla no disponible')
        return {
            'id': plantilla.id,
            'nombre': plantilla.nombre,
            'categoria': plantilla.categoria,
            'secciones': plantilla.secciones,
            'datosEjemplo': {
                'nombre': 'Juan Perez',
                'cargo': 'Desarrollador Backend',
                'experiencia': '3 anos'
            }
        }
