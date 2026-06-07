class Horario:
    def __init__(self, dia, horaInicio, horaFin, aula):
        self.dia = dia
        self.horaInicio = horaInicio
        self.horaFin = horaFin
        self.aula = aula

    def mostrarHorario(self):
        return (self.dia, f"{self.horaInicio}-{self.horaFin}")

    def verificarAula(self):
        if self.aula != "":
            print("Aula asignada correctamente")
        else:
            print("Aún no hay aula asignada")