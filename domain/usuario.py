from pydantic import BaseModel, field_validator

class LoginRequest(BaseModel):
    email: str
    password: str

    @field_validator("email")
    @classmethod
    def email_valido(cls, v):
        if not v or "@" not in v:
            raise ValueError("El correo no tiene un formato válido")
        return v.lower().strip()

    @field_validator("password")
    @classmethod
    def password_valido(cls, v):
        if len(v) < 8:
            raise ValueError("La contraseña debe tener mínimo 8 caracteres")
        return v

class LoginResponse(BaseModel):
    mensaje: str
    data: dict | None
    success: bool

class Usuario:
    def __init__(self, id: int, nombre: str, email: str,
                 password: str, rol: str):
        self.id       = id
        self.nombre   = nombre
        self.email    = email
        self.password = password
        self.rol      = rol

    def verificar_password(self, password: str) -> bool:
        return self.password == password

    def to_response(self) -> dict:
        return {
            "id":     self.id,
            "nombre": self.nombre,
            "email":  self.email,
            "rol":    self.rol,
        }

        class LogoutRequest(BaseModel):
    token: str

class LogoutResponse(BaseModel):
    mensaje: str
    data: dict | None
    success: bool