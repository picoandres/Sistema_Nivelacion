class Matricula:
    def __init__(self, cedulaEstudiante, idParalelo, fechaAsignacion=None,
                 nombreEstudiante=None, nombreCurso=None, paralelo=None):
        self.cedulaEstudiante = cedulaEstudiante
        self.idParalelo = idParalelo
        self.fechaAsignacion = fechaAsignacion

        # opcionales para mostrar joins
        self.nombreEstudiante = nombreEstudiante
        self.nombreCurso = nombreCurso
        self.paralelo = paralelo

    def mostrarInfo(self):
        nombreEstudiante = self.nombreEstudiante if self.nombreEstudiante else self.cedulaEstudiante
        paralelo = self.paralelo if self.paralelo else self.idParalelo

        print(f"Estudiante       : {nombreEstudiante}")
        print(f"Paralelo         : {paralelo}")
        print(f"Fecha asignación : {self.fechaAsignacion}")