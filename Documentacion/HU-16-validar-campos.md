# HU-16 Validación de Campos Obligatorios al Finalizar

## 📖 Historia de Usuario

Como usuario
Quiero que al intentar finalizar el documento la API valide que no haya campos obligatorios vacíos
Para asegurarme de que mi hoja de vida esté completa antes de exportarla o compartirla

## 🔁 Flujo Esperado

- El usuario hace clic en "Finalizar hoja de vida".
- El sistema valida que todos los campos obligatorios estén completos.
- Si hay campos vacíos, el sistema retorna un error indicando cuáles son.
- Si todos están completos, el sistema marca la hoja de vida como finalizada.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] Se expone un endpoint POST para finalizar la hoja de vida.
- [ ] Se validan todos los campos obligatorios definidos en la plantilla.
- [ ] Si hay campos vacíos, se retorna HTTP 400 con detalle de los campos faltantes.

### 2. 📆 Estructura de la información
- [ ] Si hay campos vacíos, el sistema retorna:
```
{
  "mensaje": "Existen campos obligatorios sin completar",
  "data": {
    "camposFaltantes": [
      "Perfil profesional",
      "Experiencia laboral"
    ]
  },
  "success": false
}
```
- [ ] Si todo está completo, el sistema retorna:
```
{
  "mensaje": "Hoja de vida finalizada exitosamente",
  "data": { "id": 1, "estado": "finalizada" },
  "success": true
}
```

## 🔧 Notas Técnicas

### 🚀 Endpoint – Finalizar Hoja de Vida
- **Método HTTP:** POST
- **Ruta:** /api/v1/hojas-de-vida/{id}/finalizar

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Finalización exitosa
- **Precondición:** Todos los campos obligatorios están completos.
- **Acción:** Ejecutar POST /api/v1/hojas-de-vida/{id}/finalizar.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Campo estado = "finalizada"
  - Campo success = true

### ❌ Caso 2: Campos obligatorios vacíos
- **Precondición:** Hay campos obligatorios sin completar.
- **Acción:** Ejecutar POST con campos vacíos.
- **Resultado esperado:**
  - Código HTTP 400 Bad Request
  - Campo camposFaltantes lista los campos incompletos

### ❌ Caso 3: Hoja de vida no encontrada
- **Precondición:** El ID de la hoja de vida no existe.
- **Acción:** Ejecutar POST con ID inexistente.
- **Resultado esperado:**
  - Código HTTP 404 Not Found
  - Campo mensaje = "Hoja de vida no encontrada"

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] El endpoint valida correctamente todos los campos obligatorios.
- [ ] La hoja de vida queda marcada como finalizada si todo está completo.
- [ ] Se listan todos los campos faltantes en caso de error.

### 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias de validación de campos.
- [ ] Se cubrieron los casos de múltiples campos faltantes.
- [ ] Las pruebas funcionales están documentadas y pasadas.

### 📄 Documentación Técnica
- [ ] Endpoint documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Campos obligatorios validados
  - Ejemplo de respuesta exitosa
  - Ejemplo de error

### 🔐 Manejo de Errores
- [ ] Se devuelve HTTP 400 si hay campos obligatorios vacíos.
- [ ] Se devuelve HTTP 404 si la hoja de vida no existe.
- [ ] El campo mensaje incluye texto claro y descriptivo.

---
