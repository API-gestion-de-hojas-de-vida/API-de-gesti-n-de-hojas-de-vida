from domain.plantilla import PlantillaResponse
from repository.plantilla_repository import PlantillaRepository

class PlantillaService:

    def __init__(self, repo: PlantillaRepository):
        self.repo = repo

    def desactivar(self, id: int) -> PlantillaResponse:

        plantilla = self.repo.buscar_por_id(id)

        # CASO DE ERROR 1: plantilla no existe
        if not plantilla:
            return PlantillaResponse(
                message="Plantilla no encontrada",
                data=None,
                success=False
            )

        # CASO DE ERROR 2: plantilla ya inactiva
        if not plantilla.esta_activa():
            return PlantillaResponse(
                message="La plantilla ya se encuentra desactivada",
                data=None,
                success=False
            )

        # ÉXITO: desactivar plantilla
        self.repo.desactivar(id)
        return PlantillaResponse(
            message="Plantilla desactivada exitosamente",
            data=plantilla.to_response(),
            success=True
        )