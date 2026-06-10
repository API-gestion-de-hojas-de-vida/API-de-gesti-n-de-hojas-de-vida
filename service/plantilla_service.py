from domain.plantilla import PlantillaResponse, ReporteUsoResponse, CatalogoResponse, Plantilla
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

    def obtener_catalogo(self) -> CatalogoResponse:
        try:
            plantillas = self.repo.obtener_activas()
            if not plantillas:
                return CatalogoResponse(
                    message="No hay plantillas disponibles",
                    data=[],
                    success=True
                )
            return CatalogoResponse(
                message="Catálogo obtenido exitosamente",
                data=[p.to_catalogo() for p in plantillas],
                success=True
            )
        except Exception:
            return CatalogoResponse(
                message="No fue posible obtener el catálogo",
                data=[],
                success=False
            )

    def obtener_preview(self, plantilla_id: int):
        plantilla = self.repo.buscar_por_id(plantilla_id)
        
        if not plantilla:
            return {
                "status_code": 404,
                "response": {
                    "message": "Plantilla no encontrada",
                    "data": None,
                    "success": False
                }
            }
        
        if hasattr(plantilla, "esta_activa") and not plantilla.esta_activa():
            return {
                "status_code": 404,
                "response": {
                    "message": "Plantilla no disponible",
                    "data": None,
                    "success": False
                }
            }
            
        preview_data = {
            "id": plantilla.id,
            "nombre": plantilla.nombre,
            "categoria": getattr(plantilla, "categoria", "Gratis"),
            "secciones": getattr(plantilla, "secciones", ["Perfil", "Experiencia", "Educación"]),
            "datosEjemplo": {
                "nombre": "Juan Pérez",
                "cargo": "Desarrollador Backend",
                "experiencia": "3 años"
            }
        }
        
        return {
            "status_code": 200,
            "response": {
                "message": "Plantilla obtenido exitosamente",
                "data": preview_data,
                "success": True
            }
        }