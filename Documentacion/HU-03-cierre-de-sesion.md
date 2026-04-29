# [HU-03] Cierre de Sesión

## 📖 Historia de Usuario

Como usuario autenticado
Quiero poder cerrar mi sesión
Para que el sistema destruya mis credenciales temporales y nadie más pueda acceder a mi perfil desde ese dispositivo

## 🔁 Flujo Esperado

- El usuario hace clic en "Cerrar sesión".
- El frontend elimina el token de su almacenamiento local (Local Storage o Cookies).
- Se envía una petición al backend con el token actual.
- El backend registra el token en una "lista negra" o invalida la sesión activa en la base de datos.
- El usuario es redirigido a la página de inicio.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] Se expone un endpoint POST para el cierre de sesión.
- [ ] Se invalida el token o sesión activa del usuario.
- [ ] Se eliminan las credenciales temporales del dispositivo.
- [ ] Un token invalidado no debe permitir acceso a ninguna ruta protegida, incluso si no ha expirado por tiempo.

### 2. 📆 Estructura de la información
- [ ] Se responde con la siguiente estructura en JSON:

```json
{
  "mensaje": "Sesión cerrada exitosamente",
  "data": null,
  "success": true
}
```

## 🔧 Notas Técnicas

### 🚀 Endpoint – Cierre de Sesión
- **Método HTTP:** `POST`
- **Ruta:** `/api/v1/usuarios/logout`

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Cierre de sesión exitoso
- **Precondición:** El usuario tiene una sesión activa.
- **Acción:** Ejecutar POST /api/v1/usuarios/logout con token válido.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Campo mensaje = "Sesión cerrada exitosamente"
  - Campo success = true

### ❌ Caso 2: Token inválido o expirado
- **Precondición:** El usuario envía un token inválido o ya expirado.
- **Acción:** Ejecutar POST con token inválido.
- **Resultado esperado:**
  - Código HTTP 401 Unauthorized
  - Campo mensaje = "Sesión no válida o ya expirada"
  - Campo success = false

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] El endpoint invalida correctamente el token o sesión activa.
- [ ] Las credenciales temporales son eliminadas del dispositivo.
- [ ] El acceso queda bloqueado tras cerrar sesión.

### 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias de invalidación de token.
- [ ] Se cubrieron los casos de error.
- [ ] Las pruebas funcionales están documentadas y pasadas.

### 📄 Documentación Técnica
- [ ] Endpoint documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint
  - Campos de entrada y salida
  - Ejemplo de respuesta exitosa
  - Ejemplo de error

### 🔐 Manejo de Errores
- [ ] Se devuelve HTTP 401 si el token es inválido o expirado.
- [ ] El campo mensaje incluye texto claro y descriptivo.


