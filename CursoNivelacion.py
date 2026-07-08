class CursoNivelacion:
    def __init__(self, idCurso, nombreCurso, modalidad, jornada, horario, docente = None):
        self.idCurso = idCurso
        self.nombreCurso = nombreCurso
        self.modalidad = modalidad
        self.jornada = jornada
        self.horario = horario
        self.docente = docente
    
    def mostrarInformacion(self):
        print(f"ID: {self.idCurso}")
        print(f"Nombre: {self.nombreCurso}")
        print(f"Modalidad: {self.modalidad}")
        print(f"Jornada: {self.jornada}")