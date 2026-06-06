#Creacion del Curso de nivelacion
class CursoNivelacion:
    def __init__(self, idCurso, nombreCurso, modalidad, jornada):
        self.idCurso = idCurso
        self.nombreCurso = nombreCurso
        self.modalidad = modalidad
        self.jornada = jornada

        #relaciones
        self.estudiantes = []
        self.materias = []

        #Docente asignado
        self.docente = None

        #Historial
        self.historial = []

    def asignarDocente(self, docente):
        pass

    def inscribir_estudiante(self, estudiante):
        pass

    @property
    def miAtributo(self):
        return self.__atributoClase

    def mostrarInformacion(self):
        pass


    def verificarCupoMaximo(self):
       pass

    def bienvenida(self):
        pass
