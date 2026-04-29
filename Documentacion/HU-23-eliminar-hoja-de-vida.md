# [HU-23] Eliminar Hoja de Vida

## 📖 Historia de Usuario

Como usuario
Quiero poder eliminar definitivamente una de mis hojas de vida
Para ejecutar el borrado en cascada de todos sus datos relacionados en la base de datos

## 🔁 Flujo Esperado

- El usuario autenticado accede al listado de sus hojas de vida y selecciona la opción eliminar.
- El sistema verifica que la hoja de vida pertenezca al usuario autenticado.
- El sistema verifica si existen enlaces de compartición activos asociados a la hoja de vida y advierte al usuario que estos también serán invalidados.
- El sistema verifica si la hoja de vida es la única que tiene el usuario y advierte al usuario antes de proceder.
- El sistema solicita confirmación explícita al usuario mediante un segundo paso antes de ejecutar la eliminación.
- El sistema invalida automáticamente todos los enlaces de compartición activos asociados a la hoja de vida.
- El sistema elimina en cascada todos los registros relacionados incluyendo bloques de experiencia, bloques de educación, habilidades, documentos PDF generados almacenados en servicios externos y enlaces de compartición.
- Si el PDF fue generado y almacenado en un servicio externo de almacenamiento, el sistema solicita su eliminación a ese servicio.
- El sistema registra la eliminación en un log de auditoría con fecha, hora, ID de usuario e ID de hoja de vida eliminada.
- El sistema retorna confirmación inmediata al usuario aunque la eliminación en cascada continúe procesándose en segundo plano.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio

- [ ] Se expone un endpoint DELETE para eliminar la hoja de vida.
- [ ] Se valida que la hoja de vida pertenezca al usuario autenticado antes de eliminar.
- [ ] Se requiere confirmación explícita del usuario antes de ejecutar la eliminación.
- [ ] Se invalidan automáticamente todos los enlaces de compartición activos antes de eliminar.
- [ ] Se elimina en cascada todos los registros relacionados: experiencia, educación, habilidades, documentos y enlaces.
- [ ] Si el PDF está almacenado en servicio externo, se solicita su eliminación a ese servicio.
- [ ] Se advierte al usuario si la hoja a eliminar es la única que tiene.
- [ ] Se advierte al usuario si existen enlaces de compartición activos que serán invalidados.
- [ ] Se registra la eliminación en log de auditoría con fecha, hora e ID de usuario.
- [ ] La eliminación es física y definitiva, no existe posibilidad de recuperación posterior.
- [ ] El sistema retorna confirmación inmediata sin tiempos de espera prolongados aunque el proceso en cascada continúe en segundo plano.
### 2. 📆 Estructura de la información
- [ ] Se responde con la siguiente estructura en JSON:
```
{
  "mensaje": "Hoja de vida eliminada exitosamente",
  "data": null,
  "success": true
}
- [ ] Si la hoja no pertenece al usuario, el sistema retorna:
{
  "mensaje": "No tienes permiso para eliminar esta hoja de vida",
  "data": null,
  "success": false
}
```

## 🔧 Notas Técnicas

### 🚀 Endpoint – Eliminar Hoja de Vida
- **Método HTTP:** DELETE
- **Ruta:** /api/v1/hojas-de-vida/{id}

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Eliminación exitosa
- **Precondición:** La hoja de vida existe y pertenece al usuario.
- **Acción:** Ejecutar DELETE /api/v1/hojas-de-vida/{id}.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Campo success = true
  - Todos los datos relacionados eliminados

### ❌ Caso 2: Hoja de vida de otro usuario
- **Precondición:** La hoja de vida pertenece a otro usuario.
- **Acción:** Ejecutar DELETE con ID de otra hoja de vida.
- **Resultado esperado:**
  - Código HTTP 403 Forbidden
  - Campo mensaje = "No tienes permiso para eliminar esta hoja de vida"

### ❌ Caso 3: Hoja de vida no encontrada
- **Precondición:** El ID no existe en la base de datos.
- **Acción:** Ejecutar DELETE con ID inexistente.
- **Resultado esperado:**
  - Código HTTP 404 Not Found
  - Campo mensaje = "Hoja de vida no encontrada"

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] El endpoint elimina correctamente la hoja de vida y sus datos relacionados.
- [ ] Se valida que la hoja pertenezca al usuario autenticado.
- [ ] El borrado en cascada funciona correctamente.

### 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias de eliminación en cascada.
- [ ] Se cubrieron los casos de acceso no autorizado.
- [ ] Las pruebas funcionales están documentadas y pasadas.

### 📄 Documentación Técnica
- [ ] Endpoint documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint
  - Datos eliminados en cascada
  - Ejemplo de respuesta exitosa
  - Ejemplo de error

### 🔐 Manejo de Errores
- [ ] Se devuelve HTTP 403 si la hoja no pertenece al usuario.
- [ ] Se devuelve HTTP 404 si la hoja no existe.
- [ ] El campo mensaje incluye texto claro y descriptivo.
