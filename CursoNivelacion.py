#Relaciones con otras clases
from Docente import Docente

class CursoNivelacion:
    def __init__(self, idCurso, nombreCurso, modalidad, jornada, horario):
        self.idCurso = idCurso
        self.nombreCurso = nombreCurso
        self.modalidad = modalidad
        self.jornada = jornada
        self.horario = horario

        #relaciones
        self.estudiantes = []
        
        #Docente asignado
        self.docente = None

        #Historial
        self.historial = []
    
    def mostrar_informacion(self):
        print(f"ID: {self.idCurso}")
        print(f"Nombre: {self.nombreCurso}")
        print(f"Modalidad: {self.modalidad}")
        print(f"Jornada: {self.jornada}")

#Nuevos Metodos implementados
    def asignar_docente(self, docente):
        if docente is None:
            raise ValueError("Debe proporcionar un docente")
        
        if not isinstance(docente, Docente):
            raise TypeError("Debe asignar un objeto Docente")
       
        if self.docente is not None:
            raise Exception("El curso ya tiene un docente asignado")

        self.docente = docente
        self.historial.append(f"Docente {docente.nombre} asignado")

    def buscar_estudiante(self, CedulaEstudiante):
        if not CedulaEstudiante:
            raise ValueError("Debe ingresar una cedula válida")
        
        for estudiante in self.estudiantes:
            if estudiante.Cedula == CedulaEstudiante:
                return estudiante 
        return None
    

    def agregar_estudiante(self, estudiante):
        pass
    def retirar_estudiante(self, estudiante):
        pass

    def registrar_acccion(self, mensaje):
        self.historial.append(mensaje)


    def total_inscritos(self):
        return len(self.estudiantes)
    
    def historial_acciones(self):
        if self.historial:
            return self.historial[-1]
        return "Sin registros"
    
    def mostrar_historial(self):
        for accion in self.historial:
            print(accion)