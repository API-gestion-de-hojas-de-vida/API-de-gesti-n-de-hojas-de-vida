from pydantic import BaseModel, EmailStr
from typing import Optional

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    message: str
    data: Optional[dict] = None
    success: bool

class LogoutRequest(BaseModel):
    email: EmailStr

class LogoutResponse(BaseModel):
    message: str
    data: Optional[dict] = None
    success: bool

class Usuario:
    def __init__(self, id: int, nombre: str, email: str, password: str, rol: str):
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
    
    