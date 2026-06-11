# app/api/v1/planes_router.py
from fastapi import APIRouter, Header
from fastapi.responses import JSONResponse
from app.domain.usuarioapi import Usuario

router = APIRouter(prefix='/api/v1/planes', tags=['Planes'])

_planes_usuarios: dict = {
    1: 'Gratis',
    2: 'Plus',
    3: 'Pro',
}

@router.get('/plus', summary='Obtener informacion del plan Plus')
def obtener_plan_plus(x_user_id: int = Header(...), x_autenticado: bool = Header(True)):
    if not x_autenticado:
        return JSONResponse(status_code=401, content={'message': 'Usuario no autenticado', 'data': None, 'success': False})
    plan_actual = _planes_usuarios.get(x_user_id, 'Gratis')
    if plan_actual in ('Plus', 'Pro'):
        return JSONResponse(status_code=409, content={'message': 'Ya cuentas con un plan superior o igual a Plus', 'data': None, 'success': False})
    return JSONResponse(status_code=200, content={
        'message': 'Informacion del plan Plus obtenida exitosamente',
        'data': {
            'plan': 'Plus',
            'precio': 9.99,
            'moneda': 'USD',
            'beneficios': ['Plantillas Plus', 'Exportacion ilimitada', 'Soporte prioritario'],
            'urlPago': '/api/v1/pagos/suscripcion/plus'
        },
        'success': True
    })
