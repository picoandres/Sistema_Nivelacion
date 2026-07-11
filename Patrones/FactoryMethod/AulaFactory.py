from Modelos.AulaVirtual import AulaVirtual
from Modelos.AulaFisica import AulaFisica

class AulaFactory:
    capacidad_maxima = 40

    @classmethod
    def crear_aula_virtual(cls, id_aula, nombre, plataforma, enlace):
        return AulaVirtual(
            id_aula=id_aula,
            nombre=nombre,
            capacidad=cls.capacidad_maxima,
            modalidad="virtual",
            tipo="virtual",
            estado=True,
            plataforma=plataforma,
            enlace=enlace
        )

    @classmethod
    def crear_aula_fisica(cls, id_aula, nombre, capacidad, tipo, ubicacion, bloque):
        return AulaFisica(
            id_aula=id_aula,
            nombre=nombre,
            capacidad=capacidad,
            tipo=tipo,
            estado=True,
            ubicacion=ubicacion,
            bloque=bloque
        )