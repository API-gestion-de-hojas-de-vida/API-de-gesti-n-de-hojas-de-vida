# app/services/validacion_service.py

from app.domain.validacion import ValidacionRequest, ValidacionResponse, ErrorCampo
from app.repositories.hoja_repository import HojaRepository


class ValidacionService:

    def __init__(self, repo: HojaRepository):
        self.repo = repo

    def validar_formulario(
        self, hoja_id: int, datos: ValidacionRequest
    ) -> ValidacionResponse:

        # Verificar que la hoja de vida existe
        if not self.repo.hoja_existe(hoja_id):
            return ValidacionResponse(
                message="La hoja de vida no existe",
                data=None,
                success=False,
            )

        errores = []

        # Validar nombre
        if not datos.nombre or datos.nombre.strip() == "":
            errores.append(ErrorCampo(
                campo="nombre",
                mensaje="El nombre es obligatorio"
            ))

        # Validar email
        if not datos.email or datos.email.strip() == "":
            errores.append(ErrorCampo(
                campo="email",
                mensaje="El email es obligatorio"
            ))

        # Validar telefono
        if not datos.telefono or datos.telefono.strip() == "":
            errores.append(ErrorCampo(
                campo="telefono",
                mensaje="El teléfono es obligatorio"
            ))

        # Validar experiencia
        if not datos.experiencia or len(datos.experiencia) == 0:
            errores.append(ErrorCampo(
                campo="experiencia",
                mensaje="Debe agregar al menos una experiencia laboral"
            ))

        # Validar educacion
        if not datos.educacion or len(datos.educacion) == 0:
            errores.append(ErrorCampo(
                campo="educacion",
                mensaje="Debe agregar al menos un registro de educación"
            ))

        if errores:
            return ValidacionResponse(
                message="Existen errores en el formulario",
                data={"errores": [e.dict() for e in errores]},
                success=False,
            )

        return ValidacionResponse(
            message="Formulario válido",
            data=None,
            success=True,
        )