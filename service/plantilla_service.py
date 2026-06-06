from domain.plantilla import PlantillaResponse, ReporteUsoResponse
from repository.plantilla_repository import PlantillaRepository

class PlantillaService:

    def __init__(self, repo: PlantillaRepository):
        self.repo = repo

    def desactivar(self, id: int) -> PlantillaResponse:
        plantilla = self.repo.buscar_por_id(id)
        if not plantilla:
            return PlantillaResponse(
                message="Plantilla no encontrada",
                data=None,
                success=False
            )
        if not plantilla.esta_activa():
            return PlantillaResponse(
                message="La plantilla ya se encuentra desactivada",
                data=None,
                success=False
            )
        self.repo.desactivar(id)
        return PlantillaResponse(
            message="Plantilla desactivada exitosamente",
            data=plantilla.to_response(),
            success=True
        )

    def reporte_uso(self) -> ReporteUsoResponse:
        try:
            reporte = self.repo.obtener_reporte_uso()
            if not reporte:
                return ReporteUsoResponse(
                    message="No hay plantillas registradas",
                    data=[],
                    success=True
                )
            return ReporteUsoResponse(
                message="Reporte generado exitosamente",
                data=reporte,
                success=True
            )
        except Exception:
            return ReporteUsoResponse(
                message="No fue posible generar el reporte",
                data=[],
                success=False
            )