from Docente import Docente

class DocenteSuplente(Docente):
    def __init__(self, cedula, nombre, correo, contrasena, titulo, especialidad, tiempoSuplente):
        super().__init__(cedula, nombre, correo, contrasena, titulo, especialidad)
        self.tiempoSuplente = tiempoSuplente

    def verPerfil(self):
        super().verPerfil()
        print(f"Tiempo de suplencia: {self.tiempoSuplente} días")

    def tomarEvaluacion(self):
        print("\nTomando evaluación")
        print("Evaluación finalizada")