# app/api/v1/pagos_router.py
from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix='/api/v1/pagos', tags=['Pagos'])

_compras: dict = {}
_contador_transacciones: int = 0

_plantillas_pro: dict = {
    5: 'Plantilla Ejecutiva Pro',
    6: 'Plantilla Moderna Pro',
    7: 'Plantilla Creativa Pro',
}

class CompraRequest(BaseModel):
    numeroTarjeta: Optional[str] = None
    cvv: Optional[str] = None
    fechaExpiracion: Optional[str] = None

@router.post('/plantillas/{id}/comprar', summary='Comprar plantilla Pro individual')
def comprar_plantilla(id: int, datos: CompraRequest, x_user_id: int = Header(...), x_autenticado: bool = Header(True)):
    global _contador_transacciones
    if not x_autenticado:
        return JSONResponse(status_code=401, content={'message': 'Usuario no autenticado', 'data': None, 'success': False})
    clave = f'{x_user_id}_{id}'
    if clave in _compras:
        return JSONResponse(status_code=409, content={'message': 'Ya tienes acceso a esta plantilla', 'data': None, 'success': False})
    if not datos.numeroTarjeta or not datos.cvv or not datos.fechaExpiracion:
        return JSONResponse(status_code=402, content={'message': 'No fue posible procesar el pago', 'data': None, 'success': False})
    if len(datos.numeroTarjeta) < 16 or not datos.cvv.isdigit():
        return JSONResponse(status_code=402, content={'message': 'No fue posible procesar el pago', 'data': None, 'success': False})
    _contador_transacciones += 1
    _compras[clave] = True
    nombre_plantilla = _plantillas_pro.get(id, f'Plantilla Pro {id}')
    return JSONResponse(status_code=201, content={
        'message': 'Plantilla adquirida exitosamente',
        'data': {
            'idTransaccion': _contador_transacciones,
            'idPlantilla': id,
            'nombrePlantilla': nombre_plantilla,
            'accesoPermanente': True
        },
        'success': True
    })
