from domain.plantilla import Plantilla

class PlantillaService:
    def __init__(self, repo):
        self.repo = repo

    def obtener_preview(self, plantilla_id: int):
        plantilla = self.repo.buscar_por_id(plantilla_id)
        
        if not plantilla:
            return {
                "status_code": 404,
                "response": {
                    "message": "Plantilla no encontrada",
                    "data": None,
                    "success": False
                }
            }
        
        if hasattr(plantilla, "esta_activa") and not plantilla.esta_activa():
            return {
                "status_code": 404,
                "response": {
                    "message": "Plantilla no disponible",
                    "data": None,
                    "success": False
                }
            }
            
        preview_data = {
            "id": plantilla.id,
            "nombre": plantilla.nombre,
            "categoria": getattr(plantilla, "categoria", "Gratis"),
            "secciones": getattr(plantilla, "secciones", ["Perfil", "Experiencia", "Educación"]),
            "datosEjemplo": {
                "nombre": "Juan Pérez",
                "cargo": "Desarrollador Backend",
                "experiencia": "3 años"
            }
        }
        
        return {
            "status_code": 200,
            "response": {
                "message": "Plantilla obtenida exitosamente",
                "data": preview_data,
                "success": True
            }
        }
