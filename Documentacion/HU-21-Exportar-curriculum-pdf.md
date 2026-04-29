# [HU-21] Exportar Hoja de Vida en PDF

## 📖 Historia de Usuario

Como usuario
Quiero presionar el botón "Exportar"
Para que el backend genere un archivo PDF descargable con mis datos y plantilla seleccionada

🔁 Flujo Esperado

* El usuario accede a su hoja de vida.
* El usuario selecciona el formato de descarga (PDF o Word).
* El frontend envía la solicitud al backend indicando el formato.
* El backend valida que la hoja de vida exista y pertenezca al usuario.
* El sistema valida que el formato solicitado sea permitido.
* El backend obtiene los datos y estructura de la plantilla.
* El sistema transforma la información al formato solicitado.
* El sistema genera el archivo correspondiente en memoria.
* El backend retorna el archivo listo para descarga.
* El frontend inicia la descarga automática.
* Si el formato no es válido, el sistema rechaza la solicitud.
* Si ocurre un error, se evita la descarga de archivos corruptos.

✅ Criterios de Aceptación

1. 🔍 Estructura y lógica del servicio

* Se expone un endpoint GET o POST para descarga.
* Se valida que el formato sea PDF o Word.
* Se valida que la hoja de vida exista y pertenezca al usuario.
* El sistema genera correctamente el archivo en el formato solicitado.
* Se garantiza consistencia entre formatos (misma información).

### 2. 📆 Estructura de la información

* Para PDF:
    * Content-Type: application/pdf
* Para Word:
    * Content-Type: application/vnd.openxmlformats-officedocument.wordprocessingml.document
* El nombre del archivo es consistente (ej: hoja_de_vida.pdf / .docx)
* En caso de error:
}
- [ ] Si no tiene plantilla asignada, el sistema retorna:
```
{
  "mensaje": "Debe asignar una plantilla antes de exportar",
  "data": null,
  "success": false
}
```


## 🔧 Notas Técnicas

### 🚀 Endpoint – Exportar PDF
- **Método HTTP:** GET
- **Ruta:** /api/v1/hojas-de-vida/{id}/exportar/pdf
- **Content-Type respuesta:** application/pdf

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Exportación exitosa
- **Precondición:** La hoja de vida está finalizada y tiene plantilla asignada.
- **Acción:** Ejecutar GET /api/v1/hojas-de-vida/{id}/exportar/pdf.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Archivo PDF generado correctamente
  - Content-Type = application/pdf

### ❌ Caso 2: Hoja de vida no finalizada
- **Precondición:** La hoja de vida está en estado borrador.
- **Acción:** Ejecutar GET para exportar.
- **Resultado esperado:**
  - Código HTTP 400 Bad Request
  - Campo mensaje = "La hoja de vida debe estar finalizada para exportarse"

### ❌ Caso 3: Sin plantilla asignada
- **Precondición:** La hoja de vida no tiene plantilla.
- **Acción:** Ejecutar GET para exportar.
- **Resultado esperado:**
  - Código HTTP 400 Bad Request
  - Campo mensaje = "Debe asignar una plantilla antes de exportar"

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] El endpoint genera correctamente el PDF.
- [ ] Se valida el estado de la hoja de vida antes de exportar.
- [ ] Se valida que tenga plantilla asignada.

### 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias de generación de PDF.
- [ ] Se cubrieron los casos de error.
- [ ] Las pruebas funcionales están documentadas y pasadas.

### 📄 Documentación Técnica
- [ ] Endpoint documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint
  - Formato de respuesta
  - Ejemplo de error

### 🔐 Manejo de Errores
- [ ] Se devuelve HTTP 400 si la hoja no está finalizada o no tiene plantilla.
- [ ] Se devuelve HTTP 500 si falla la generación del PDF.
- [ ] El campo mensaje incluye texto claro y descriptivo.
