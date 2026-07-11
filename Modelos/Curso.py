class Curso:
    def __init__(self, idCurso, nombreCurso, modalidad):
        self.idCurso = idCurso
        self.nombreCurso = nombreCurso
        self.modalidad = modalidad

    def mostrarInformacionCurso(self):
        print(f"ID        : {self.idCurso}")
        print(f"Nombre    : {self.nombreCurso}")
        print(f"Modalidad : {self.modalidad}")