from pydantic import BaseModel
from typing import Optional, List

class PlanPlusData(BaseModel):
    plan: str
    precio: float
    moneda: str
    beneficios: List[str]
    urlPago: str

class PlanPlusResponse(BaseModel):
    mensaje: str
    data: Optional[PlanPlusData] = None
    success: bool