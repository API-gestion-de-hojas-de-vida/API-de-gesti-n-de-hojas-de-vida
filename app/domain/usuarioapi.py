# app/domain/usuarioapi.py
from dataclasses import dataclass

@dataclass
class Usuario:
    id: int
    nombre: str
    email: str
    contrasena_hash: str
    rol: str