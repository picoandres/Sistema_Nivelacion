class Paralelo:
    def __init__(self, idParalelo, idCurso, paralelo, jornada, cupoMaximo, estado=True):
        self.idParalelo = idParalelo
        self.idCurso = idCurso
        self.paralelo = paralelo
        self.jornada = jornada
        self.cupoMaximo = cupoMaximo
        self.estado = estado
        self.nombreCurso = None
        
    def mostrarInformacion(self):
        nombreCurso = self.nombreCurso if self.nombreCurso else self.idCurso
        estado = "Activo" if self.estado else "Inactivo"

        print(f"ID paralelo  : {self.idParalelo}")
        print(f"Curso        : {nombreCurso}")
        print(f"Paralelo     : {self.paralelo}")
        print(f"Jornada      : {self.jornada}")
        print(f"Cupo máximo  : {self.cupoMaximo}")
        print(f"Estado       : {estado}")