# app/repositories/hoja_de_vida_repository.py
from app.domain.hoja_de_vida import HojaDeVida
from typing import Optional, List
import datetime


class HojaDeVidaRepository:
    def __init__(self):
        self._datos: List[HojaDeVida] = []
        self._siguiente_id = 1
        self._log_auditoria: List[dict] = []
        self._exportaciones_mes: dict = {}

    def crear_prueba(self, usuario_id: int, plantilla_id: Optional[int] = None, datos: dict = None) -> HojaDeVida:
        nueva = HojaDeVida(self._siguiente_id, usuario_id, plantilla_id, datos)
        self._datos.append(nueva)
        self._siguiente_id += 1
        return nueva

    def obtener_por_id(self, id: int) -> Optional[HojaDeVida]:
        for hv in self._datos:
            if hv.id == id:
                return hv
        return None

    def obtener_por_usuario(self, usuario_id: int) -> List[HojaDeVida]:
        return [hv for hv in self._datos if hv.usuario_id == usuario_id]

    def registrar_auditoria(self, usuario_id: int, hoja_de_vida_id: int, accion: str = "EXPORTAR_PDF"):
        log = {
            "fecha_hora": datetime.datetime.now().isoformat(),
            "usuario_id": usuario_id,
            "hoja_de_vida_id": hoja_de_vida_id,
            "accion": accion
        }
        self._log_auditoria.append(log)
        self._exportaciones_mes[usuario_id] = self._exportaciones_mes.get(usuario_id, 0) + 1
        print(f"[AUDIT LOG] {log}")

    def obtener_exportaciones_mensuales(self, usuario_id: int) -> int:
        return self._exportaciones_mes.get(usuario_id, 0)

    # HU-23: eliminar hoja de vida
    def eliminar(self, id: int) -> bool:
        for i, hv in enumerate(self._datos):
            if hv.id == id:
                self._datos.pop(i)
                return True
        return False


hoja_de_vida_repository = HojaDeVidaRepository()