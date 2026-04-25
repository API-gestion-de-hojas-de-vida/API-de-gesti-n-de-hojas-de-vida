# HU-18 Actualizar a Plan Plus

## 📖 Historia de Usuario

Como usuario Gratis
Quiero ver un botón de "Actualizar a Plus" que me redirija al flujo de pago
Para iniciar el proceso de suscripción mensual

## 🔁 Flujo Esperado

- El usuario Gratis hace clic en "Actualizar a Plus".
- El sistema verifica que el usuario tiene plan Gratis.
- El sistema retorna la información del plan Plus con el precio y beneficios.
- El usuario es redirigido al flujo de pago.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] Se expone un endpoint GET para obtener la información del plan Plus.
- [ ] Se valida que el usuario tenga plan Gratis antes de mostrar la opción.
- [ ] Se retorna el precio y beneficios del plan Plus.

### 2. 📆 Estructura de la información
- [ ] Se responde con la siguiente estructura en JSON:
{
  "mensaje": "Información del plan Plus obtenida exitosamente",
  "data": {
    "plan": "Plus",
    "precio": 9.99,
    "moneda": "USD",
    "beneficios": ["Plantillas Plus", "Exportación ilimitada", "Soporte prioritario"],
    "urlPago": "/api/v1/pagos/suscripcion/plus"
  },
  "success": true
}
- [ ] Si el usuario ya tiene plan Plus o Pro, el sistema retorna:
{
  "mensaje": "Ya cuentas con un plan superior o igual a Plus",
  "data": null,
  "success": false
}

## 🔧 Notas Técnicas

### 🚀 Endpoint – Información Plan Plus
- **Método HTTP:** GET
- **Ruta:** /api/v1/planes/plus

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Usuario Gratis consulta plan Plus
- **Precondición:** El usuario tiene plan Gratis.
- **Acción:** Ejecutar GET /api/v1/planes/plus.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Información completa del plan Plus
  - Campo success = true

### ✅ Caso 2: Usuario ya tiene plan Plus
- **Precondición:** El usuario ya tiene plan Plus.
- **Acción:** Ejecutar GET /api/v1/planes/plus.
- **Resultado esperado:**
  - Código HTTP 409 Conflict
  - Campo mensaje = "Ya cuentas con un plan superior o igual a Plus"

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] El endpoint retorna correctamente la información del plan Plus.
- [ ] Se valida el plan actual del usuario.
- [ ] Se incluye la URL de redirección al flujo de pago.

### 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias de validación de plan.
- [ ] Se cubrieron los casos de usuario con plan superior.
- [ ] Las pruebas funcionales están documentadas y pasadas.

### 📄 Documentación Técnica
- [ ] Endpoint documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint
  - Campos de salida
  - Ejemplo de respuesta exitosa
  - Ejemplo de error

### 🔐 Manejo de Errores
- [ ] Se devuelve HTTP 409 si el usuario ya tiene plan igual o superior.
- [ ] Se devuelve HTTP 401 si el usuario no está autenticado.
- [ ] El campo mensaje incluye texto claro y descriptivo.

---
