class Calificacion:
    def __init__(self, idCalificacion, cedulaEstudiante, idEvaluacion, nota, retroalimentacion):
        self.idCalificacion = idCalificacion
        self.cedulaEstudiante = cedulaEstudiante
        self.idEvaluacion = idEvaluacion
        self.nota = nota
        self.retroalimentacion = retroalimentacion

        # Atributos de apoyo para listados con JOIN
        self.nombreEstudiante = None
        self.tituloEvaluacion = None
        self.nombreMateria = None
        self.idParalelo = None
        self.nombreParalelo = None

    def mostrarInfo(self):
        retroalimentacion = self.retroalimentacion if self.retroalimentacion else "Sin retroalimentación"

        print(f"ID calificación   : {self.idCalificacion}")
        print(f"Estudiante        : {self.cedulaEstudiante}")
        print(f"ID evaluación     : {self.idEvaluacion}")
        print(f"Nota              : {self.nota}")
        print(f"Retroalimentación : {retroalimentacion}")