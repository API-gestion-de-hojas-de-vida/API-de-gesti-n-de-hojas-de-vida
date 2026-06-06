from domain.usuario import LoginRequest, LoginResponse, LogoutRequest, LogoutResponse

class UsuarioService:
    def __init__(self):
        # Simulación de usuarios registrados en el sistema
        self._usuarios_validos = {
            "admin@correo.com": "123456",
            "user@correo.com": "password123"
        }

    def login(self, datos: LoginRequest) -> LoginResponse:
        try:
            email = datos.email
            password = datos.password

            if email in self._usuarios_validos and self._usuarios_validos[email] == password:
                return LoginResponse(
                    message="Inicio de sesión exitoso",
                    data={"email": email, "token": "simulated-jwt-token-xyz"},
                    success=True
                )
            
            return LoginResponse(
                message="Credenciales inválidas",
                data=None,
                success=False
            )
        except Exception:
            return LoginResponse(
                message="Error interno al iniciar sesión",
                data=None,
                success=False
            )

    def logout(self, datos: LogoutRequest) -> LogoutResponse:
        try:
            return LogoutResponse(
                message="Cierre de sesión exitoso",
                data={"email": datos.email},
                success=True
            )
        except Exception:
            return LogoutResponse(
                message="Error al cerrar sesión",
                data=None,
                success=False
            )

usuario_service = UsuarioService()