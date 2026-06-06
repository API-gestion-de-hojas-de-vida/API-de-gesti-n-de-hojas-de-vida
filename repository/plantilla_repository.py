from domain.plantilla import Plantilla
from typing import Optional

class PlantillaRepository:

    def __init__(self):
        self._datos: list[Plantilla] = []
        self._seed()

    def _seed(self):
        self._datos = [
            Plantilla(1, "Plantilla Moderna", "activo"),
            Plantilla(2, "Plantilla Clásica", "activo"),
            Plantilla(3, "Plantilla Antigua", "activo"),
        ]

    def buscar_por_id(self, id: int) -> Optional[Plantilla]:
        return next(
            (p for p in self._datos if p.id == id),
            None
        )

    def desactivar(self, id: int) -> Optional[Plantilla]:
        plantilla = self.buscar_por_id(id)
        if plantilla:
            plantilla.desactivar()
        return plantilla

    def obtener_reporte_uso(self) -> list:
        reporte = [
            {
                "id": p.id,
                "nombre": p.nombre,
                "vecesUsada": 0
            }
            for p in self._datos
        ]
        return sorted(reporte, key=lambda x: x["vecesUsada"], reverse=True)

plantilla_repository = PlantillaRepository()