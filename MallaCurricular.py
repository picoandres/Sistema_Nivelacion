class MallaCurricular:
    def __init__(self, idMalla, facultad, carrera, modalidadMalla):
        self.idMalla = idMalla
        self.facultad = facultad
        self.carrera = carrera
        self.modalidad = modalidadMalla
        self.materias = []

    def mostrarInfoMalla(self):
        print(f"Malla Curricular {self.idMalla} de la Facultad de {self.facultad}")
        print(f"Carrera: {self.carrera} Modalidad: {self.modalidad}")
        print(f"Materias: {self.materias}")

    def agregarMteria(self, materia):
        self.materias.append(materia)

    def totalCreditos(self):
        return sum(materia.creditos for materia in self.materias)