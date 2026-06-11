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
