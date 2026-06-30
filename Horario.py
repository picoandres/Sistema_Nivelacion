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

class HorarioEstudiante(Horario):
    def __init__(self, dia, horaInicio, horaFin, aula, asignador, idEstudiante):
        super().__init__(dia, horaInicio, horaFin, aula, asignador)
        self.idEstudiante = idEstudiante
        self.materias = []

    def definirHorario(self, idMateria):
        if idMateria not in self.materias:
            self.materias.append(idMateria)
            self.estado = "Aprobado"
            return True
        return False

    def mostrarHorario(self):
        materias = ", ".join(self.materias) if self.materias else "Sin materias"
        print(f"[Estudiante {self.idEstudiante}] {self.dia} {self.horaInicio}-{self.horaFin} | Aula: {self.aula}")
        print(f"Materias: {materias} | Estado: {self.estado} | Asignado por: {self.asignador}")

    def verificarAula(self, gestor_aulas):
        return gestor_aulas.aulaDisponible(self.aula, self.dia, self.horaInicio, self.horaFin)

class HorarioSistema(Horario):
    def verificarHorario(self, otro_horario):
        if self.dia != otro_horario.dia or self.aula != otro_horario.aula:
            return False
        return not (self.horaFin <= otro_horario.horaInicio or self.horaInicio >= otro_horario.horaFin)
     
    def definir_horario(self):
        pass

    def mostrarHorario(self):
        print(f"{self.dia} {self.horaInicio}-{self.horaFin}")

    def verificarAula(self, gestor_aulas):
        return gestor_aulas.aula_disponible(
            self.aula,
            self.dia,
            self.horaInicio,
            self.horaFin
        )

class HorarioDocente(Horario):
    def __init__(self, dia, horaInicio, horaFin, aula, asignador, idDocente):
        super().__init__(dia, horaInicio, horaFin, aula, asignador)
        self.idDocente = idDocente
        self.materias = []
        self.horas_oficina = None

    def definirHorario(self, idMateria):
        self.materias.append(idMateria)
        self.estado = "Aprobado"

    def asignarHorasOficina(self, dia_oficina, hora_inicio, hora_fin):
        self.horas_oficina = (dia_oficina, hora_inicio, hora_fin)

    def mostrarHorario(self):
        materias = ", ".join(self.materias) if self.materias else "Sin materias"
        print(f"[Docente {self.idDocente}] {self.dia} {self.horaInicio}-{self.horaFin} | Aula: {self.aula}")
        print(f"Materias: {materias} | Oficina: {self.horas_oficina} | Estado: {self.estado}")

    def verificarAula(self, gestor_aulas):
        return gestor_aulas.aulaDisponible(self.aula, self.dia, self.horaInicio, self.horaFin)
    
class HorarioCurso(Horario):
    def __init__(self, dia, horaInicio, horaFin, aula, asignador):
        super().__init__(dia, horaInicio, horaFin, aula, asignador)
        self.estado = "Activo"

    def verificarHorario(self, otroHorario):
        if self.dia != otroHorario.dia:
            return False

        return not (
            self.horaFin <= otroHorario.horaInicio or
            self.horaInicio >= otroHorario.horaFin
        )

    def definirHorario(self):
        pass

    def mostrarHorario(self):
        print(f"""
        Día: {self.dia}
        Hora: {self.horaInicio} - {self.horaFin}
        Aula: {self.aula}
        Estado: {self.estado}
        """)

    def verificarAula(self, gestorAulas):
        return gestorAulas.aula_disponible(
            self.aula,
            self.dia,
            self.horaInicio,
            self.horaFin
        )