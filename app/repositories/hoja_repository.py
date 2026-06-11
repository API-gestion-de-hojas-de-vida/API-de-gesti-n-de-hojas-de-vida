# app/repositories/hoja_repository.py
from typing import Dict

class HojaRepository:
    def __init__(self):
        self._hojas: set[int] = {1, 2, 3}
        self._secciones: Dict[int, dict] = {}

    def hoja_existe(self, hoja_id: int) -> bool:
        return hoja_id in self._hojas

    def guardar_secciones(self, hoja_id: int, datos: dict) -> int:
        self._secciones[hoja_id] = datos
        return hoja_id

hoja_repository = HojaRepository()
