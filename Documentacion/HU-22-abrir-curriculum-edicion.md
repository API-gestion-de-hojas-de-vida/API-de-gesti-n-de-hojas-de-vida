# [HU-22] Abrir Hoja de Vida en Modo Edición

## 📖 Historia de Usuario

Como usuario
Quiero poder abrir una hoja de vida previamente creada en modo edición
Para que la API consulte mis datos y los inyecte de nuevo en el formulario

## 🔁 Flujo Esperado

- El usuario selecciona una hoja de vida existente para editar.
- El sistema consulta todos los datos de la hoja de vida por su ID.
- El sistema retorna los datos completos para cargarlos en el formulario.
- El usuario puede modificar cualquier sección.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] Se expone un endpoint GET para obtener los datos de una hoja de vida en modo edición.
- [ ] Se valida que la hoja de vida pertenezca al usuario autenticado.
- [ ] Se retornan todos los datos incluyendo bloques de experiencia y educación.

### 2. 📆 Estructura de la información
- [ ] Se responde con la siguiente estructura en JSON:
{
  "mensaje": "Hoja de vida cargada exitosamente",
  "data": {
    "id": 1,
    "estado": "borrador",
    "plantilla": { "id": 2, "nombre": "Plantilla Moderna" },
    "perfil": { "nombre": "Juan Pérez", "cargo": "Desarrollador" },
    "experiencia": [
      { "id": 1, "empresa": "Tech Corp", "cargo": "Backend Dev" }
    ],
    "educacion": [
      { "id": 1, "institucion": "Universidad X", "titulo": "Ing. Sistemas" }
    ]
  },
  "success": true
}
- [ ] Si la hoja de vida no pertenece al usuario, el sistema retorna:
{
  "mensaje": "No tienes permiso para editar esta hoja de vida",
  "data": null,
  "success": false
}

## 🔧 Notas Técnicas

### 🚀 Endpoint – Cargar Hoja de Vida para Edición
- **Método HTTP:** GET
- **Ruta:** /api/v1/hojas-de-vida/{id}/editar

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Carga exitosa
- **Precondición:** La hoja de vida existe y pertenece al usuario.
- **Acción:** Ejecutar GET /api/v1/hojas-de-vida/{id}/editar.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Datos completos de la hoja de vida
  - Campo success = true

### ❌ Caso 2: Hoja de vida de otro usuario
- **Precondición:** La hoja de vida pertenece a otro usuario.
- **Acción:** Ejecutar GET con ID de otra hoja de vida.
- **Resultado esperado:**
  - Código HTTP 403 Forbidden
  - Campo mensaje = "No tienes permiso para editar esta hoja de vida"

### ❌ Caso 3: Hoja de vida no encontrada
- **Precondición:** El ID no existe en la base de datos.
- **Acción:** Ejecutar GET con ID inexistente.
- **Resultado esperado:**
  - Código HTTP 404 Not Found
  - Campo mensaje = "Hoja de vida no encontrada"

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] El endpoint retorna todos los datos de la hoja de vida.
- [ ] Se valida que la hoja pertenezca al usuario autenticado.
- [ ] Se incluyen todos los bloques de experiencia y educación.

### 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias de carga de datos.
- [ ] Se cubrieron los casos de acceso no autorizado.
- [ ] Las pruebas funcionales están documentadas y pasadas.

### 📄 Documentación Técnica
- [ ] Endpoint documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint
  - Estructura completa de la respuesta
  - Ejemplo de respuesta exitosa
  - Ejemplo de error

### 🔐 Manejo de Errores
- [ ] Se devuelve HTTP 403 si la hoja no pertenece al usuario.
- [ ] Se devuelve HTTP 404 si la hoja no existe.
- [ ] El campo mensaje incluye texto claro y descriptivo.
