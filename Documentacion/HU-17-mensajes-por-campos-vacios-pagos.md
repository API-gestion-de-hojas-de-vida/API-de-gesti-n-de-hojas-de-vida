# HU-17 Mensajes de Error por Campos Faltantes

## 📖 Historia de Usuario

Como usuario
Quiero ver mensajes de error claros en la interfaz indicando exactamente qué campos me faltan por llenar
Para corregir rápidamente mi hoja de vida sin adivinar qué está mal

## 🔁 Flujo Esperado

- El usuario intenta guardar o finalizar su hoja de vida con campos incompletos.
- El sistema identifica todos los campos vacíos o inválidos.
- El sistema retorna un listado claro de los campos que faltan.
- El usuario visualiza los mensajes de error en la interfaz.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] El sistema identifica y lista todos los campos faltantes en una sola respuesta.
- [ ] Los mensajes de error son claros y específicos por campo.
- [ ] Se retorna HTTP 400 con el detalle completo de errores.

2. 📆 **Estructura de la información**
* Respuesta:

```json
{
  "mensaje": "Existen errores en el formulario",
  "data": {
    "errores": [
      {
        "campo": "nombre",
        "mensaje": "El nombre es obligatorio"
      },
      {
        "campo": "experiencia",
        "mensaje": "Debe agregar al menos una experiencia laboral"
      }
    ]
  },
  "success": false
}
```

## 🔧 Notas Técnicas

### 🚀 Endpoint – Validación de Formulario
- **Método HTTP:** POST
- **Ruta:** /api/v1/hojas-de-vida/{id}/validar

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Un solo campo faltante
- **Precondición:** Solo el campo nombre está vacío.
- **Acción:** Ejecutar POST con nombre vacío.
- **Resultado esperado:**
  - Código HTTP 400 Bad Request
  - Un solo error en la lista
  - Campo success = false

### ✅ Caso 2: Múltiples campos faltantes
- **Precondición:** Varios campos obligatorios están vacíos.
- **Acción:** Ejecutar POST con múltiples campos vacíos.
- **Resultado esperado:**
  - Código HTTP 400 Bad Request
  - Lista completa de todos los campos faltantes

### ✅ Caso 3: Sin errores
- **Precondición:** Todos los campos están completos.
- **Acción:** Ejecutar POST con todos los campos llenos.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Campo success = true

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] El sistema lista todos los errores en una sola respuesta.
- [ ] Los mensajes son claros y específicos por campo.
- [ ] No se requieren múltiples intentos para conocer todos los errores.

### 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias de validación múltiple.
- [ ] Se cubrieron los casos de uno y múltiples errores.
- [ ] Las pruebas funcionales están documentadas y pasadas.

### 📄 Documentación Técnica
- [ ] Endpoint documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Estructura de errores por campo
  - Ejemplo de respuesta con errores
  - Ejemplo de respuesta exitosa

### 🔐 Manejo de Errores
- [ ] Se devuelve HTTP 400 con lista completa de errores.
- [ ] Se devuelve HTTP 404 si la hoja de vida no existe.
- [ ] El campo mensaje incluye texto claro y descriptivo.

---
