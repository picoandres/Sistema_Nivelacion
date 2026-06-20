from abc import ABC, abstractmethod
from Horario import Horario

class HorarioCreador(ABC):
    @abstractmethod
    def crear_horario(self, dia: str, aula: str, asignador: str) -> Horario:
        pass

class HorarioMatutinoCreador(HorarioCreador):
    def crear_horario(self, dia: str, aula: str, asignador: str) -> Horario:
        return Horario(dia, "07:00", "13:00", aula)


class HorarioVespertinoCreador(HorarioCreador):
    def crear_horario(self, dia: str, aula: str) -> Horario:
        return Horario(dia, "13:00", "18:00", aula)


class HorarioNocturnoCreador(HorarioCreador):
    def crear_horario(self, dia: str, aula: str) -> Horario:
        return Horario(dia, "18:00", "22:00", aula)


class HorarioVirtualCreador(HorarioCreador):
    def crear_horario(self, dia: str, aula: str = "Aula Virtual") -> Horario:
        return Horario(dia, "00:00", "23:59", aula)

_fabricas_horario = {
    "matutina":    HorarioMatutinoCreador,
    "vespertina":  HorarioVespertinoCreador,
    "nocturna":    HorarioNocturnoCreador,
    "virtual":     HorarioVirtualCreador,
}

def obtener_fabrica_horario(jornada: str) -> HorarioCreador:

    jornada = jornada.strip().lower()
    if jornada not in _fabricas_horario:
        validas = list(_fabricas_horario.keys())
        raise ValueError(f"Jornada '{jornada}' no reconocida. Válidas: {validas}")
    return _fabricas_horario[jornada]()
