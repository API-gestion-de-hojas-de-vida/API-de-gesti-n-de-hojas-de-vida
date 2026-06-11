# app/repositories/plantilla_repository.py
<<<<<<< HEAD
from app.domain.plantilla import Plantilla
from typing import Optional, List
# app/repositories/plantilla_repository.py
=======
>>>>>>> origin/development
from app.domain.plantilla import Plantilla
from typing import Optional, List

class PlantillaRepository:
    def __init__(self):
        self._datos: List[Plantilla] = []
        self._siguiente_id: int = 1

    def obtener_todos(self) -> List[Plantilla]:
        return self._datos

    def obtener_por_nombre(self, nombre: str) -> Optional[Plantilla]:
        nombre_limpio = " ".join(nombre.strip().split()).lower()
        for p in self._datos:
            p_limpio = " ".join(p.nombre.strip().split()).lower()
            if p_limpio == nombre_limpio:
                return p
        return None

    def crear(self, nombre: str, secciones: List[str], categoria: str) -> Plantilla:
        nueva = Plantilla(
            id=self._siguiente_id,
            nombre=nombre,
            secciones=secciones,
            categoria=categoria
        )
        self._datos.append(nueva)
        self._siguiente_id += 1
        return nueva
    
    def obtener_por_id(self, id: int) -> Optional[Plantilla]:
        for p in self._datos:
            if p.id == id:
                return p
        return None

    def actualizar_campos(self, id: int, campos: List[str]) -> Plantilla:
        plantilla = self.obtener_por_id(id)
        if plantilla:
            plantilla.campos_obligatorios = campos
        return plantilla

    def actualizar_categoria(self, id: int, nueva_categoria: str):
        plantilla = self.obtener_por_id(id)
        if plantilla:
            plantilla.categoria = nueva_categoria
        return plantilla

    def desactivar_logico(self, id: int):
        plantilla = self.obtener_por_id(id)
        if plantilla:
            plantilla.activa = False
        return plantilla

    def obtener_paginadas(self, page: int, size: int, categoria: str = None, buscar: str = None):
        # Filtrar solo las activas
        activas = [p for p in self._datos if p.activa]
        
        # Filtro de categoría
        if categoria:
            activas = [p for p in activas if p.categoria == categoria]

        # Búsqueda por coincidencia parcial en nombre
        if buscar:
            termino = buscar.strip().lower()
            activas = [p for p in activas if termino in p.nombre.lower()]
            
        total_activas = len(activas)

        # Paginación
        inicio = (page - 1) * size
        fin = inicio + size

        return total_activas, activas[inicio:fin]

plantilla_repository = PlantillaRepository()
class PlantillaRepository:
    def __init__(self):
        self._datos: List[Plantilla] = []
        self._siguiente_id: int = 1

    def obtener_todos(self) -> List[Plantilla]:
        return self._datos

    def obtener_por_nombre(self, nombre: str) -> Optional[Plantilla]:
        nombre_limpio = " ".join(nombre.strip().split()).lower()
        for p in self._datos:
            p_limpio = " ".join(p.nombre.strip().split()).lower()
            if p_limpio == nombre_limpio:
                return p
        return None

    def crear(self, nombre: str, secciones: List[str], categoria: str) -> Plantilla:
        nueva = Plantilla(
            id=self._siguiente_id,
            nombre=nombre,
            secciones=secciones,
            categoria=categoria
        )
        setattr(nueva, "activo", True)
        self._datos.append(nueva)
        self._siguiente_id += 1
        return nueva

    def obtener_por_id(self, id: int) -> Optional[Plantilla]:
        for p in self._datos:
            if p.id == id:
                return p
        return None

    def actualizar_campos(self, id: int, campos: List[str]) -> Plantilla:
        plantilla = self.obtener_por_id(id)
        if plantilla:
            plantilla.campos_obligatorios = campos
        return plantilla

    def actualizar_categoria(self, id: int, categoria: str) -> Plantilla:
        plantilla = self.obtener_por_id(id)
        if plantilla:
            plantilla.categoria = categoria
        return plantilla

    def desactivar_logico(self, id: int) -> Optional[Plantilla]:
        plantilla = self.obtener_por_id(id)
        if plantilla:
            plantilla.activa = False
        return plantilla

    def actualizar_categoria(self, id: int, nueva_categoria: str) -> Plantilla:
        plantilla = self.obtener_por_id(id)
        if plantilla:
            plantilla.categoria = nueva_categoria
        return plantilla

    def obtener_paginadas(self, page: int, size: int, categoria: str = None, buscar: str = None):
        # 1. Filtrar solo las activas
        activas = [p for p in self._datos if p.activa]
        
        # 2. HU-10: Filtro de categoría
        if categoria:
            activas = [p for p in activas if p.categoria == categoria]

        # 3. HU-13: Búsqueda por coincidencia parcial en nombre
        if buscar:
            termino = buscar.strip().lower()
            activas = [p for p in activas if termino in p.nombre.lower()]
            
        total_activas = len(activas)

        # 4. HU-09: Paginación
        inicio = (page - 1) * size
        fin = inicio + size

        return total_activas, activas[inicio:fin]

    # ==========================================
    # HU-11: OBTENER ACTIVAS
    # ==========================================
    def obtener_activas(self):
        return [p for p in self._datos if p.activa]
    # ==========================================
    # HU-13: BUSQUEDA POR PALABRA CLAVE
    # ==========================================
    def buscar(self, termino: str) -> List[Plantilla]:
        termino_limpio = termino.strip().lower()
        return [p for p in self._datos if p.activa and termino_limpio in p.nombre.lower()]
plantilla_repository = PlantillaRepository()
