from abc import ABC, abstractmethod

class Horario(ABC):
    def __init__(self, dia, horaInicio, horaFin, aula, asignador):
        self.dia = dia
        self.horaInicio = horaInicio
        self.horaFin = horaFin
        self.aula = aula
        self.asignador = asignador
        self.estado = "Pendiente"

    @abstractmethod
    def verificarHorario(self, otro_horario):
        pass

    @abstractmethod
    def definirHorario(self):
        pass
    
    @abstractmethod
    def mostrarHorario(self):
        pass
    
    @abstractmethod
    def verificarAula(self, gestor_aulas):
        pass


class HorarioCurso(Horario):
    def __init__(self, dia, horaInicio, horaFin, aula, asignador):
        super().__init__(dia, horaInicio, horaFin, aula, asignador)
        self.estado = "Activo"

    def verificarHorario(self, otroHorario):
        if self.dia != otroHorario.dia:
            return False

        return not (self.horaFin <= otroHorario.horaInicio or self.horaInicio >= otroHorario.horaFin)

    def definirHorario(self):
        pass

    def mostrarHorario(self):
        print(f"Día    : {self.dia}")
        print(f"Hora   : {self.horaInicio} - {self.horaFin}")
        print(f"Aula   : {self.aula}")
        print(f"Estado : {self.estado}")
    
    def verificarAula(self, gestorAulas):
        return gestorAulas.aula_disponible(
            self.aula,
            self.dia,
            self.horaInicio,
            self.horaFin
        )