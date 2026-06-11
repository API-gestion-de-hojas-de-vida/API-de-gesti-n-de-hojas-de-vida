# app/repositories/hoja_repository.py
from typing import Dict

class HojaRepository:
    def __init__(self):
        self._hojas: set[int] = {1, 2, 3}
        self._secciones: Dict[int, dict] = {}
        self._bloques: Dict[int, list] = {}

    def hoja_existe(self, hoja_id: int) -> bool:
        return hoja_id in self._hojas

    def guardar_secciones(self, hoja_id: int, datos: dict) -> int:
        self._secciones[hoja_id] = datos
        return hoja_id

    def agregar_bloque(self, hoja_id: int, tipo: str, datos: dict) -> dict:
        if hoja_id not in self._bloques:
            self._bloques[hoja_id] = []
        nuevo_id = len(self._bloques[hoja_id]) + 1
        bloque = {'id': nuevo_id, 'tipo': tipo, **datos}
        self._bloques[hoja_id].append(bloque)
        return bloque

hoja_repository = HojaRepository()
