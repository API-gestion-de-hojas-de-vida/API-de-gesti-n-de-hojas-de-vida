# app/services/hoja_de_vida_service.py
import datetime
from app.repositories.hoja_de_vida_repository import HojaDeVidaRepository
from app.repositories.plantilla_repository import PlantillaRepository

class NoEncontradoException(Exception):
    pass

class CamposFaltantesException(Exception):
    def __init__(self, faltantes: list):
        self.faltantes = faltantes
        super().__init__("Existen campos obligatorios sin completar")

class LongitudInvalidaException(Exception):
    def __init__(self, mensajes: list):
        super().__init__(", ".join(mensajes))

class ExportacionInvalidaException(Exception):
    pass


class HojaDeVidaService:
    LIMITES_LONGITUD = {
        "descripción": 500, "perfil": 500, "experiencia": 1000, "educación": 800
    }
    LIMITE_POR_DEFECTO = 255

    def __init__(self, repo_hv: HojaDeVidaRepository, repo_plantilla: PlantillaRepository):
        self.repo_hv = repo_hv
        self.repo_plantilla = repo_plantilla

    def guardar_secciones(self, id: int, secciones: dict):
        hv = self.repo_hv.obtener_por_id(id)
        if not hv:
            raise NoEncontradoException("Hoja de vida no encontrada")

        errores = []
        for campo, valor in secciones.items():
            limite = self.LIMITES_LONGITUD.get(campo.lower(), self.LIMITE_POR_DEFECTO)
            if len(valor) > limite:
                errores.append(f"El campo '{campo}' supera la longitud máxima permitida de {limite} caracteres")

        if errores:
            raise LongitudInvalidaException(errores)

        hv.datos.update(secciones)
        return hv

    def finalizar_hoja_de_vida(self, id: int):
        hv = self.repo_hv.obtener_por_id(id)
        if not hv:
            raise NoEncontradoException("Hoja de vida no encontrada")

        if not hv.plantilla_id:
            raise ExportacionInvalidaException("Debe asignar una plantilla antes de exportar")

        plantilla = self.repo_plantilla.obtener_por_id(hv.plantilla_id)
        if not plantilla:
            raise NoEncontradoException("Plantilla asociada no encontrada")

        campos_faltantes = []
        for campo in plantilla.campos_obligatorios:
            valor = hv.datos.get(campo)
            if not valor or (isinstance(valor, list) and len(valor) == 0):
                campos_faltantes.append(campo)

        if campos_faltantes:
            raise CamposFaltantesException(campos_faltantes)

        hv.estado = "finalizada"
        return hv

    # ==========================================
    # HU-21: LÓGICA DE EXPORTACIÓN PDF
    # ==========================================
    def preparar_exportacion_pdf(self, id: int, usuario_id: int, plan_usuario: str, nombre_usuario: str):
        # 1. Verificar existencia y pertenencia
        hv = self.repo_hv.obtener_por_id(id)
        if not hv or hv.usuario_id != usuario_id:
            raise NoEncontradoException("Hoja de vida no encontrada")

        # 2. Verificar si tiene plantilla asignada
        if not hv.plantilla_id:
            raise ExportacionInvalidaException("Debe asignar una plantilla antes de exportar")

        # 3. Verificar estado de finalización
        if hv.estado != "finalizada":
            raise ExportacionInvalidaException("La hoja de vida debe estar finalizada para exportarse")

        # 4. Verificar que la plantilla asociada siga activa
        plantilla = self.repo_plantilla.obtener_por_id(hv.plantilla_id)
        if not plantilla or not plantilla.activa:
            raise ExportacionInvalidaException(
                "La plantilla asignada ya no está activa. Por favor seleccione una nueva plantilla antes de exportar"
            )

        # 5. Aplicar límites comerciales para plan Gratis (Máximo 3 descargas simuladas al mes)
        if plan_usuario.lower() == "gratis":
            contador = self.repo_hv.obtener_exportaciones_mensuales(usuario_id)
            if contador >= 3:
                raise ExportacionInvalidaException("Ha superado el límite de exportaciones mensuales para el plan Gratis")

        # 6. Registrar auditoría en el log
        self.repo_hv.registrar_auditoria(usuario_id, id)

        # 7. Formatear nombre del archivo: NombreUsuario-HV-YYYY-MM-DD.pdf
        fecha_actual = datetime.date.today().strftime("%Y-%m-%d")
        nombre_archivo = f"{nombre_usuario.replace(' ', '_')}-HV-{fecha_actual}.pdf"

        # 8. Simulación técnica de generación de bytes del PDF con Metadata incrustada
        # En producción aquí se llamaría a ReportLab/WeasyPrint inyectando hv.datos y plantilla.categoria
        pdf_metadata_simulado = (
            f"%PDF-1.4\n"
            f"%Metadata: Author={nombre_usuario}, Created={fecha_actual}, Title=Hoja de Vida de {nombre_usuario}\n"
            f"Content: Diseno={plantilla.nombre}, Categoria={plantilla.categoria}, Datos={hv.datos}\n"
        ).encode("utf-8")

        return pdf_metadata_simulado, nombre_archivo
    
    # app/services/plantilla_service.py
# ... (dentro de tu clase PlantillaService) ...

    def obtener_catalogo(self, page: int, size: int, categoria: str = None, buscar: str = None):
        if page < 1 or size < 1:
            raise CamposInvalidosException("Los parámetros de paginación deben ser números positivos")

        if categoria and categoria not in ["Gratis", "Plus", "Pro"]:
            raise CamposInvalidosException("Categoría no válida. Debe ser Gratis, Plus o Pro")

        # Validación HU-13: Que no envíen espacios vacíos en la búsqueda
        if buscar is not None and len(buscar.strip()) == 0:
            raise CamposInvalidosException("El término de búsqueda no puede estar vacío")

        return self.repo.obtener_paginadas(page, size, categoria, buscar)