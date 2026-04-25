# [HU-04] Crear Estructura Base de Plantilla

## 📖 Historia de Usuario

Como administrador
Quiero crear la estructura base de una nueva plantilla definiendo sus secciones
Para que el frontend sepa qué campos debe renderizar dinámicamente

## 🔁 Flujo Esperado

- El administrador define el nombre de la plantilla y sus secciones.
- El sistema valida que el nombre no esté duplicado.
- El sistema guarda la estructura de la plantilla en la base de datos.
- El sistema retorna confirmación de creación exitosa con el ID asignado.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] Se expone un endpoint POST para crear plantillas.
- [ ] Se valida que el nombre de la plantilla sea único.
- [ ] Se valida que las secciones no estén vacías.

### 2. 📆 Estructura de la información
- [ ] Se responde con la siguiente estructura en JSON:

```json
{
  "mensaje": "Plantilla creada exitosamente",
  "data": {
    "id": 1,
    "nombre": "Plantilla Moderna",
    "secciones": ["Perfil", "Experiencia", "Educación", "Habilidades"],
    "categoria": "Gratis"
  },
  "success": true
}
```

- [ ] Si el nombre ya existe, el sistema retorna:

```json
{
  "mensaje": "Ya existe una plantilla con ese nombre",
  "data": null,
  "success": false
}
```

## 🔧 Notas Técnicas

### 🚀 Endpoint – Crear Plantilla
- **Método HTTP:** `POST`
- **Ruta:** `/api/v1/plantillas`

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Creación exitosa
- **Precondición:** El nombre de la plantilla no existe en la base de datos.
- **Acción:** Ejecutar POST /api/v1/plantillas con datos válidos.
- **Resultado esperado:**
  - Código HTTP 201 Created
  - Campo id generado correctamente
  - Campo success = true

### ✅ Caso 2: Nombre duplicado
- **Precondición:** Ya existe una plantilla con el mismo nombre.
- **Acción:** Ejecutar POST con nombre duplicado.
- **Resultado esperado:**
  - Código HTTP 409 Conflict
  - Campo mensaje = "Ya existe una plantilla con ese nombre"
  - Campo success = false

### ❌ Caso 3: Secciones vacías
- **Precondición:** El administrador no define ninguna sección.
- **Acción:** Ejecutar POST con secciones vacías.
- **Resultado esperado:**
  - Código HTTP 400 Bad Request
  - Campo mensaje = "Las secciones no pueden estar vacías"

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] El endpoint crea correctamente la estructura de la plantilla.
- [ ] Se valida unicidad del nombre.
- [ ] Las secciones quedan guardadas correctamente.

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
- [ ] Se devuelve HTTP 409 si el nombre ya existe.
- [ ] Se devuelve HTTP 400 si las secciones están vacías.
- [ ] El campo mensaje incluye texto claro y descriptivo.
