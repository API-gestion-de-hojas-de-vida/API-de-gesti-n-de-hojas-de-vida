# [HU-19] Compra de Plantilla Pro Individual

## 📖 Historia de Usuario

Como usuario
Quiero comprar una plantilla Pro individual
Para obtener acceso permanente a ese diseño específico

## 🔁 Flujo Esperado

- El usuario selecciona una plantilla Pro que desea comprar.
- El sistema verifica que el usuario no tenga ya acceso a esa plantilla.
- El usuario completa el proceso de pago.
- El sistema registra la transacción y otorga acceso permanente a la plantilla.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] Se expone un endpoint POST para comprar una plantilla Pro.
- [ ] Se valida que el usuario no tenga ya acceso a la plantilla.
- [ ] Se registra la transacción en la base de datos.
- [ ] Se otorga acceso permanente tras el pago exitoso.

### 2. 📆 Estructura de la información
- [ ] Se responde con la siguiente estructura en JSON:
{
  "mensaje": "Plantilla adquirida exitosamente",
  "data": {
    "idTransaccion": 123,
    "idPlantilla": 5,
    "nombrePlantilla": "Plantilla Ejecutiva Pro",
    "accesoPermanente": true
  },
  "success": true
}
- [ ] Si el usuario ya tiene acceso, el sistema retorna:
{
  "mensaje": "Ya tienes acceso a esta plantilla",
  "data": null,
  "success": false
}

## 🔧 Notas Técnicas

### 🚀 Endpoint – Comprar Plantilla Pro
- **Método HTTP:** POST
- **Ruta:** /api/v1/pagos/plantillas/{id}/comprar

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Compra exitosa
- **Precondición:** El usuario no tiene acceso a la plantilla y el pago es válido.
- **Acción:** Ejecutar POST con datos de pago válidos.
- **Resultado esperado:**
  - Código HTTP 201 Created
  - Campo accesoPermanente = true
  - Campo success = true

### ✅ Caso 2: Usuario ya tiene acceso
- **Precondición:** El usuario ya compró la plantilla anteriormente.
- **Acción:** Ejecutar POST para comprar la misma plantilla.
- **Resultado esperado:**
  - Código HTTP 409 Conflict
  - Campo mensaje = "Ya tienes acceso a esta plantilla"

### ❌ Caso 3: Pago fallido
- **Precondición:** Los datos de pago son inválidos.
- **Acción:** Ejecutar POST con tarjeta inválida.
- **Resultado esperado:**
  - Código HTTP 402 Payment Required
  - Campo mensaje = "No fue posible procesar el pago"

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] El endpoint registra correctamente la transacción.
- [ ] Se otorga acceso permanente tras el pago exitoso.
- [ ] Se valida que el usuario no tenga ya acceso.

### 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias de compra.
- [ ] Se cubrieron los casos de pago fallido y acceso duplicado.
- [ ] Las pruebas funcionales están documentadas y pasadas.

### 📄 Documentación Técnica
- [ ] Endpoint documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint
  - Campos de entrada y salida
  - Ejemplo de respuesta exitosa
  - Ejemplo de error

### 🔐 Manejo de Errores
- [ ] Se devuelve HTTP 409 si el usuario ya tiene acceso.
- [ ] Se devuelve HTTP 402 si el pago falla.
- [ ] El campo mensaje incluye texto claro y descriptivo.

