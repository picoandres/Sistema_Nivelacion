class CursoNivelacion:
    atributoClase = "Público"
    __atributoClase = "Privado"
    def __init__(self, idCurso, nombreCurso, cupoMaximo, modalidad, jornada):
        self.idCurso = idCurso
        self.nombreCurso = nombreCurso
        self.cupoMaximo = cupoMaximo
        self.modalidad = modalidad
        self.jornada = jornada

    @property
    def miAtributo(self):
        return self.__atributoClase

    def mostrarInformacion(self):
        print(f"ID: {self.idCurso}")
        print(f"Nombre: {self.nombreCurso}")
        print(f"Cupo Máximo: {self.cupoMaximo}")
        print(f"Modalidad: {self.modalidad}")
        print(f"Jornada: {self.jornada}")

    def verificarCupoMaximo(self):
        if self.cupoMaximo > 0:
            print("El curso tiene cupos disponibles")
        else:
            print("No hay cupos disponibles")

    def bienvenida(self):
        print(f"Bienvenidos al curso de: {self.nombreCurso}")

class Usuario:
    def __init__(self, idUsuario, nombre, correo, contrasena, rol):
        self.idUsuario = idUsuario
        self.nombre = nombre
        self.correo = correo
        self.contrasena = contrasena
        self.rol = rol
    
    def iniciarSesion(self):
        print(f"El usuario '{self.nombre}' ha iniciado sesión")

    def cerrarSesion(self):
        print(f"El usuario {self.nombre} ha salido del sistema")

    def verPerfil(self):
        print("Perfil de usuario")
        print(f"ID: {self.idUsuario}")
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        print(f"Contraseña: {self.contrasena}")
        print(f"Rol: {self.rol}")

    def recuperarContrasena(self, **kwargs):
        print("Escoja un método para recuperar su contraseña")

        while True:
            opcion = input("Correo o teléfono: ").lower()

            if opcion in kwargs.values():
                print("Código: 1234")

                codigo = input("Ingrese el código que acaba de recibir: ")

                if codigo == "1234":
                    self.contrasena = input("Escriba la nueva contraseña: ")
                    print("Contraseña actualizada")
                    break
                else:
                    print("Código incorrecto")
            
            else:
                print("Escoja solo entre correo o número de teléfono")

    def editarPerfil(self, *args):
        print("Editar perfil")
        print("Nuevos datos:", args)
        print("Perfil actualizado exitosamente\n")

class Docente(Usuario):
    def __init__(self, idUsuario, nombre, correo, contrasena, rol, titulo, especialidad):
        super().__init__(idUsuario, nombre, correo, contrasena, rol)
        self.titulo = titulo
        self.especialidad = especialidad

    def verPerfil(self):
        super().verPerfil()
        print(f"Título: {self.titulo}")
        print(f"Especialidad: {self.especialidad}")

    def tomarEvaluacion(self):
        print("\nTomando evaluación")
        print("Evaluación finalizada")
        nota = input("Calificación: ")
        print()
    
class DocenteSuplente(Docente):
    def __init__(self, idUsuario, nombre, correo, contrasena, rol, titulo, especialidad, tiempoSuplente):
        super().__init__(idUsuario, nombre, correo, contrasena, rol, titulo, especialidad)
        self.tiempoSuplente = tiempoSuplente

    def verPerfil(self):
        super().verPerfil()
        print(F"Tiempo de suplencia: {self.tiempoSuplente} días")

    def tomarEvaluacion(self):
        print("\nTomando evaluación")
        print("Evaluación finalizada")
        print(f"La evaluación será entregada al docente {docente1.nombre}")

class Inscripcion:
    def __init__(self, idInscripcion, estado, fechaInscripcion):
        self.idInscripcion = idInscripcion
        self.estado = estado
        self.fechaInscripcion = fechaInscripcion

    def estadoInscripcion(self):
        print(f"Inscripción: {self.idInscripcion}")
        print(f"Estado: {self.estado}")

    def verificarFecha(self):
        print(f"Fecha de inscripción: {self.fechaInscripcion}")
    
    def alerta(self):
        print("Recuerde verificar el estado de su inscripción regularmente")


class MallaCurricular:
    def __init__(self, idMalla, facultad, carrera, modalidadMalla, cantidadPeriodos, materias):
        self.idMalla = idMalla
        self.facultad = facultad
        self.carrera = carrera
        self.modalidad = modalidadMalla
        self.cantidadPeriodos = cantidadPeriodos
        self.materias = materias

    def mostrarInfoMalla(self):
        print(f"Malla Curricular {self.idMalla} de la Facultad de {self.facultad}")
        print(f"Carrera: {self.carrera} Modalidad: {self.modalidad}")
        print(f"Cantidad de periodos: {self.cantidadPeriodos}")
        print(f"Materias: {self.materias}")

    def mostrarRequisitosIngreso(self):
        print("""Poseer título de bachiller o su equivalente, de conformidad con la Ley.
                Haber cumplido los requisitos normados por el Sistema de Nivelación y Admisión.
                Cumplir con la entrega de documentación personal y habilitante en la secretaría general de la Universidad.""")
        
    def mostrarRequisitosGraduacion(self):
        print("""Haber aprobado las asignaturas de las unidades básica y profesional del plan curricular de la carrera.
                Acreditar nivel de suficiencia B1 en un idioma extranjero por medio del certificado emitido u homologado por el
                Instituto de idiomas de la Universidad en sus diferentes modalidades: Cursos complementarios o Convenio con Institutos acreditados.""")


class Horario:
    def __init__(self, dia, hora, aula):
        self.dia = dia
        self.hora = hora
        self.aula = aula
    
    def mostrarHorario(self):
        print(f"Días de clases: {self.dia}")
        print(f"Hora: {self.hora}")
        
    def mostrarAula(self):
        print(f"Aula: {self.aula}")

    def verificarAula(self):
        if self.aula != "":
            print("Aula asignada correctamente")
        else:
            print("Aún no hay aula asignada")


#Instancias de objetos
#curso = CursoNivelacion(1234, "Nivelación para Software", 30, "virtual", "matutina")
#usuario1 = Usuario(123, "Andrés Pico", "ejemplo@gmail.com", "Pico1212", "Estudiante")
#inscripcion1 = Inscripcion("SOFT-299", "Activa", "01/04/2026")
#mallaCurricular = MallaCurricular("FCTV-SW-A04", "Ciencias de la Vida y Tecnologías", "Software", "Presencial", 8, "Estilo de Vida, Emprendimiento Global, Matemáticas, Lógica de Algoritmos")
#horario = Horario("Lunes - Viernes", "8:00 a.m - 13:00 p.m", "Aula virtual A28")
docente1 = Docente(456, 'Juan Sendón', 'SendonJuanca@gmail.com', 'juanchito123', 'Docente', 'Ingeniero en Software', 'Ingeniería de Requisitos')
docentesuplente1 = DocenteSuplente(2937, 'Robert Moreira', 'robmoreira@gmail.com', 'moreira6574', 'Docente Suplente', 'Ingeniero en Sistemas', 'Bases de Datos', 3)

#Métodos de docente
docente1.verPerfil()
docente1.tomarEvaluacion()

docentesuplente1.verPerfil()
docentesuplente1.tomarEvaluacion()
#Métodos de usuario
#usuario1.editarPerfil(123, "Juan", "juan1314@gmail.com", "juan8595", "Estudiante")
#usuario1.recuperarContrasena(a="correo", b="telefono", c= "teléfono")

#Métodos de inicio de sesión
#usuario1.iniciarSesion()
#curso.bienvenida()

#Métodos de revisión de curso
#curso.mostrarInformacion()
#curso.verificarCupoMaximo()

#Métodos de revisión de datos personales
#usuario1.verPerfil()
#inscripcion1.estadoInscripcion()
#inscripcion1.verificarFecha()
#inscripcion1.alerta()

#Métodos de revisión de malla
#mallaCurricular.mostrarInfoMalla()
#mallaCurricular.mostrarRequisitosIngreso()
#mallaCurricular.mostrarRequisitosGraduacion()

#Métodos de Horario
#horario.mostrarHorario()
#horario.mostrarAula()
#horario.verificarAula()

#usuario1.cerrarSesion()
