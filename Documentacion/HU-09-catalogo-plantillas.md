# [HU-09] Catálogo de Plantillas Paginado

## 📖 Historia de Usuario

Como usuario
Quiero que los diseños me vayan apareciendo de a pocos, en páginas que carguen rápido
Para no abrumarme viendo cien opciones de golpe ni frustrarme porque mi celular o mi internet se quedan congelados

## 🔁 Flujo Esperado

- El frontend realiza un GET enviando page y size como Query Params.
- El backend recibe los parámetros, aplicando valores por defecto si no existen
- Se realiza la consulta en base de datos aplicando LIMIT y OFFSET.
- Paralelamente, se calcula el total de registros activos para la paginación del frontend.
- Se retorna el objeto de paginación estructurado.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] Se expone un endpoint GET con parámetros de paginación.
- [ ] Se valida que los parámetros page y size sean números positivos.
- [ ] Solo se retornan plantillas activas.

### 2. 📆 Estructura de la información
- [ ] Se responde con la siguiente estructura en JSON:

```json
{
  "mensaje": "Catálogo obtenido exitosamente",
  "data": {
    "pagina": 1,
    "tamano": 10,
    "total": 25,
    "plantillas": [
      { "id": 1, "nombre": "Plantilla Moderna", "categoria": "Gratis" },
      { "id": 2, "nombre": "Plantilla Clásica", "categoria": "Plus" }
    ]
  },
  "success": true
}
```

## 🔧 Notas Técnicas

### 🚀 Endpoint – Catálogo Paginado
- **Método HTTP:** `GET`
- **Ruta:** `/api/v1/plantillas?page=1&size=10`

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Catálogo exitoso
- **Precondición:** Existen plantillas activas en la base de datos.
- **Acción:** Ejecutar GET con page=1 y size=10.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Lista de máximo 10 plantillas
  - Campo success = true

### ✅ Caso 2: Página sin resultados
- **Precondición:** Se solicita una página que supera el total.
- **Acción:** Ejecutar GET con page=99.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Lista vacía
  - Campo success = true

### ❌ Caso 3: Parámetros inválidos
- **Precondición:** El usuario envía page=0 o size negativo.
- **Acción:** Ejecutar GET con page=0.
- **Resultado esperado:**
  - Código HTTP 400 Bad Request
  - Campo mensaje = "Los parámetros de paginación deben ser números positivos"

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] El endpoint retorna correctamente el catálogo paginado.
- [ ] Solo se incluyen plantillas activas.
- [ ] La paginación funciona correctamente.

### 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias de paginación.
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
- [ ] Se devuelve HTTP 400 si los parámetros son inválidos.
- [ ] Se devuelve HTTP 500 si hay error en la base de datos.
- [ ] El campo mensaje incluye texto claro y descriptivo.
