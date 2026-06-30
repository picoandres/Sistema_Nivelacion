from abc import ABC, abstractmethod
from Usuario import Usuario

class TipoDocente(ABC):
    @abstractmethod
    def descripcion(self):
        pass

class Titular(TipoDocente):
    def descripcion(self):
        return "Titular"
    
class Suplente(TipoDocente):
    def descripcion(self):
        return "Suplente"
    
class TiempoContrato(ABC):
    @abstractmethod
    def contrato(self):
        pass

class TiempoParcial(TiempoContrato):
    def contrato(self):
        return "Tiempo Parcial"

class TiempoCompleto(TiempoContrato):
    def contrato(self):
        return "Tiempo Completo"

class Docente(Usuario):
    def __init__(self, cedula, nombre, correo, contrasena, rol, titulo, especialidad):
        super().__init__(cedula, nombre, correo, contrasena, rol)
        self.titulo = titulo
        self.especialidad = especialidad
        self.cursos = []
        self.evaluaciones_creadas = []

    #Polimorfismo con sobreescritura de métodos de usuario
    def verPerfil(self):
        super().verPerfil()  
        print(f"Título Académico: {self.titulo}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Cursos Asignados: {len(self.cursos)}")

    #Métodos de Docente
    def mostrarCursosAsignados(self, cursos):
        if not cursos:
            print("\nNo tiene cursos asignados\n")
            return

        print("\n===== MIS CURSOS =====")
        for curso in cursos:
            print(f"ID: {curso.idCurso}")
            print(f"Nombre: {curso.nombreCurso}")
            print(f"Modalidad: {curso.modalidad}")
            print(f"Jornada: {curso.jornada}")
            print("-"*20)

    def calificar(self, estudiante, nota, materia):
        if not (0 <= nota <= 10):
            print("Error: la calificacion debe estar entre 0 y 10")
            return
        else:
            estudiante.agregarNota(materia, nota)
            print(f"Se calificó a {estudiante.nombre} con {nota} en la materia {materia.nombre}")
                   
    def crearEvaluacion(self, tituloEvaluacion, descripcion):
        evaluacion = {
            "titulo": tituloEvaluacion,
            "descripcion": descripcion,
            "docente": self.nombre
        }
        self.evaluaciones_creadas.append(evaluacion)
        print(f"Evaluacion {tituloEvaluacion} creada exitosamente")
        return evaluacion

    def verCronogramaTrabajo(self):
        pass
    
    def verEstudiantesCurso(self, curso):
        if curso in self.cursos:
            print(f"Estudiantes en {curso.nombre}")
            print()
        else:
            print("Este curso no existe")