from domain.plan import PlanPlusResponse, PlanPlusData
from typing import Optional

class PlanesService:
    def __init__(self, usuario_repo):
        self.usuario_repo = usuario_repo

    def obtener_informacion_plus(self, usuario_id: Optional[int], plan_actual: Optional[str]):
        if not usuario_id:
            return {
                "status_code": 401,
                "response": {
                    "mensaje": "Usuario no autenticado",
                    "data": None,
                    "success": False
                }
            }

        if plan_actual in ["Plus", "Pro"]:
            return {
                "status_code": 409,
                "response": {
                    "mensaje": "Ya cuentas con un plan superior o igual a Plus",
                    "data": None,
                    "success": False
                }
            }

        data_plan = {
            "plan": "Plus",
            "precio": 9.99,
            "moneda": "USD",
            "beneficios": [
                "Plantillas Plus",
                "Exportación ilimitada",
                "Soporte prioritario"
            ],
            "urlPago": "/api/v1/pagos/suscripcion/plus"
        }

        return {
            "status_code": 200,
            "response": {
                "mensaje": "Información del plan Plus obtenida exitosamente",
                "data": data_plan,
                "success": True
            }
        }