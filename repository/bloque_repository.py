# repository/bloque_repository.py

from domain.bloque import Bloque
from typing import Optional


class BloqueRepository:

    def __init__(self):
        self._datos: list[Bloque] = []
        self._contador: int = 0
        # Hojas de vida simuladas (IDs existentes)
        self._hojas_de_vida: set[int] = {1, 2, 3}

    def hoja_existe(self, hoja_id: int) -> bool:
        return hoja_id in self._hojas_de_vida

    def agregar(self, hoja_id: int, tipo: str, datos: dict) -> Bloque:
        self._contador += 1
        bloque = Bloque(
            id=self._contador,
            tipo=tipo,
            datos=datos,
        )
        self._datos.append(bloque)
        return bloque

    def obtener_por_hoja(self, hoja_id: int) -> list[Bloque]:
        return [b for b in self._datos]


bloque_repository = BloqueRepository()