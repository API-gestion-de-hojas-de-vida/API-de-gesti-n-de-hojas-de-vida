# [HU-10] Filtrar Catálogo por Plan

## 📖 Historia de Usuario

Como usuario
Quiero poder filtrar el catálogo por plan (Gratis, Plus, Pro)
Para visualizar rápidamente las opciones que se ajustan a mi nivel de cuenta

## 🔁 Flujo Esperado

- El usuario selecciona un filtro de plan en el catálogo.
- El sistema consulta la base de datos filtrando por la categoría seleccionada.
- El backend aplica la cláusula WHERE categoria = ? AND estado = 'activo' en la base de datos.
- Se retorna la lista filtrada.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] Se expone un endpoint GET con parámetro de filtro por plan.
- [ ] Se valida que el plan sea uno de los permitidos: Gratis, Plus, Pro.
- [ ] Solo se retornan plantillas activas.

### 2. 📆 Estructura de la información
- [ ] Se responde con la siguiente estructura en JSON:
{
  "mensaje": "Filtro aplicado exitosamente",
  "data": [
    { "id": 1, "nombre": "Plantilla Moderna", "categoria": "Gratis" },
    { "id": 3, "nombre": "Plantilla Simple", "categoria": "Gratis" }
  ],
  "success": true
}
- [ ] Si no hay plantillas para ese plan, el sistema retorna:
{
  "mensaje": "No hay plantillas disponibles para este plan",
  "data": [],
  "success": true
}

## 🔧 Notas Técnicas

### 🚀 Endpoint – Filtrar por Plan
- **Método HTTP:** GET
- **Ruta:** /api/v1/plantillas?categoria=Gratis

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Filtro exitoso
- **Precondición:** Existen plantillas activas con la categoría solicitada.
- **Acción:** Ejecutar GET con categoria=Gratis.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Solo plantillas de categoría Gratis
  - Campo success = true

### ✅ Caso 2: Sin resultados
- **Precondición:** No hay plantillas activas para el plan solicitado.
- **Acción:** Ejecutar GET con categoria=Pro.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Lista vacía
  - Campo success = true

### ❌ Caso 3: Categoría inválida
- **Precondición:** El usuario envía una categoría no permitida.
- **Acción:** Ejecutar GET con categoria=Premium.
- **Resultado esperado:**
  - Código HTTP 400 Bad Request
  - Campo mensaje = "Categoría no válida. Debe ser Gratis, Plus o Pro"

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] El endpoint filtra correctamente por categoría.
- [ ] Solo se incluyen plantillas activas.
- [ ] Se valida que la categoría sea una de las permitidas.

### 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias de filtrado.
- [ ] Se cubrieron los casos de error.
- [ ] Las pruebas funcionales están documentadas y pasadas.

### 📄 Documentación Técnica
- [ ] Endpoint documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint
  - Parámetros de entrada
  - Ejemplo de respuesta exitosa
  - Ejemplo de error

### 🔐 Manejo de Errores
- [ ] Se devuelve HTTP 400 si la categoría no es válida.
- [ ] Se devuelve HTTP 500 si hay error en la base de datos.
- [ ] El campo mensaje incluye texto claro y descriptivo.

