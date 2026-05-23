from domain.usuario import LoginRequest, LoginResponse
from repository.usuario_repository import UsuarioRepository

class UsuarioService:

    def __init__(self, repo: UsuarioRepository):
        self.repo = repo

    def login(self, datos: LoginRequest) -> LoginResponse:

        usuario = self.repo.buscar_por_email(datos.email)

        if not usuario:
            return LoginResponse(
                mensaje="Correo o contraseña incorrectos",
                data=None,
                success=False
            )

        if not usuario.verificar_password(datos.password):
            return LoginResponse(
                mensaje="Correo o contraseña incorrectos",
                data=None,
                success=False
            )

        return LoginResponse(
            mensaje="Inicio de sesión exitoso",
            data={
                **usuario.to_response(),
                "token": f"token-simulado-{usuario.id}-abc123"
            },
            success=True
        )

        def logout(self, token: str) -> LogoutResponse:
    from domain.usuario import LogoutResponse

    # CASO DE ERROR: token vacío
    if not token:
        return LogoutResponse(
            mensaje="El token no puede estar vacío",
            data=None,
            success=False
        )

    # CASO DE ERROR: token ya invalidado
    if not self.repo.token_es_valido(token):
        return LogoutResponse(
            mensaje="Sesión no válida o ya expirada",
            data=None,
            success=False
        )

    # ÉXITO: invalidar el token
    self.repo.invalidar_token(token)
    return LogoutResponse(
        mensaje="Sesión cerrada exitosamente",
        data=None,
        success=True
    )