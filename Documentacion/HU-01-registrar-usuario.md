# [HU-01] Registro de Usuario

## 📖 Historia de Usuario

Como usuario nuevo
Quiero registrarme fácil y rapido en la plataforma ingresando mis datos básicos y contraseña
Para que el sistema me asigne automáticamente el rol "Gratis" y cree mi perfil

## 🔁 Flujo Esperado

- El usuario ingresa nombre completo, correo electrónico y contraseña.
- El frontend realiza una validación previa de formato y deshabilita el botón de envío para evitar peticiones duplicadas.
- El backend recibe el payload, elimina espacios en blanco al inicio y final (trim) y convierte el correo a minúsculas.
- El sistema consulta la base de datos para garantizar la unicidad del correo.
- El sistema valida que la contraseña tenga mínimo 8 caracteres, una mayúscula y un número.
- El sistema crea el perfil con rol "Gratis" automáticamente.
- El sistema retorna confirmación de registro exitoso.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] El campo email debe ser validado con formato estándar y guardado estrictamente en minúsculas.
- [ ] El sistema debe limpiar (trim) los espacios en el nombre y email.
- [ ] Se expone un endpoint POST para el registro.
- [ ] Se valida que el correo sea único en el sistema.
- [ ] Se valida formato y seguridad de la contraseña.

### 2. 📆 Estructura de la información
- [ ] Se responde con la siguiente estructura en JSON:

```json
{
  "mensaje": "Registro exitoso",
  "data": {
    "id": 1,
    "nombre": "Juan Pérez",
    "email": "juan@email.com",
    "rol": "Gratis"
  },
  "success": true
}
```

- [ ] Si el correo ya existe, el sistema retorna:

```json
{
  "mensaje": "El correo ya está registrado",
  "data": null,
  "success": false
}
```

## 🔧 Notas Técnicas

## 🚀 Endpoint – Registro de Usuario

- **Método HTTP:** `POST`
- **Ruta:** `/api/v1/usuarios/registro`

## 🧪 Requisitos de Pruebas

### 🔍 Casos de Prueba Funcional

### ✅ Caso 1: Registro exitoso
- **Precondición:** El correo no existe en la base de datos.
- **Acción:** Ejecutar POST /api/v1/usuarios/registro con datos válidos.
- **Resultado esperado:**
  - Código HTTP 201 Created
  - Campo rol = "Gratis"
  - Campo success = true

### ✅ Caso 2: Correo duplicado
- **Precondición:** El correo ya existe en la base de datos.
- **Acción:** Ejecutar POST con el mismo correo.
- **Resultado esperado:**
  - Código HTTP 409 Conflict
  - Campo mensaje = "El correo ya está registrado"
  - Campo success = false

### ❌ Caso 3: Contraseña inválida
- **Precondición:** El usuario envía una contraseña sin mayúscula o sin número.
- **Acción:** Ejecutar POST con contraseña "contraseña123".
- **Resultado esperado:**
  - Código HTTP 400 Bad Request
  - Campo mensaje = "La contraseña debe tener mínimo 8 caracteres, una mayúscula y un número"

### ❌ Caso 4: Campos vacíos
- **Precondición:** El usuario no completa todos los campos.
- **Acción:** Ejecutar POST con nombre vacío.
- **Resultado esperado:**
  - Código HTTP 400 Bad Request
  - Campo mensaje = "Todos los campos son obligatorios"

## ✅ Definición de Hecho

## 📦 Alcance Funcional
- [ ] El endpoint registra correctamente al usuario con rol "Gratis".
- [ ] Se valida unicidad del correo.
- [ ] Se valida seguridad de la contraseña.

## 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias de validación.
- [ ] Se cubrieron los casos de error.
- [ ] Las pruebas funcionales están documentadas y pasadas.

## 📄 Documentación Técnica
- [ ] Endpoint documentado en Swagger / OpenAPI.
- [ ] Se describe:
  - Propósito del endpoint
  - Campos de entrada y salida
  - Ejemplo de respuesta exitosa
  - Ejemplo de error

## 🔐 Manejo de Errores
- [ ] Se devuelve HTTP 409 si el correo ya existe.
- [ ] Se devuelve HTTP 400 si los campos no cumplen las validaciones.
- [ ] El campo mensaje incluye texto claro y descriptivo.

