# [HU-13] Búsqueda de Plantillas por Palabra Clave

## 📖 Historia de Usuario

Como usuario
Quiero poder buscar plantillas por palabras clave
Para encontrar rápidamente un estilo acorde a mi profesión

🔁 Flujo Esperado

* El usuario ingresa una palabra clave en el buscador.
* El sistema valida que la palabra clave no esté vacía ni compuesta únicamente por espacios.
* El sistema normaliza el término de búsqueda (eliminando espacios innecesarios y aplicando formato consistente).
* El sistema consulta la base de datos filtrando por coincidencia parcial en nombre o descripción.
* El sistema aplica un límite de resultados para optimizar la respuesta.
* El sistema retorna las plantillas activas que coincidan con la búsqueda.

✅ Criterios de Aceptación

1. 🔍 Estructura y lógica del servicio

* Se expone un endpoint GET con parámetro de búsqueda.
* La búsqueda aplica sobre el nombre y descripción de la plantilla.
* La búsqueda es insensible a mayúsculas y minúsculas.
* Se permiten coincidencias parciales del término ingresado.
* Solo se retornan plantillas activas.
* Se valida que el parámetro de búsqueda no esté vacío antes de ejecutar la consulta.

1. 📆 Estructura de la información

* Se responde con la siguiente estructura en JSON:
```json
    { “mensaje”: “Búsqueda realizada exitosamente”,
 “data”:
[ { “id”: 1,
“nombre”: “Plantilla Moderna”,
 “categoria”: “Gratis” },
 { “id”: 4, “nombre”:
“Plantilla Moderna Pro”,
 “categoria”: “Pro” } ],
 “success”: true }
```
* El campo data siempre retorna una lista (vacía o con resultados).
* Los resultados pueden venir ordenados por nombre o relevancia.
* Si no hay resultados, el sistema retorna:
    { “mensaje”: “No se encontraron plantillas con ese término”, “data”: [], “success”: true }

## 🔧 Notas Técnicas

### 🚀 Endpoint – Búsqueda de Plantillas
- **Método HTTP:** GET
- **Ruta:** /api/v1/plantillas?buscar=moderna

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Búsqueda exitosa
- **Precondición:** Existen plantillas cuyo nombre contiene la palabra clave.
- **Acción:** Ejecutar GET con buscar=moderna.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Lista de plantillas que coinciden
  - Campo success = true

### ✅ Caso 2: Sin resultados
- **Precondición:** Ninguna plantilla coincide con la palabra clave.
- **Acción:** Ejecutar GET con buscar=xyz123.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Lista vacía
  - Campo success = true

### ❌ Caso 3: Búsqueda vacía
- **Precondición:** El usuario no ingresa ninguna palabra clave.
- **Acción:** Ejecutar GET con buscar vacío.
- **Resultado esperado:**
  - Código HTTP 400 Bad Request
  - Campo mensaje = "El término de búsqueda no puede estar vacío"

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] El endpoint busca correctamente por nombre y descripción.
- [ ] Solo se incluyen plantillas activas.
- [ ] Se maneja correctamente el caso sin resultados.

### 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias de búsqueda.
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
- [ ] Se devuelve HTTP 400 si el término está vacío.
- [ ] Se devuelve HTTP 500 si hay error en la base de datos.
- [ ] El campo mensaje incluye texto claro y descriptivo.
