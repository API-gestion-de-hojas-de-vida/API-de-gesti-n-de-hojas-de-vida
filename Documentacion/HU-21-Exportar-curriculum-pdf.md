# [HU-21] Exportar Hoja de Vida en PDF

## 📖 Historia de Usuario

Como usuario
Quiero presionar el botón "Exportar"
Para que el backend genere un archivo PDF descargable con mis datos y plantilla seleccionada

## 🔁 Flujo Esperado

- El usuario autenticado accede a su hoja de vida y hace clic en "Exportar PDF".
- El sistema verifica que el usuario esté autenticado y que la hoja de vida le pertenezca.
- El sistema valida que la hoja de vida tenga estado "finalizada" antes de proceder.
- El sistema valida que la hoja de vida tenga una plantilla activa asignada.
- El sistema verifica si el usuario tiene los permisos de exportación según su plan, aplicando límites de exportaciones mensuales para usuarios Gratis.
- El sistema inicia la generación del PDF aplicando exactamente el diseño de la plantilla seleccionada incluyendo colores, tipografías, márgenes y distribución de secciones.
- El sistema maneja correctamente caracteres especiales, tildes, emojis y símbolos en el contenido del PDF.
- El sistema genera metadata del PDF incluyendo autor, fecha de creación y título del documento.
- El sistema nombra el archivo con el formato NombreUsuario-HV-YYYY-MM-DD.pdf.
- El PDF se retorna como stream de descarga directa con Content-Type application/pdf.
- El sistema registra la exportación en un log de auditoría con fecha, hora, ID de usuario e ID de hoja de vida.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio

- [ ] Se expone un endpoint GET para exportar la hoja de vida en PDF.
- [ ] Se valida que la hoja de vida pertenezca al usuario autenticado.
- [ ] Se valida que la hoja de vida tenga estado "finalizada".
- [ ] Se valida que la hoja de vida tenga una plantilla activa asignada.
- [ ] Se aplica límite de exportaciones mensuales para usuarios con plan Gratis.
- [ ] El PDF respeta exactamente el diseño de la plantilla incluyendo colores, tipografías y distribución.
- [ ] El PDF contiene texto seleccionable, no es una imagen escaneada.
- [ ] El PDF incluye metadata de autor, fecha de creación y título.
- [ ] El nombre del archivo sigue el formato NombreUsuario-HV-YYYY-MM-DD.pdf.
- [ ] La generación del PDF no supera los 5 segundos para una experiencia fluida.
- [ ] Se registra cada exportación en log de auditoría.
- [ ] Si la plantilla asignada fue desactivada después de finalizar la hoja de vida, el sistema notifica al usuario y le solicita seleccionar una nueva plantilla antes de exportar.
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
