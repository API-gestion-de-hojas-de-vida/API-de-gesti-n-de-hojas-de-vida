# app/services/hoja_de_vida_service.py
from app.domain.hoja_de_vida import SeccionRequest, SeccionResponse
from app.repositories.hoja_repository import HojaRepository

LIMITES = {'nombre': 100, 'descripcion': 500, 'titulo': 150, 'telefono': 20, 'email': 100, 'direccion': 200, 'perfil': 1000, 'habilidades': 300}

class HojaDeVidaService:
    def __init__(self, repo: HojaRepository):
        self.repo = repo

    def guardar_secciones(self, hoja_id: int, datos: SeccionRequest) -> SeccionResponse:
        if not self.repo.hoja_existe(hoja_id):
            return SeccionResponse(message='La hoja de vida no existe', data=None, success=False)
        errores = []
        campos = datos.model_dump(exclude_none=True)
        for campo, valor in campos.items():
            limite = LIMITES.get(campo)
            if limite and len(valor) > limite:
                errores.append(f"El campo '{campo}' supera la longitud maxima permitida de {limite} caracteres")
        if errores:
            return SeccionResponse(message='; '.join(errores), data=None, success=False)
        id_guardado = self.repo.guardar_secciones(hoja_id, campos)
        return SeccionResponse(message='Informacion guardada exitosamente', data={'id': id_guardado}, success=True)

    def agregar_experiencia(self, hoja_id: int, datos) -> 'BloqueResponse':
        from app.domain.hoja_de_vida import BloqueResponse
        if not self.repo.hoja_existe(hoja_id):
            return BloqueResponse(message='La hoja de vida no existe', data=None, success=False)
        if not datos.empresa or not datos.cargo:
            return BloqueResponse(message='Los campos empresa y cargo son obligatorios', data=None, success=False)
        bloque = self.repo.agregar_bloque(hoja_id, 'experiencia', datos.model_dump())
        return BloqueResponse(message='Bloque agregado exitosamente', data=bloque, success=True)

    def agregar_educacion(self, hoja_id: int, datos) -> 'BloqueResponse':
        from app.domain.hoja_de_vida import BloqueResponse
        if not self.repo.hoja_existe(hoja_id):
            return BloqueResponse(message='La hoja de vida no existe', data=None, success=False)
        if not datos.institucion or not datos.titulo:
            return BloqueResponse(message='Los campos institucion y titulo son obligatorios', data=None, success=False)
        bloque = self.repo.agregar_bloque(hoja_id, 'educacion', datos.model_dump())
        return BloqueResponse(message='Bloque agregado exitosamente', data=bloque, success=True)
