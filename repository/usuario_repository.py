from domain.usuario import Usuario
from typing import Optional

class UsuarioRepository:

    def __init__(self):
        self._datos: list[Usuario] = []
        self.tokens_invalidados: set = set()
        self._seed()

    def _seed(self):
        self._datos = [
            Usuario(1, "Juan Pérez",  "juan@email.com",  "Juan2024",  "Gratis"),
            Usuario(2, "María López", "maria@email.com", "Maria2024", "Plus"),
        ]

    def buscar_por_email(self, email: str) -> Optional[Usuario]:
        return next(
            (u for u in self._datos if u.email == email.lower()),
            None
        )

    def invalidar_token(self, token: str) -> bool:
        self.tokens_invalidados.add(token)
        return True

    def token_es_valido(self, token: str) -> bool:
        return token not in self.tokens_invalidados

usuario_repository = UsuarioRepository()