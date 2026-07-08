from Usuario import Usuario

class Estudiante(Usuario):
    def __init__(self, cedula, nombre, correo, contrasena, rol, carrera, paralelo):
        super().__init__(cedula, nombre, correo, contrasena, rol)
        self.carrera = carrera
        self.paralelo = paralelo

    def verPerfil(self):
        super().verPerfil()
        print(f"Carrera         : {self.carrera}")
        print(f"Paralelo        : {self.paralelo}")
    
    def cambiarContrasena(self, usuario_dao):
        return super().cambiarContrasena(usuario_dao)

    def verCursos(self, asignacionCurso_dao):
        cursos = asignacionCurso_dao.buscarPorEstudiante(self.cedula)

        if not cursos:
            print("\nNo se encontraron matrículas en ningún curso\n")
            return

        print("\n=================== MIS CURSOS ==================")
        for curso in cursos:
            docente = curso.docente
             
            if docente is None:
                docente = "Sin asignar"

            print(f"ID        : {curso.idCurso}")
            print(f"Nombre    : {curso.nombreCurso}")
            print(f"Modalidad : {curso.modalidad}")
            print(f"Jornada   : {curso.jornada}")
            print(f"Docente   : {docente}")
            print(f"-"*50)


    def verNotas(self, calificacion_dao):
        print("\n=============== MIS CALIFICACIONES ===============")

        calificaciones = calificacion_dao.listarPorEstudiante(self.cedula)
        if not calificaciones:
            print("\nNo tienes calificaciones registradas\n")
            return

        curso_actual = None

        for calificacion in calificaciones:
            if curso_actual != calificacion.idCurso:
                curso_actual = calificacion.idCurso

                print(f"\n===== CURSO: {calificacion.nombreCurso} ({calificacion.idCurso}) =====")

            descripcion = calificacion.descripcion if calificacion.descripcion else "Sin descripción"

            print(f"ID calificación : {calificacion.idCalificacion}")
            print(f"Evaluación      : {calificacion.titulo}")
            print(f"Materia         : {calificacion.nombreMateria}")
            print(f"Nota            : {calificacion.nota}")
            print(f"Descripción     : {descripcion}")
            print("-" * 50)


        cursos_mostrados = []
        for calificacion in calificaciones:
            if calificacion.idCurso not in cursos_mostrados:
                promedio_curso = calificacion_dao.obtenerPromedioPonderadoPorCurso(self.cedula, calificacion.idCurso)
                print(f"Promedio ponderado en {calificacion.nombreCurso}: {promedio_curso}")
                cursos_mostrados.append(calificacion.idCurso)

        promedio_general = calificacion_dao.obtenerPromedioPonderado(self.cedula)
        print("\n" + "=" * 50)
        print(f"PROMEDIO GENERAL: {promedio_general}")
        print("=" * 50)


    def verHorario(self, horario_dao):
        print("\n=============== MI HORARIO ===============")
        horario = horario_dao.listarPorEstudiante(self.cedula)

        if not horario:
            print("\nNo tienes cursos asignados con horario registrado\n")
            return

        for item in horario:
            docente = item.nombreDocente if item.nombreDocente else "Sin asignar"
            aula = item.aula if item.aula is not None else "Aula virtual"
            asignador = item.asignador if item.asignador else "No registrado"

            print(f"Curso        : {item.nombreCurso} ({item.idCurso})")
            print(f"Modalidad    : {item.modalidad}")
            print(f"Jornada      : {item.jornada}")
            print(f"Docente      : {docente}")
            print(f"Día          : {item.dia}")
            print(f"Hora         : {item.horaInicio} - {item.horaFin}")
            print(f"Aula         : {aula}")
            print(f"Asignado por : {asignador}")
            print("-" * 50)
    

    def __str__(self):
        return f"Estudiante | {self.nombre} | Carrera: {self.carrera} | Paralelo: {self.paralelo}"