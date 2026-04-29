# [HU-02] Inicio de Sesión

## 📖 Historia de Usuario

Como usuario registrado
Quiero iniciar sesión de forma segura
Para que el sistema genere una sesión válida que me permita navegar por rutas protegidas

## 🔁 Flujo Esperado

- El usuario ingresa su correo electrónico y contraseña.
- El backend normaliza el correo a minúsculas y busca coincidencias exactas en la base de datos.
- Si el correo existe, el sistema compara la contraseña ingresada con el hash encriptado de la base de datos.
- Si coincide, el sistema genera un token de autenticación (ej. JWT) con un tiempo de expiración definido y los datos esenciales del usuario.
- El sistema retorna confirmación de inicio de sesión exitoso.

## ✅ Criterios de Aceptación

### 1. 🔍 Estructura y lógica del servicio
- [ ] La validación de credenciales debe ser estricta (case-sensitive para contraseña, case-insensitive para correo).
- [ ] Se valida que el correo exista en el sistema.
- [ ] Se valida que la contraseña sea correcta.
- [ ] Los mensajes de error nunca deben especificar si el fallo fue el correo o la contraseña para evitar enumeración de usuarios.
- [ ] El token generado debe incluir el id y rol del usuario en su payload para manejo de permisos.

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
