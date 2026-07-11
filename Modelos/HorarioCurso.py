class HorarioCurso:
    def __init__(self, idHorario, idParalelo, dia, horaInicio, horaFin, aula, asignador, nombreCurso, paralelo, jornada):
        self.idHorario = idHorario
        self.idParalelo = idParalelo
        self.dia = dia
        self.horaInicio = horaInicio
        self.horaFin = horaFin
        self.aula = aula
        self.asignador = asignador

        self.nombreCurso = nombreCurso
        self.paralelo = paralelo
        self.jornada = jornada

    def verificarHorario(self, otroHorario):
        if self.dia != otroHorario.dia:
            return False

        return not (self.horaFin <= otroHorario.horaInicio or self.horaInicio >= otroHorario.horaFin)


    def mostrarHorario(self):
        aula = self.aula if self.aula else "Sin asignar"

        print(f"Paralelo  : {self.idParalelo}")
        print(f"Días      : {self.dia}")
        print(f"Hora      : {self.horaInicio} - {self.horaFin}")
        print(f"Aula      : {aula}")
        print(f"Asignador : {self.asignador}")
    

    def verificarAula(self, gestorAulas):
        return gestorAulas.aula_disponible(
            self.aula,
            self.dia,
            self.horaInicio,
            self.horaFin
        )