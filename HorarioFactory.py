from abc import ABC, abstractmethod
from Horario import HorarioCurso

class HorarioCreador(ABC):
    @abstractmethod
    def crearHorario(self, dia: str, aula: str, asignador: str):
        pass


class HorarioMatutinoCreador(HorarioCreador):
    def crearHorario(self, dia: str, aula: str, asignador: str):
        return HorarioCurso(dia, "07:00", "13:00", aula, asignador)


class HorarioVespertinoCreador(HorarioCreador):
    def crearHorario(self, dia: str, aula: str, asignador: str):
        return HorarioCurso(dia, "13:00", "18:00", aula, asignador)


class HorarioNocturnoCreador(HorarioCreador):
    def crearHorario(self, dia: str, aula: str, asignador: str):
        return HorarioCurso(dia, "18:00", "22:00", aula, asignador)


class HorarioVirtualCreador(HorarioCreador):
    def crearHorario(self, dia: str, aula: str, asignador: str):
        return HorarioCurso(dia, "00:00", "23:59", aula, asignador)

_fabricas_horario = {
    "matutina":    HorarioMatutinoCreador,
    "vespertina":  HorarioVespertinoCreador,
    "nocturna":    HorarioNocturnoCreador,
    "virtual":     HorarioVirtualCreador,
}

def obtenerFabricaHorario(jornada: str):
    jornada = jornada.strip().lower()
    if jornada not in _fabricas_horario:
        validas = list(_fabricas_horario.keys())
        raise ValueError(f"Jornada '{jornada}' no reconocida. Válidas: {validas}")
    return _fabricas_horario[jornada]()