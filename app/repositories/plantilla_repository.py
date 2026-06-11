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
        setattr(nueva, "activo", True)
        self._datos.append(nueva)
        self._siguiente_id += 1
        return nueva

    def obtener_por_id(self, id: int) -> Optional[Plantilla]:
        for p in self._datos:
            if p.id == id:
                return p
        return None

    def actualizar_campos(self, id: int, campos: List[str]) -> Plantilla:
        plantilla = self.obtener_por_id(id)
        if plantilla:
            plantilla.campos_obligatorios = campos
        return plantilla

    def actualizar_categoria(self, id: int, categoria: str) -> Plantilla:
        plantilla = self.obtener_por_id(id)
        if plantilla:
            plantilla.categoria = categoria
        return plantilla

    def desactivar_logico(self, id: int) -> Optional[Plantilla]:
        plantilla = self.obtener_por_id(id)
        if plantilla:
            plantilla.activa = False
        return plantilla

    # HU-09: catálogo paginado solo con plantillas activas
    def obtener_catalogo_paginado(self, page: int, size: int) -> dict:
        activas = [p for p in self._datos if p.activa]
        total = len(activas)
        offset = (page - 1) * size
        pagina = activas[offset:offset + size]
        return {
            "total": total,
            "plantillas": [
                {"id": p.id, "nombre": p.nombre, "categoria": p.categoria}
                for p in pagina
            ]
        }


plantilla_repository = PlantillaRepository()