from Horario import Horario

class AsignacionHorario:
    def __init__(self, asignar: Horario):
        self.asignar = asignar  
        self.fecha_asignacion = None
        self.aprobado = False

    def aprobar(self, fecha):
        self.fecha_asignacion = fecha
        self.aprobado = True
        self.asignar.estado = "Aprobado"
        print(f"Horario aprobado para {self.asignar.dia} en aula {self.asignar.aula}")

    def cancelar(self):
        self.aprobado = False
        self.asignar.estado = "Cancelado"
        print("Asignación cancelada")

    def mostrar(self):
        print(f"--- Asignación ---")
        self.asignar.mostrarHorario()
        print(f"Aprobado: {self.aprobado} | Fecha: {self.fecha_asignacion}\n")