# app/repositories/hoja_de_vida_repository.py
from app.domain.hoja_de_vida import HojaDeVida
from typing import Optional, List
import datetime

class HojaDeVidaRepository:
    def __init__(self):
        self._datos: List[HojaDeVida] = []
        self._siguiente_id = 1
        self._log_auditoria: List[dict] = []
        self._exportaciones_mes: dict = {}  # Simula: {usuario_id: contador_de_exportaciones}

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

    def registrar_auditoria(self, usuario_id: int, hoja_de_vida_id: int):
        log = {
            "fecha_hora": datetime.datetime.now().isoformat(),
            "usuario_id": usuario_id,
            "hoja_de_vida_id": hoja_de_vida_id,
            "accion": "EXPORTAR_PDF"
        }
        self._log_auditoria.append(log)
        # Incrementar contador mensual simulado
        self._exportaciones_mes[usuario_id] = self._exportaciones_mes.get(usuario_id, 0) + 1
        print(f"[AUDIT LOG] {log}")  # Visualización directa en consola de Uvicorn

    def obtener_exportaciones_mensuales(self, usuario_id: int) -> int:
        return self._exportaciones_mes.get(usuario_id, 0)

hoja_de_vida_repository = HojaDeVidaRepository()