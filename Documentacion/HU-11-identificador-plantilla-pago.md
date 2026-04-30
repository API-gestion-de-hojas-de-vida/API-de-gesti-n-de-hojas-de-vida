 # [HU-11] Indicador Visual de Plantilla de Pago

## 📖 Historia de Usuario

Como usuario
Quiero ver un indicador visual en cada tarjeta del catálogo
Para identificar inmediatamente si una plantilla es de pago o gratuita

## 🔁 Flujo Esperado

- Durante la consulta del catálogo (GET /plantillas), el backend formatea la respuesta.
- Se evalúa la columna categoria. Si es "Plus" o "Pro", se inyecta dinámicamente un atributo booleano es De Pago: true, sino es De Pago: false.
- El sistema retorna cada plantilla con su categoría incluida.
- El frontend muestra un indicador visual según la categoría.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] El campo esDePago debe ser un tipo Booleano estricto (true/false), no un string ("true").
- [ ] El campo categoria puede ser Gratis, Plus o Pro.
- [ ] Solo se retornan plantillas activas.

### 2. 📆 Estructura de la información
- [ ] Se responde con la siguiente estructura en JSON:
{
  "mensaje": "Catálogo obtenido exitosamente",
  "data": [
    { "id": 1, "nombre": "Plantilla Moderna", "categoria": "Gratis", "esDePago": false },
    { "id": 2, "nombre": "Plantilla Ejecutiva", "categoria": "Pro", "esDePago": true }
  ],
  "success": true
}

## 🔧 Notas Técnicas

### 🚀 Endpoint – Catálogo con Indicador
- **Método HTTP:** GET
- **Ruta:** /api/v1/plantillas

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Indicador correcto en plantilla gratuita
- **Precondición:** Existe una plantilla con categoría Gratis.
- **Acción:** Ejecutar GET /api/v1/plantillas.
- **Resultado esperado:**
  - Campo esDePago = false para plantillas Gratis
  - Campo success = true

### ✅ Caso 2: Indicador correcto en plantilla de pago
- **Precondición:** Existe una plantilla con categoría Pro o Plus.
- **Acción:** Ejecutar GET /api/v1/plantillas.
- **Resultado esperado:**
  - Campo esDePago = true para plantillas Plus y Pro
  - Campo success = true

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] Cada plantilla incluye el campo esDePago correctamente.
- [ ] El campo categoria está presente en todas las plantillas.
- [ ] Solo se incluyen plantillas activas.

### 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias del campo esDePago.
- [ ] Se cubrieron todos los tipos de categoría.
- [ ] Las pruebas funcionales están documentadas y pasadas.

### 📄 Documentación Técnica
- [ ] Endpoint documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del campo esDePago
  - Ejemplo de respuesta exitosa

### 🔐 Manejo de Errores
- [ ] Se devuelve HTTP 500 si hay error en la base de datos.
- [ ] El campo mensaje incluye texto claro y descriptivo.

---
