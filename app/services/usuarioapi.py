# app/services/usuarioapi.py

import re
import bcrypt

from app.domain.usuarioapi import Usuario
from app.repositories.usuarioapi import IUsuarioRepository


# ─── Excepciones de dominio ───────────────────────────────────────────────────

class EmailDuplicadoError(Exception):
    pass


class ContrasenaInvalidaError(Exception):
    pass


# ─── Servicio ─────────────────────────────────────────────────────────────────

class UsuarioService:

    ROL_DEFECTO = "Gratis"
    _PATRON_CONTRASENA = re.compile(r"^(?=.*[A-Z])(?=.*\d).{8,}$")

    def __init__(self, repositorio: IUsuarioRepository) -> None:
        self._repo = repositorio

    def registrar_usuario(self, nombre: str, email: str, contrasena: str) -> Usuario:
        self._validar_contrasena(contrasena)
        self._verificar_email_unico(email)

        contrasena_hash = bcrypt.hashpw(
            contrasena.encode("utf-8"),
            bcrypt.gensalt()
        ).decode("utf-8")

        return self._repo.crear(
            nombre=nombre,
            email=email,
            contrasena_hash=contrasena_hash,
            rol=self.ROL_DEFECTO,
        )

    def _validar_contrasena(self, contrasena: str) -> None:
        if not self._PATRON_CONTRASENA.match(contrasena):
            raise ContrasenaInvalidaError(
                "La contraseña debe tener mínimo 8 caracteres, una mayúscula y un número"
            )

    def _verificar_email_unico(self, email: str) -> None:
        if self._repo.obtener_por_email(email) is not None:
            raise EmailDuplicadoError("El correo ya está registrado")