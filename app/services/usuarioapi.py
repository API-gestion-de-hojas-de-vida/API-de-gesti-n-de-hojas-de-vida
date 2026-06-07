# app/services/usuarioapi.py
import re
import bcrypt
from jose import jwt, JWTError
from datetime import datetime, timedelta
from app.domain.usuarioapi import Usuario
from app.repositories.usuarioapi import IUsuarioRepository

# ─── Excepciones de dominio ──────────────────────────────────────────────────
class EmailDuplicadoError(Exception):
    pass

class ContrasenaInvalidaError(Exception):
    pass

class CredencialesInvalidasError(Exception):
    pass

class CorreoNoRegistradoError(Exception):
    pass

class CamposObligatoriosError(Exception):
    pass

class TokenInvalidoError(Exception):
    pass

# ─── Configuración JWT ───────────────────────────────────────────────────────
SECRET_KEY = "clave_secreta_proyecto"
ALGORITHM = "HS256"
EXPIRACION_MINUTOS = 60

# ─── Lista negra de tokens ───────────────────────────────────────────────────
_tokens_invalidados: set = set()

# ─── Servicio ────────────────────────────────────────────────────────────────
class UsuarioService:
    ROL_DEFECTO = "Gratis"
    _PATRON_CONTRASENA = re.compile(r"^(?=.*[A-Z])(?=.*\d).{8,}$")

    def __init__(self, repositorio: IUsuarioRepository) -> None:
        self._repo = repositorio

    def registrar_usuario(self, nombre: str, email: str, contrasena: str) -> Usuario:
        if not nombre or not email or not contrasena:
            raise CamposObligatoriosError()
        self._validar_contrasena(contrasena)
        self._verificar_email_unico(email.lower())
        contrasena_hash = bcrypt.hashpw(
            contrasena.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")
        return self._repo.crear(
            nombre=nombre,
            email=email.lower(),
            contrasena_hash=contrasena_hash,
            rol=self.ROL_DEFECTO,
        )

    def iniciar_sesion(self, email: str, contrasena: str) -> dict:
        if not email or not contrasena:
            raise CamposObligatoriosError()
        usuario = self._repo.obtener_por_email(email.lower())
        if usuario is None:
            raise CorreoNoRegistradoError()
        if not bcrypt.checkpw(contrasena.encode("utf-8"), usuario.contrasena_hash.encode("utf-8")):
            raise CredencialesInvalidasError()
        token = self._generar_token(usuario)
        return {
            "id": usuario.id,
            "nombre": usuario.nombre,
            "email": usuario.email,
            "token": token,
        }

    def cerrar_sesion(self, token: str) -> None:
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        except JWTError:
            raise TokenInvalidoError()
        if token in _tokens_invalidados:
            raise TokenInvalidoError()
        _tokens_invalidados.add(token)

    def _generar_token(self, usuario: Usuario) -> str:
        payload = {
            "sub": str(usuario.id),
            "rol": usuario.rol,
            "exp": datetime.utcnow() + timedelta(minutes=EXPIRACION_MINUTOS),
        }
        return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

    def _validar_contrasena(self, contrasena: str) -> None:
        if not self._PATRON_CONTRASENA.match(contrasena):
            raise ContrasenaInvalidaError(
                "La contraseña debe tener mínimo 8 caracteres, una mayúscula y un número"
            )

    def _verificar_email_unico(self, email: str) -> None:
        if self._repo.obtener_por_email(email) is not None:
            raise EmailDuplicadoError("El correo ya está registrado")