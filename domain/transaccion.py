from pydantic import BaseModel
from typing import Optional

class TransaccionData(BaseModel):
    idTransaccion: int
    idPlantilla: int
    nombrePlantilla: str
    accesoPermanente: bool

class TransaccionResponse(BaseModel):
    mensaje: str
    data: Optional[TransaccionData] = None
    success: bool