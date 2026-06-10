# service/bloque_service.py

from domain.bloque import ExperienciaRequest, EducacionRequest, BloqueResponse
from repository.bloque_repository import BloqueRepository


class BloqueService:

    def __init__(self, repo: BloqueRepository):
        self.repo = repo

    def agregar_experiencia(
        self, hoja_id: int, datos: ExperienciaRequest
    ) -> BloqueResponse:
        if not self.repo.hoja_existe(hoja_id):
            return BloqueResponse(
                message="La hoja de vida no existe",
                data=None,
                success=False,
            )

        bloque = self.repo.agregar(
            hoja_id=hoja_id,
            tipo="experiencia",
            datos={
                "empresa": datos.empresa,
                "cargo": datos.cargo,
                "fechaInicio": datos.fechaInicio,
                "fechaFin": datos.fechaFin,
            },
        )

        return BloqueResponse(
            message="Bloque agregado exitosamente",
            data=bloque.to_response(),
            success=True,
        )

    def agregar_educacion(
        self, hoja_id: int, datos: EducacionRequest
    ) -> BloqueResponse:
        if not self.repo.hoja_existe(hoja_id):
            return BloqueResponse(
                message="La hoja de vida no existe",
                data=None,
                success=False,
            )

        bloque = self.repo.agregar(
            hoja_id=hoja_id,
            tipo="educacion",
            datos={
                "institucion": datos.institucion,
                "titulo": datos.titulo,
                "fechaInicio": datos.fechaInicio,
                "fechaFin": datos.fechaFin,
            },
        )

        return BloqueResponse(
            message="Bloque agregado exitosamente",
            data=bloque.to_response(),
            success=True,
        )
    