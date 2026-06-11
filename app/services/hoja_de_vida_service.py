# app/services/hoja_de_vida_service.py
import datetime
from app.repositories.hoja_de_vida_repository import HojaDeVidaRepository
from app.repositories.plantilla_repository import PlantillaRepository


class NoEncontradoException(Exception):
    pass


class AccesoNoAutorizadoException(Exception):
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
        "descripcion": 500, "perfil": 500, "experiencia": 1000, "educacion": 800
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

    # HU-21: Exportación PDF
    def preparar_exportacion_pdf(self, id: int, usuario_id: int, plan_usuario: str, nombre_usuario: str):
        hv = self.repo_hv.obtener_por_id(id)
        if not hv or hv.usuario_id != usuario_id:
            raise NoEncontradoException("Hoja de vida no encontrada")

        if not hv.plantilla_id:
            raise ExportacionInvalidaException("Debe asignar una plantilla antes de exportar")

        if hv.estado != "finalizada":
            raise ExportacionInvalidaException("La hoja de vida debe estar finalizada para exportarse")

        plantilla = self.repo_plantilla.obtener_por_id(hv.plantilla_id)
        if not plantilla or not plantilla.activa:
            raise ExportacionInvalidaException(
                "La plantilla asignada ya no está activa. Por favor seleccione una nueva plantilla antes de exportar"
            )

        if plan_usuario.lower() == "gratis":
            contador = self.repo_hv.obtener_exportaciones_mensuales(usuario_id)
            if contador >= 3:
                raise ExportacionInvalidaException("Ha superado el límite de exportaciones mensuales para el plan Gratis")

        self.repo_hv.registrar_auditoria(usuario_id, id)

        fecha_actual = datetime.date.today().strftime("%Y-%m-%d")
        nombre_archivo = f"{nombre_usuario.replace(' ', '_')}-HV-{fecha_actual}.pdf"

        pdf_metadata_simulado = (
            f"%PDF-1.4\n"
            f"%Metadata: Author={nombre_usuario}, Created={fecha_actual}, Title=Hoja de Vida de {nombre_usuario}\n"
            f"Content: Diseno={plantilla.nombre}, Categoria={plantilla.categoria}, Datos={hv.datos}\n"
        ).encode("utf-8")

        return pdf_metadata_simulado, nombre_archivo

    # HU-22: Abrir hoja de vida en modo edición
    def abrir_modo_edicion(self, id: int, usuario_id: int) -> dict:
        hv = self.repo_hv.obtener_por_id(id)

        if not hv:
            raise NoEncontradoException("Hoja de vida no encontrada")

        if hv.usuario_id != usuario_id:
            raise AccesoNoAutorizadoException("No tienes permiso para editar esta hoja de vida")

        # Si está finalizada, volver a borrador
        if hv.estado == "finalizada":
            hv.estado = "borrador"

        # Verificar plantilla
        plantilla_info = None
        advertencia_plantilla = None
        if hv.plantilla_id:
            plantilla = self.repo_plantilla.obtener_por_id(hv.plantilla_id)
            if plantilla:
                plantilla_info = {"id": plantilla.id, "nombre": plantilla.nombre}
                if not plantilla.activa:
                    advertencia_plantilla = "La plantilla asignada fue desactivada. Selecciona una nueva antes de finalizar."
            
        return {
            "id": hv.id,
            "estado": hv.estado,
            "plantilla": plantilla_info,
            "advertencia_plantilla": advertencia_plantilla,
            "perfil": hv.datos.get("perfil"),
            "experiencia": hv.datos.get("experiencia", []),
            "educacion": hv.datos.get("educacion", []),
            "habilidades": hv.datos.get("habilidades")
        }
    # HU-23: eliminar hoja de vida
    def eliminar_hoja_de_vida(self, id: int, usuario_id: int) -> dict:
        hv = self.repo_hv.obtener_por_id(id)

        if not hv:
            raise NoEncontradoException("Hoja de vida no encontrada")

        if hv.usuario_id != usuario_id:
            raise AccesoNoAutorizadoException("No tienes permiso para eliminar esta hoja de vida")

        # Registrar auditoría antes de eliminar
        self.repo_hv.registrar_auditoria(usuario_id, id, accion="ELIMINAR_HV")

        # Eliminar en cascada
        self.repo_hv.eliminar(id)

        return {
            "message": "Hoja de vida eliminada exitosamente",
            "data": None,
            "success": True
        }