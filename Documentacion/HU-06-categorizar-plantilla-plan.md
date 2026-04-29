# [HU-06] Categorizar Plantilla por Plan


## 📖 Historia de Usuario

Como administrador
Quiero categorizar cada plantilla como "Gratis", "Plus" o "Pro"
Para establecer las reglas de autorización de uso en la API

## 🔁 Flujo Esperado

- El administrador envía el ID de la plantilla y el string de la nueva categoría.
- El backend valida el rol de administrador y la existencia de la plantilla.
- El sistema valida que el string enviado coincida exactamente con un enum permitido (Gratis, Plus, Pro).
- El sistema actualiza el registro y retorna el objeto actualizado.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] Se expone un endpoint PATCH para categorizar plantillas.
- [ ] Se valida que la categoría sea una de las tres permitidas.
- [ ] Se valida que la plantilla exista.

### 2. 📆 Estructura de la información
- [ ] Se responde con la siguiente estructura en JSON:

```json
{
  "mensaje": "Categoría asignada exitosamente",
  "data": {
    "id": 1,
    "nombre": "Plantilla Moderna",
    "categoria": "Plus"
  },
  "success": true
}
```

- [ ] Si la categoría no es válida, el sistema retorna:

```json
{
  "mensaje": "Categoría no válida. Debe ser Gratis, Plus o Pro",
  "data": null,
  "success": false
}
```

## 🔧 Notas Técnicas

### 🚀 Endpoint – Categorizar Plantilla
- **Método HTTP:** `PATCH`
- **Ruta:** `/api/v1/plantillas/{id}/categoria`

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Categorización exitosa
- **Precondición:** La plantilla existe y la categoría es válida.
- **Acción:** Ejecutar PATCH con categoría "Plus".
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Campo categoria = "Plus"
  - Campo success = true

### ✅ Caso 2: Categoría inválida
- **Precondición:** El administrador envía una categoría no permitida.
- **Acción:** Ejecutar PATCH con categoría "Premium".
- **Resultado esperado:**
  - Código HTTP 400 Bad Request
  - Campo mensaje = "Categoría no válida. Debe ser Gratis, Plus o Pro"
  - Campo success = false

### ❌ Caso 3: Plantilla no encontrada
- **Precondición:** El ID de la plantilla no existe.
- **Acción:** Ejecutar PATCH con ID inexistente.
- **Resultado esperado:**
  - Código HTTP 404 Not Found
  - Campo mensaje = "Plantilla no encontrada"

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] El endpoint categoriza correctamente la plantilla.
- [ ] Se valida que la categoría sea una de las permitidas.
- [ ] Se valida que la plantilla exista.

### 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias de validación.
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
- [ ] Se devuelve HTTP 400 si la categoría no es válida.
- [ ] Se devuelve HTTP 404 si la plantilla no existe.
- [ ] El campo mensaje incluye texto claro y descriptivo.
