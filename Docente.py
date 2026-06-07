from Usuario import Usuario

class Docente(Usuario):
    def __init__(self, cedulaDocente, nombre, correo, contrasena, titulo, especialidad):
        super().__init__(cedulaDocente, nombre, correo, contrasena)
        self.titulo = titulo
        self.especialidad = especialidad
        self.cursos = []

    def verPerfil(self):
        super().verPerfil()
        print(f"Título: {self.titulo}")
        print(f"Especialidad: {self.especialidad}")

    def asignarCurso(self, curso):
        self.cursos.append(curso)

    def calificar(self, estudiante, nota):
        estudiante.agregarNota(nota)