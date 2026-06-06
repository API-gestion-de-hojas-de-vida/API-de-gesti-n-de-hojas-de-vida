# app/repositories/usuarioapi.py

from abc import ABC, abstractmethod
from typing import Optional

from app.domain.usuarioapi import Usuario


# ─── Interfaz (Contrato) ──────────────────────────────────────────────────────

class IUsuarioRepository(ABC):

    @abstractmethod
    def obtener_por_email(self, email: str) -> Optional[Usuario]:
        raise NotImplementedError

    @abstractmethod
    def crear(self, nombre: str, email: str, contrasena_hash: str, rol: str) -> Usuario:
        raise NotImplementedError


# ─── Implementación en memoria (para desarrollo y pruebas) ───────────────────

class UsuarioRepositoryMemoria(IUsuarioRepository):

    def __init__(self) -> None:
        self._almacen: dict[str, Usuario] = {}
        self._contador: int = 0

    def obtener_por_email(self, email: str) -> Optional[Usuario]:
        return self._almacen.get(email)

    def crear(self, nombre: str, email: str, contrasena_hash: str, rol: str) -> Usuario:
        self._contador += 1
        usuario = Usuario(
            id=self._contador,
            nombre=nombre,
            email=email,
            contrasena_hash=contrasena_hash,
            rol=rol,
        )
        self._almacen[email] = usuario
        return usuario