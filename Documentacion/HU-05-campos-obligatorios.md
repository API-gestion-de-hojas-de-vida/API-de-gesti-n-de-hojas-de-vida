# [HU-05] Marcar Campos Obligatorios en Plantilla

## 📖 Historia de Usuario

Como administrador
Quiero marcar qué campos de la plantilla son obligatorios
Para garantizar que ninguna hoja de vida quede incompleta

## 🔁 Flujo Esperado

- El administrador selecciona una plantilla existente.
- El administrador marca qué campos son obligatorios.
- El sistema guarda la configuración de campos obligatorios.
- El sistema retorna confirmación de actualización exitosa.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] Se expone un endpoint PATCH para actualizar campos obligatorios.
- [ ] Se valida que la plantilla exista.
- [ ] Se valida que los campos marcados existan en la estructura.

### 2. 📆 Estructura de la información
- [ ] Se responde con la siguiente estructura en JSON:

```json
{
  "mensaje": "Campos obligatorios actualizados exitosamente",
  "data": {
    "id": 1,
    "nombre": "Plantilla Moderna",
    "camposObligatorios": ["Perfil", "Experiencia"]
  },
  "success": true
}
```

- [ ] Si la plantilla no existe, el sistema retorna:

```json
{
  "mensaje": "Plantilla no encontrada",
  "data": null,
  "success": false
}
```

## 🔧 Notas Técnicas

### 🚀 Endpoint – Marcar Campos Obligatorios
- **Método HTTP:** `PATCH`
- **Ruta:** `/api/v1/plantillas/{id}/campos-obligatorios`

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Actualización exitosa
- **Precondición:** La plantilla existe en la base de datos.
- **Acción:** Ejecutar PATCH con campos válidos.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Campos obligatorios actualizados correctamente
  - Campo success = true

### ✅ Caso 2: Plantilla no encontrada
- **Precondición:** El ID de la plantilla no existe.
- **Acción:** Ejecutar PATCH con ID inexistente.
- **Resultado esperado:**
  - Código HTTP 404 Not Found
  - Campo mensaje = "Plantilla no encontrada"
  - Campo success = false

### ❌ Caso 3: Campos inválidos
- **Precondición:** Los campos enviados no existen en la estructura.
- **Acción:** Ejecutar PATCH con campos inexistentes.
- **Resultado esperado:**
  - Código HTTP 400 Bad Request
  - Campo mensaje = "Los campos enviados no existen en la plantilla"

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] El endpoint actualiza correctamente los campos obligatorios.
- [ ] Se valida que la plantilla exista.
- [ ] Se valida que los campos existan en la estructura.

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
- [ ] Se devuelve HTTP 404 si la plantilla no existe.
- [ ] Se devuelve HTTP 400 si los campos son inválidos.
- [ ] El campo mensaje incluye texto claro y descriptivo.
