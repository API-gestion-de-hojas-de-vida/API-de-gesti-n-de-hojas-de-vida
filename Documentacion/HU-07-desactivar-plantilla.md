# [HU-07] Desactivar Plantilla Obsoleta

## 📖 Historia de Usuario

Como administrador
Quiero desactivar una plantilla obsoleta
Para que no aparezca en el catálogo público pero mantenga la integridad de las hojas de vida existentes

## 🔁 Flujo Esperado

- El administrador solicita la desactivación mediante el ID.
- El backend valida la existencia de la plantilla.
- Se actualiza la bandera booleana o estado a "inactivo" (Soft Delete). No se ejecuta un DELETE físico.
- El sistema retorna la confirmación. A partir de este momento, los endpoints de catálogo público omiten este ID.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] Se expone un endpoint PATCH para desactivar plantillas.
- [ ] Se valida que la plantilla exista y esté activa.
- [ ] Se realiza borrado lógico, no físico.
- [ ] Si la plantilla ya estaba inactiva, la API no falla de forma crítica, pero advierte del estado (409 Conflict).

### 2. 📆 Estructura de la información
- [ ] Se responde con la siguiente estructura en JSON:

```json
{
  "mensaje": "Plantilla desactivada exitosamente",
  "data": {
    "id": 1,
    "nombre": "Plantilla Antigua",
    "estado": "inactivo"
  },
  "success": true
}
```

- [ ] Si la plantilla ya está inactiva, el sistema retorna:

```json
{
  "mensaje": "La plantilla ya se encuentra desactivada",
  "data": null,
  "success": false
}
```

## 🔧 Notas Técnicas

### 🚀 Endpoint – Desactivar Plantilla
- **Método HTTP:** `PATCH`
- **Ruta:** `/api/v1/plantillas/{id}/desactivar`

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Desactivación exitosa
- **Precondición:** La plantilla existe y está activa.
- **Acción:** Ejecutar PATCH /api/v1/plantillas/{id}/desactivar.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Campo estado = "inactivo"
  - Campo success = true

### ✅ Caso 2: Plantilla ya inactiva
- **Precondición:** La plantilla ya fue desactivada previamente.
- **Acción:** Ejecutar PATCH sobre plantilla inactiva.
- **Resultado esperado:**
  - Código HTTP 409 Conflict
  - Campo mensaje = "La plantilla ya se encuentra desactivada"
  - Campo success = false

### ❌ Caso 3: Plantilla no encontrada
- **Precondición:** El ID no existe en la base de datos.
- **Acción:** Ejecutar PATCH con ID inexistente.
- **Resultado esperado:**
  - Código HTTP 404 Not Found
  - Campo mensaje = "Plantilla no encontrada"

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] El endpoint desactiva correctamente la plantilla.
- [ ] La plantilla no aparece en el catálogo público tras desactivarse.
- [ ] Las hojas de vida existentes mantienen su integridad referencial.

### 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias de borrado lógico.
- [ ] Se cubrieron los casos de error.
- [ ] Las pruebas funcionales están documentadas y pasadas.

### 📄 Documentación Técnica
- [ ] Endpoint documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint
  - Campos de entrada y salida
  - Ejemplo de respuesta exitosa
  - Ejemplo de error

### 🔐 Manejo de Errores
- [ ] Se devuelve HTTP 404 si la plantilla no existe.
- [ ] Se devuelve HTTP 409 si la plantilla ya está inactiva.
- [ ] El campo mensaje incluye texto claro y descriptivo.

