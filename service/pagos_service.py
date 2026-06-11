from domain.transaccion import TransaccionResponse, TransaccionData

class PagosService:
    def __init__(self):
        # Simulamos una base de datos de accesos previos: Usuario 1 ya compró la plantilla 99
        self.accesos_previos = {(1, 99)} 
        self.contador_transacciones = 122

    def comprar_plantilla_pro(self, usuario_id: int, plantilla_id: int, token_tarjeta: str):
        # Caso 2: El usuario ya tiene acceso previo
        if (usuario_id, plantilla_id) in self.accesos_previos:
            return {
                "status_code": 409,
                "response": {
                    "mensaje": "Ya tienes acceso a esta plantilla",
                    "data": None,
                    "success": False
                }
            }

        # Caso 3: Pago fallido (Simulamos tarjeta inválida si el token contiene 'invalid')
        if "invalid" in token_tarjeta.lower():
            return {
                "status_code": 402,
                "response": {
                    "mensaje": "No fue posible procesar el pago",
                    "data": None,
                    "success": False
                }
            }

        # Caso 1: Compra exitosa
        self.contador_transacciones += 1
        self.accesos_previos.add((usuario_id, plantilla_id))

        data_transaccion = {
            "idTransaccion": self.contador_transacciones,
            "idPlantilla": plantilla_id,
            "nombrePlantilla": "Plantilla Ejecutiva Pro",
            "accesoPermanente": True
        }

        return {
            "status_code": 201, # Created
            "response": {
                "mensaje": "Plantilla adquirida exitosamente",
                "data": data_transaccion,
                "success": True
            }
        }