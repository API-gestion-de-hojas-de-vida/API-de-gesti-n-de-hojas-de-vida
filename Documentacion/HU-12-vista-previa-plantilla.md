# [HU-12] Vista Previa Ampliada de Plantilla

## 📖 Historia de Usuario

Como usuario
Quiero hacer clic en una plantilla y ver una vista previa ampliada con datos de ejemplo
Para evaluar el diseño antes de usarlo

## 🔁 Flujo Esperado

- El usuario hace clic en una plantilla del catálogo.
- El sistema consulta la plantilla por su ID.
- El sistema retorna la estructura completa con datos de ejemplo.
- El usuario visualiza el mockup de la plantilla.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] Se expone un endpoint GET para obtener el detalle de una plantilla.
- [ ] Se valida que la plantilla exista y esté activa.
- [ ] Se retornan datos de ejemplo para el mockup.

### 2. 📆 Estructura de la información
- [ ] Se responde con la siguiente estructura en JSON:
{
  "mensaje": "Plantilla obtenida exitosamente",
  "data": {
    "id": 1,
    "nombre": "Plantilla Moderna",
    "categoria": "Gratis",
    "secciones": ["Perfil", "Experiencia", "Educación"],
    "datosEjemplo": {
      "nombre": "Juan Pérez",
      "cargo": "Desarrollador Backend",
      "experiencia": "3 años"
    }
  },
  "success": true
}
- [ ] Si la plantilla no existe, el sistema retorna:
{
  "mensaje": "Plantilla no encontrada",
  "data": null,
  "success": false
}

## 🔧 Notas Técnicas

### 🚀 Endpoint – Vista Previa de Plantilla
- **Método HTTP:** GET
- **Ruta:** /api/v1/plantillas/{id}/preview

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Vista previa exitosa
- **Precondición:** La plantilla existe y está activa.
- **Acción:** Ejecutar GET /api/v1/plantillas/{id}/preview.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Datos de ejemplo incluidos
  - Campo success = true

### ✅ Caso 2: Plantilla no encontrada
- **Precondición:** El ID no existe en la base de datos.
- **Acción:** Ejecutar GET con ID inexistente.
- **Resultado esperado:**
  - Código HTTP 404 Not Found
  - Campo mensaje = "Plantilla no encontrada"
  - Campo success = false

### ❌ Caso 3: Plantilla inactiva
- **Precondición:** La plantilla existe pero está desactivada.
- **Acción:** Ejecutar GET con ID de plantilla inactiva.
- **Resultado esperado:**
  - Código HTTP 404 Not Found
  - Campo mensaje = "Plantilla no disponible"

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] El endpoint retorna la vista previa correctamente.
- [ ] Los datos de ejemplo están presentes en la respuesta.
- [ ] No se retornan plantillas inactivas.

### 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias de la vista previa.
- [ ] Se cubrieron los casos de error.
- [ ] Las pruebas funcionales están documentadas y pasadas.

### 📄 Documentación Técnica
- [ ] Endpoint documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint
  - Campos de salida
  - Ejemplo de respuesta exitosa
  - Ejemplo de error

### 🔐 Manejo de Errores
- [ ] Se devuelve HTTP 404 si la plantilla no existe o está inactiva.
- [ ] El campo mensaje incluye texto claro y descriptivo.
