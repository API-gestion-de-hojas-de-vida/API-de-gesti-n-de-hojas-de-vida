# HU-02: Autenticación de Usuario

**Como** usuario registrado en el sistema
**Quiero** iniciar sesión utilizando mi correo electrónico y contraseña, y que el sistema valide mis credenciales antes de permitirme el acceso
**Para** acceder de forma segura a mi cuenta y gestionar mis hojas de vida sin que terceros puedan ver o modificar mi información


## 🔁 Flujo Esperado

- El usuario ingresa su correo electrónico y contraseña.
- El sistema valida que el correo exista en la base de datos.
- El sistema valida que la contraseña coincida con la registrada.
- El sistema genera una sesión o token válido.
- El sistema retorna confirmación de inicio de sesión exitoso.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] Se expone un endpoint POST para el inicio de sesión.
- [ ] Se valida que el correo exista en el sistema.
- [ ] Se valida que la contraseña sea correcta.

### 2. 📆 Estructura de la información
- [ ] Se responde con la siguiente estructura en JSON:

```json
{
  "mensaje": "Inicio de sesión exitoso",
  "data": {
    "id": 1,
    "nombre": "Juan Pérez",
    "email": "juan@email.com",
    "token": "eyJhbGciOiJIUzI1NiJ9..."
  },
  "success": true
}
```

- [ ] Si las credenciales son incorrectas, el sistema retorna:

```json
{
  "mensaje": "Correo o contraseña incorrectos",
  "data": null,
  "success": false
}
```

## 🔧 Notas Técnicas

### 🚀 Endpoint – Inicio de Sesión
- **Método HTTP:** `POST`
- **Ruta:** `/api/v1/usuarios/login`

## 🧪 Requisitos de Pruebas

### ✅ Caso 1: Inicio de sesión exitoso
- **Precondición:** El usuario existe y la contraseña es correcta.
- **Acción:** Ejecutar POST /api/v1/usuarios/login con credenciales válidas.
- **Resultado esperado:**
  - Código HTTP 200 OK
  - Campo token generado correctamente
  - Campo success = true

### ✅ Caso 2: Correo no registrado
- **Precondición:** El correo no existe en la base de datos.
- **Acción:** Ejecutar POST con correo inexistente.
- **Resultado esperado:**
  - Código HTTP 404 Not Found
  - Campo mensaje = "Correo o contraseña incorrectos"
  - Campo success = false

### ❌ Caso 3: Contraseña incorrecta
- **Precondición:** El correo existe pero la contraseña no coincide.
- **Acción:** Ejecutar POST con contraseña incorrecta.
- **Resultado esperado:**
  - Código HTTP 401 Unauthorized
  - Campo mensaje = "Correo o contraseña incorrectos"
  - Campo success = false

### ❌ Caso 4: Campos vacíos
- **Precondición:** El usuario no completa todos los campos.
- **Acción:** Ejecutar POST con correo vacío.
- **Resultado esperado:**
  - Código HTTP 400 Bad Request
  - Campo mensaje = "Todos los campos son obligatorios"

## ✅ Definición de Hecho

### 📦 Alcance Funcional
- [ ] El endpoint valida correctamente las credenciales.
- [ ] Se genera token o sesión válida al autenticarse.
- [ ] Se bloquea el acceso con credenciales incorrectas.

### 🧪 Pruebas Completadas
- [ ] Se ejecutaron pruebas unitarias de validación.
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
- [ ] Se devuelve HTTP 401 si la contraseña es incorrecta.
- [ ] Se devuelve HTTP 404 si el correo no existe.
- [ ] Se devuelve HTTP 400 si los campos están vacíos.
