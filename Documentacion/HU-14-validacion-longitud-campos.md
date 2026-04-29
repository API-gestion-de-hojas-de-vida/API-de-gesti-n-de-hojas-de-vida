# [HU-14] Validación de Longitud de Campos

📖 Historia de Usuario

Como usuario
Quiero llenar las secciones de texto de la hoja de vida y que la plataforma valide la longitud máxima de caracteres
Para evitar errores al guardar en la base de datos

🔁 Flujo Esperado

* El usuario llena los campos de texto de su hoja de vida.
* El sistema recibe todos los datos del formulario.
* El sistema valida que cada campo no supere la longitud máxima permitida antes de guardar.
* El sistema evalúa todos los campos y acumula los errores encontrados.
* Si algún campo supera el límite, el sistema retorna todos los errores sin guardar información.
* Si todos los campos son válidos, el sistema guarda la información en una única operación.

✅ Criterios de Aceptación

1. 🔍 Estructura y lógica del servicio

* Se valida la longitud máxima de cada campo antes de guardar.
* Se retorna un error descriptivo indicando qué campo supera el límite.
* Se validan todos los campos en una sola ejecución.
* No se guarda información parcial si existen errores.
* Los límites de caracteres están definidos por campo.

1. 📆 Estructura de la información

* Si un campo supera el límite, el sistema retorna:
  ```json
    { “mensaje”: “El campo ‘descripción’ supera la longitud máxima permitida de 500 caracteres”, “data”: null, “success”: false }
  ```
* El mensaje incluye el nombre del campo y su límite máximo permitido.
* Se pueden listar múltiples campos inválidos en una sola respuesta.
* Si todos los campos son válidos, el sistema retorna:
```json
    { “mensaje”: “Información guardada exitosamente”, “data”: { “id”: 1 }, “success”: true }
```

## 🔧 Notas Técnicas

### 🚀 Endpoint – Guardar Secciones de Hoja de Vida
- **Método HTTP:** POST
- **Ruta:** /api/v1/hojas-de-vida/{id}/secciones

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Guardado exitoso
- **Precondición:** Todos los campos cumplen con la longitud máxima.
- **Acción:** Ejecutar POST con datos válidos.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Campo success = true

### ❌ Caso 2: Campo supera longitud máxima
- **Precondición:** El campo descripción supera 500 caracteres.
- **Acción:** Ejecutar POST con descripción de 600 caracteres.
- **Resultado esperado:**
  - Código HTTP 400 Bad Request
  - Campo mensaje indica qué campo supera el límite

### ❌ Caso 3: Múltiples campos inválidos
- **Precondición:** Varios campos superan su longitud máxima.
- **Acción:** Ejecutar POST con múltiples campos inválidos.
- **Resultado esperado:**
  - Código HTTP 400 Bad Request
  - Campo mensaje lista todos los campos que superan el límite

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] Se valida la longitud de todos los campos antes de guardar.
- [ ] Los mensajes de error indican exactamente qué campo falla.
- [ ] Los límites de caracteres están documentados.

### 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias de validación de longitud.
- [ ] Se cubrieron los casos de múltiples errores.
- [ ] Las pruebas funcionales están documentadas y pasadas.

### 📄 Documentación Técnica
- [ ] Endpoint documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Límites de caracteres por campo
  - Ejemplo de respuesta exitosa
  - Ejemplo de error

### 🔐 Manejo de Errores
- [ ] Se devuelve HTTP 400 si algún campo supera el límite.
- [ ] El campo mensaje incluye texto claro indicando el campo y límite.
