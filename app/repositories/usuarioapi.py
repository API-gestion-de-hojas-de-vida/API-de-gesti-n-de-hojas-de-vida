# app/repositories/usuarioapi.py
from abc import ABC, abstractmethod
from typing import Optional
from app.domain.usuarioapi import Usuario

class IUsuarioRepository(ABC):
    @abstractmethod
    def obtener_por_email(self, email: str) -> Optional[Usuario]:
        raise NotImplementedError
    @abstractmethod
    def crear(self, nombre: str, email: str, contrasena_hash: str, rol: str) -> Usuario:
        raise NotImplementedError

class UsuarioRepositoryMemoria(IUsuarioRepository):
    def __init__(self) -> None:
        self._almacen: dict[str, Usuario] = {}
        self._por_id: dict[int, Usuario] = {}
        self._contador: int = 0
        self._precargar_usuarios()

    def _precargar_usuarios(self):
        u1 = Usuario(id=1, nombre='Usuario Gratis', email='gratis@test.com', contrasena_hash='', rol='Gratis')
        u2 = Usuario(id=2, nombre='Usuario Plus', email='plus@test.com', contrasena_hash='', rol='Plus')
        self._almacen['gratis@test.com'] = u1
        self._almacen['plus@test.com'] = u2
        self._por_id[1] = u1
        self._por_id[2] = u2
        self._contador = 2

    def obtener_por_email(self, email: str) -> Optional[Usuario]:
        return self._almacen.get(email)

    def obtener_por_id(self, user_id: int) -> Optional[Usuario]:
        return self._por_id.get(user_id)

    def crear(self, nombre: str, email: str, contrasena_hash: str, rol: str) -> Usuario:
        self._contador += 1
        usuario = Usuario(id=self._contador, nombre=nombre, email=email, contrasena_hash=contrasena_hash, rol=rol)
        self._almacen[email] = usuario
        self._por_id[self._contador] = usuario
        return usuario

    def actualizar_usuario(self, usuario: Usuario) -> None:
        self._almacen[usuario.email] = usuario
        self._por_id[usuario.id] = usuario
