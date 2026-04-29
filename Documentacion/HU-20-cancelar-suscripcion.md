# [HU-20] Cancelar Suscripción Plus

## 📖 Historia de Usuario

Como usuario Plus
Quiero poder cancelar mi suscripción desde mi perfil
Para actualizar mi estado en la base de datos y evitar futuros cobros

🔁 Flujo Esperado

* El usuario solicita cancelación.
* El sistema valida plan activo.
* El sistema solicita confirmación.
* El sistema programa cancelación al final del periodo.
* Retorna confirmación.

✅ Criterios de Aceptación

1. 🔍 Estructura y lógica del servicio

* Se valida que el usuario tenga plan Plus activo.
* No se cancela inmediatamente, respeta periodo pagado.

### 2. 📆 Estructura de la información
- [ ] Se responde con la siguiente estructura en JSON:
```
{
  "mensaje": "Suscripción cancelada exitosamente",
  "data": {
    "planActual": "Plus",
    "planAlVencer": "Gratis",
    "fechaVencimiento": "2026-05-18"
  },
  "success": true
}
```
- [ ] Si el usuario no tiene plan Plus, el sistema retorna:
```
{
  "mensaje": "No tienes una suscripción Plus activa",
  "data": null,
  "success": false
}
```
## 🔧 Notas Técnicas

### 🚀 Endpoint – Cancelar Suscripción
- **Método HTTP:** POST
- **Ruta:** /api/v1/usuarios/suscripcion/cancelar

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Cancelación exitosa
- **Precondición:** El usuario tiene plan Plus activo.
- **Acción:** Ejecutar POST /api/v1/usuarios/suscripcion/cancelar.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Campo planAlVencer = "Gratis"
  - Campo success = true

### ✅ Caso 2: Sin suscripción activa
- **Precondición:** El usuario tiene plan Gratis.
- **Acción:** Ejecutar POST para cancelar.
- **Resultado esperado:**
  - Código HTTP 409 Conflict
  - Campo mensaje = "No tienes una suscripción Plus activa"

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] El endpoint cancela correctamente la suscripción.
- [ ] El plan se mantiene activo hasta la fecha de vencimiento.
- [ ] No se generan cobros futuros tras la cancelación.

### 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias de cancelación.
- [ ] Se cubrieron los casos de usuario sin suscripción.
- [ ] Las pruebas funcionales están documentadas y pasadas.

### 📄 Documentación Técnica
- [ ] Endpoint documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint
  - Campos de salida
  - Ejemplo de respuesta exitosa
  - Ejemplo de error

### 🔐 Manejo de Errores
- [ ] Se devuelve HTTP 409 si no hay suscripción activa.
- [ ] Se devuelve HTTP 401 si el usuario no está autenticado.
- [ ] El campo mensaje incluye texto claro y descriptivo.

.
