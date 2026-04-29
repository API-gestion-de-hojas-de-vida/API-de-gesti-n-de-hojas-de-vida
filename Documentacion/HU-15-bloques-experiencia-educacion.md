# HU-15 Agregar Bloques Dinámicos de Experiencia y Educación

📖 Historia de Usuario

Como usuario
Quiero agregar dinámicamente múltiples bloques de Experiencia Laboral y Educación
Para reflejar toda mi trayectoria profesional y académica

🔁 Flujo Esperado

* El usuario hace clic en “Agregar experiencia” o “Agregar educación”.
* El sistema valida el tipo de bloque solicitado.
* El sistema agrega un nuevo bloque vacío al formulario.
* El usuario llena el bloque con su información.
* El sistema valida los campos obligatorios del bloque.
* El sistema guarda el bloque como un registro independiente asociado a la hoja de vida.
* El usuario puede repetir el proceso múltiples veces sin afectar los bloques existentes.

✅ Criterios de Aceptación

1. 🔍 Estructura y lógica del servicio

* Se expone un endpoint POST para agregar bloques de experiencia y educación.
* Se permite agregar múltiples bloques por hoja de vida.
* Cada bloque se guarda como un registro independiente relacionado.
* Se valida el tipo de bloque (experiencia o educación).
* Se validan los campos obligatorios antes de guardar.

1. 📆 Estructura de la información

* Se responde con la siguiente estructura en JSON:
    { “mensaje”: “Bloque agregado exitosamente”, “data”: { “id”: 1, 
    “tipo”: “experiencia”,
    “empresa”: “Tech Corp”, 
    “cargo”: “Desarrollador Backend”,
    “fechaInicio”: “2022-01-01”,
    “fechaFin”: “2024-01-01” },
    “success”: true }
* Cada respuesta incluye el ID del bloque creado.
* Los campos de fecha cumplen con un formato válido.
* El campo tipo siempre está presente en la respuesta.



## 🔧 Notas Técnicas

### 🚀 Endpoints – Agregar Bloque
- **Método HTTP:** POST
- **Ruta experiencia:** /api/v1/hojas-de-vida/{id}/experiencia
- **Ruta educación:** /api/v1/hojas-de-vida/{id}/educacion

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Bloque agregado exitosamente
- **Precondición:** La hoja de vida existe y los datos son válidos.
- **Acción:** Ejecutar POST con datos completos.
- **Resultado esperado:**
  - Código HTTP 201 Created
  - Bloque guardado correctamente
  - Campo success = true

### ✅ Caso 2: Múltiples bloques
- **Precondición:** La hoja de vida ya tiene bloques existentes.
- **Acción:** Ejecutar POST para agregar un bloque adicional.
- **Resultado esperado:**
  - Código HTTP 201 Created
  - Nuevo bloque agregado sin afectar los existentes

### ❌ Caso 3: Campos obligatorios vacíos
- **Precondición:** El usuario no completa los campos obligatorios.
- **Acción:** Ejecutar POST sin campo empresa.
- **Resultado esperado:**
  - Código HTTP 400 Bad Request
  - Campo mensaje = "Los campos empresa y cargo son obligatorios"

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] Se pueden agregar múltiples bloques por hoja de vida.
- [ ] Cada bloque se guarda como registro independiente.
- [ ] Se validan los campos obligatorios de cada bloque.

### 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias de inserción de bloques.
- [ ] Se cubrieron los casos de múltiples bloques.
- [ ] Las pruebas funcionales están documentadas y pasadas.

### 📄 Documentación Técnica
- [ ] Endpoints documentados en Swagger / OpenAPI.
- [ ] Se describe:
  - Campos obligatorios por bloque
  - Ejemplo de respuesta exitosa
  - Ejemplo de error

### 🔐 Manejo de Errores
- [ ] Se devuelve HTTP 400 si faltan campos obligatorios.
- [ ] Se devuelve HTTP 404 si la hoja de vida no existe.
- [ ] El campo mensaje incluye texto claro y descriptivo.

---
