
# [HU-08] Reporte de Uso de Plantillas

## 📖 Historia de Usuario

Como administrador
Quiero visualizar un reporte de cuántas veces se ha usado cada plantilla por parte de los visitantes registrados o no registrados
Para identificar cuáles son los diseños más exitosos

## 🔁 Flujo Esperado

- El administrador solicita el reporte de uso de plantillas.
- El backend realiza una consulta agregada (GROUP BY, COUNT) cruzando la tabla de plantillas con la tabla de hojas de vida.
- El resultado se ordena de manera descendente (ORDER BY count DESC).
- Se empaqueta la lista y se envía al frontend.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] Se expone un endpoint GET para obtener el reporte.
- [ ] El reporte incluye todas las plantillas activas e inactivas.
- [ ] Si una plantilla tiene 0 usos, debe aparecer en la lista con valor 0, no omitirse.

### 2. 📆 Estructura de la información
- [ ] Se responde con la siguiente estructura en JSON:

```json
{
  "mensaje": "Reporte generado exitosamente",
  "data": [
    { "id": 1, "nombre": "Plantilla Moderna", "vecesUsada": 150 },
    { "id": 2, "nombre": "Plantilla Clásica", "vecesUsada": 80 }
  ],
  "success": true
}
```

## 🔧 Notas Técnicas

### 🚀 Endpoint – Reporte de Uso
- **Método HTTP:** `GET`
- **Ruta:** `/api/v1/plantillas/reporte-uso`

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Reporte exitoso
- **Precondición:** Existen plantillas con registros de uso.
- **Acción:** Ejecutar GET /api/v1/plantillas/reporte-uso.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Lista ordenada de mayor a menor uso
  - Campo success = true

### ✅ Caso 2: Sin registros de uso
- **Precondición:** No hay hojas de vida creadas aún.
- **Acción:** Ejecutar GET sin datos de uso.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Lista vacía
  - Campo success = true

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] El endpoint retorna el reporte correctamente ordenado.
- [ ] Se incluyen plantillas activas e inactivas.
- [ ] El conteo de uso es exacto.

### 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias del conteo.
- [ ] Se cubrieron los casos de lista vacía.
- [ ] Las pruebas funcionales están documentadas y pasadas.

### 📄 Documentación Técnica
- [ ] Endpoint documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint
  - Campos de salida
  - Ejemplo de respuesta exitosa

### 🔐 Manejo de Errores
- [ ] Se devuelve HTTP 500 si hay error en la base de datos.
- [ ] El campo mensaje incluye texto claro y descriptivo.
