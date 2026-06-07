from Usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, cedulaEstudiante, nombre, correo, contrasena, carrera, paralelo):
        super().__init__(cedulaEstudiante, nombre, correo, contrasena)
        self.carrera = carrera
        self.paralelo = paralelo
        self.notas = []

    def verPerfil(self):
        super().verPerfil()
        print(f"Carrera: {self.carrera}")
        print(f"Paralelo: {self.paralelo}")

    def agregarNota(self, nota):
        self.notas.append(nota)
    
    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)