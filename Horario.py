from abc import ABC, abstractmethod


class Horario(ABC):
    def __init__(self, dia, horaInicio, horaFin, aula, asignador):
        self.dia = dia
        self.horaInicio = horaInicio
        self.horaFin = horaFin
        self.aula = aula
        self.estado = "Pendiente"  # Pendiente, Aprobado, Cancelado
        self.asignador = asignador


    def verificarHorario(self, otro_horario):
        if self.dia != otro_horario.dia or self.aula != otro_horario.aula:
            return False
        return not (self.horaFin <= otro_horario.horaInicio or self.horaInicio >= otro_horario.horaFin)

    @abstractmethod
    def definir_horario(self):
        pass
    
    @abstractmethod
    def mostrarHorario(self):
        pass
    
    @abstractmethod
    def verificarAula(self, gestor_aulas):
        pass

class HorarioEstudiante(Horario):
    def __init__(self, dia, horaInicio, horaFin, aula, idEstudiante, asignador):
        super().__init__(dia, horaInicio, horaFin, aula, asignador)
        self.idEstudiante = idEstudiante
        self.materias = []

    def definir_horario(self, idMateria):
        if idMateria not in self.materias:
            self.materias.append(idMateria)
            self.estado = "Aprobado"
            return True
        return False

    def mostrarHorario(self):
        materias = ", ".join(self.materias) if self.materias else "Sin materias"
        print(f"[Estudiante {self.idEstudiante}] {self.dia} {self.horaInicio}-{self.horaFin} | Aula: {self.aula}")
        print(f"Materias: {materias} | Estado: {self.estado} | Asignado por: {self._asignado_por}")

    def verificarAula(self, gestor_aulas):
        return gestor_aulas.aula_disponible(self.aula, self.dia, self.horaInicio, self.horaFin)

class HorarioDocente(Horario):
    def __init__(self, dia, horaInicio, horaFin, aula, idDocente, asignador):
        super().__init__(dia, horaInicio, horaFin, aula, asignador)
        self.idDocente = idDocente
        self.materias = []
        self.horas_oficina = None

    def definir_horario(self, idMateria):
        self.materias.append(idMateria)
        self.estado = "Aprobado"

    def asignarHorasOficina(self, dia_oficina, hora_inicio, hora_fin):
        self.horas_oficina = (dia_oficina, hora_inicio, hora_fin)

    def mostrarHorario(self):
        materias = ", ".join(self.materias) if self.materias else "Sin materias"
        print(f"[Docente {self.idDocente}] {self.dia} {self.horaInicio}-{self.horaFin} | Aula: {self.aula}")
        print(f"Materias: {materias} | Oficina: {self.horas_oficina} | Estado: {self.estado}")

    def verificarAula(self, gestor_aulas):
        return gestor_aulas.aula_disponible(self.aula, self.dia, self.horaInicio, self.horaFin)
