
# [HU-04] Crear Estructura Base de Plantilla

## 📖 Historia de Usuario

Como administrador
Quiero crear la estructura base de una nueva plantilla definiendo sus secciones
Para que el frontend sepa qué campos debe renderizar dinámicamente

## 🔁 Flujo Esperado

- El administrador ingresa el nombre de la plantilla, el array de secciones que la componen y su categoría por defecto.
- El backend verifica mediante el token que el usuario tiene permisos de "Administrador".
- El sistema valida que no exista otra plantilla activa con el mismo nombre exacto (ignorando espacios extra).
- El sistema guarda la entidad en la base de datos y la retorna con su nuevo ID.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] Se debe validar autorización: Solo el rol Administrador puede consumir este endpoint.
- [ ] El array de secciones debe contener al menos un elemento y no permitir strings vacíos.
- [ ] Se debe aplicar trim al nombre para evitar duplicados accidentales.

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

