# [HU-20] Cancelar Suscripción Plus

## 📖 Historia de Usuario

Como usuario Plus
Quiero poder cancelar mi suscripción desde mi perfil
Para actualizar mi estado en la base de datos y evitar futuros cobros

## 🔁 Flujo Esperado

- El usuario autenticado accede a la sección "Mi Plan" dentro de su perfil.
- El sistema verifica que el usuario tenga una suscripción Plus activa y vigente.
- El sistema muestra al usuario información detallada sobre las consecuencias de la cancelación, incluyendo la fecha exacta hasta la que tendrá acceso a las funcionalidades Plus y qué ocurrirá con sus hojas de vida que usen plantillas Plus.
- El usuario confirma explícitamente que desea cancelar mediante un segundo paso de confirmación.
- El sistema verifica que no haya una transacción de pago en proceso antes de proceder.
- El sistema programa la cancelación para que se ejecute al finalizar el período ya pagado, sin realizar ningún cobro adicional.
- El sistema actualiza el estado de la suscripción a "cancelada pendiente de vencimiento".
- El sistema envía un correo de confirmación al usuario con la fecha exacta en que su plan regresará a Gratis.
- Al llegar la fecha de vencimiento, el sistema cambia automáticamente el estado del usuario a Gratis y restringe el acceso a funcionalidades exclusivas del plan Plus.
- Las hojas de vida que usen plantillas Plus quedan visibles pero no editables una vez que el plan venza.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio

- [ ] Se expone un endpoint POST para solicitar la cancelación de la suscripción.
- [ ] Se valida que el usuario tenga un plan Plus activo antes de proceder.
- [ ] Se valida que no haya una transacción de pago en proceso al momento de cancelar.
- [ ] La cancelación no es inmediata, el plan permanece activo hasta el último día del período pagado.
- [ ] El sistema programa automáticamente el cambio de estado a Gratis al vencer el período.
- [ ] Se requiere confirmación explícita del usuario antes de proceder con la cancelación.
- [ ] Se envía correo de confirmación con fecha de vencimiento del plan Plus.
- [ ] Se registra la fecha de cancelación, el motivo si el usuario lo proporciona y el ID del usuario en un log de auditoría.
- [ ] Las plantillas Plus asignadas a hojas de vida existentes se mantienen visibles pero se bloquea su edición una vez que el plan venza.
- [ ] El sistema no permite iniciar una nueva suscripción Plus si ya hay una cancelación pendiente de vencimiento, hasta que el período actual termine.

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
