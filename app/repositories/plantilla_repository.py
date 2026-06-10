# app/repositories/plantilla_repository.py
from app.domain.plantilla import Plantilla
from typing import Optional, List

class PlantillaRepository:
    def __init__(self):
        self._datos: List[Plantilla] = []
        self._siguiente_id: int = 1

    def obtener_todos(self) -> List[Plantilla]:
        return self._datos

    def obtener_por_nombre(self, nombre: str) -> Optional[Plantilla]:
        # Búsqueda ignorando espacios extra y mayúsculas/minúsculas
        nombre_limpio = " ".join(nombre.strip().split()).lower()
        for p in self._datos:
            p_limpio = " ".join(p.nombre.strip().split()).lower()
            if p_limpio == nombre_limpio:
                return p
        return None

    def crear(self, nombre: str, secciones: List[str], categoria: str) -> Plantilla:
        nueva = Plantilla(
            id=self._siguiente_id,
            nombre=nombre,
            secciones=secciones,
            categoria=categoria
        )
        self._datos.append(nueva)
        self._siguiente_id += 1
        return nueva

plantilla_repository = PlantillaRepository()