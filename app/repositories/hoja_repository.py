# app/repositories/hoja_repository.py

from typing import Optional


class HojaRepository:

    def __init__(self):
        # Hojas de vida simuladas
        self._hojas: set[int] = {1, 2, 3}

    def hoja_existe(self, hoja_id: int) -> bool:
        return hoja_id in self._hojas


hoja_repository = HojaRepository()