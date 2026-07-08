from abc import ABC, abstractmethod
from Usuario import Usuario
from GestorNotificaciones import GestorNotificaciones
from FormateadorNotificaciones import FormateadorNotificaciones
from datetime import datetime

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
    def descripcion(self):
        pass

class TiempoParcial(TiempoContrato):
    def descripcion(self):
        return "Tiempo Parcial"

class TiempoCompleto(TiempoContrato):
    def descripcion(self):
        return "Tiempo Completo"


class Docente(Usuario):
    def __init__(self, cedula, nombre, correo, contrasena, rol, profesion, especialidad, tipoDocente, tiempoContrato, idMateria):
        super().__init__(cedula, nombre, correo, contrasena, rol)
        self.profesion = profesion
        self.especialidad = especialidad
        # Patrón estructural Bridge
        self.tipoDocente = tipoDocente if tipoDocente is not None else Titular()
        self.tiempoContrato = tiempoContrato if tiempoContrato is not None else TiempoCompleto()
        self.idMateria = idMateria

    @property
    def obtenerContrasena(self):
        return self.__contrasena

    def obtenerTipoDocente(self):
        return self.tipoDocente.descripcion()

    def obtenerTiempoContrato(self):
        return self.tiempoContrato.descripcion()


    def verPerfil(self, docente_dao):
        super().verPerfil()
        print(f"Profesión       : {self.profesion}")
        print(f"Especialidad    : {self.especialidad}")
        print(f"Tipo docente    : {self.obtenerTipoDocente()}")
        print(f"Contrato        : {self.obtenerTiempoContrato()}")

        materia = docente_dao.buscarMateriaDocente(self.cedula)
        
        if materia is not None:
            print(f"Materia         : {materia.nombre} ({materia.idMateria})")
        else:
            print("Materia         : No asignada")
            
    def cambiarContrasena(self, usuario_dao):
        return super().cambiarContrasena(usuario_dao)


    def mostrarCursosAsignados(self, cursos):
        if not cursos:
            print("\nNo tienes cursos asignados\n")
            return

        print("\n===== MIS CURSOS =====")
        for curso in cursos:
            print(f"ID        : {curso.idCurso}")
            print(f"Nombre    : {curso.nombreCurso}")
            print(f"Modalidad : {curso.modalidad}")
            print(f"Jornada   : {curso.jornada}")
            print("-" * 20)


    def seleccionarCursoPropio(self, curso_dao, mensaje= "\nIngrese el ID del curso: "):
        cursos = curso_dao.buscarPorDocente(self.cedula)
        if not cursos:
            print("\nNo tienes cursos asignados\n")
            return None

        self.mostrarCursosAsignados(cursos)

        idCurso = input(mensaje).strip()

        for curso in cursos:
            if str(curso.idCurso) == idCurso:
                return curso

        print("\nEse curso no está asignado a este docente\n")
        return None


    def verCursosAsignados(self, curso_dao):
        cursos = curso_dao.buscarPorDocente(self.cedula)
        self.mostrarCursosAsignados(cursos)


    def verMateria(self, docente_dao):
        print("\n=============== MI MATERIA ===============")
        materia = docente_dao.buscarMateriaDocente(self.cedula)

        if materia is None:
            print("\nNo tienes una materia asignada\n")
            return

        print(f"ID          : {materia.idMateria}")
        print(f"Nombre      : {materia.nombre}")
        print(f"Descripción : {materia.descripcion}")
        print(f"Horas       : {materia.horas}")
        print("-" * 50)


    def verEstudiantes(self, curso_dao, asignacionCurso_dao):
        curso = self.seleccionarCursoPropio(curso_dao, "\nIngrese el ID del curso para ver sus estudiantes: ")
        if curso is None:
            return

        estudiantes = asignacionCurso_dao.buscarEstudiantesPorCursoYDocente(curso.idCurso, self.cedula)
        if not estudiantes:
            print(f"\nEl curso {curso.nombreCurso} no tiene estudiantes asignados\n")
            return

        print(f"\n===== ESTUDIANTES DEL CURSO: {curso.nombreCurso} =====")
        for estudiante in estudiantes:
            print(f"Cédula   : {estudiante.cedula}")
            print(f"Nombre   : {estudiante.nombre}")
            print(f"Correo   : {estudiante.correo}")
            print(f"Carrera  : {estudiante.carrera}")
            print(f"Paralelo : {estudiante.paralelo}")
            print("-" * 50)


    def calificarEstudiante(self, curso_dao, asignacionCurso_dao, evaluacion_dao, calificacion_dao):
        curso = self.seleccionarCursoPropio(curso_dao, "\nIngrese el ID del curso: ")
        if curso is None:
            return

        estudiantes = asignacionCurso_dao.buscarEstudiantesPorCursoYDocente(curso.idCurso, self.cedula)
        if not estudiantes:
            print(f"\nEl curso {curso.nombreCurso} no tiene estudiantes asignados\n")
            return

        print(f"\n===== ESTUDIANTES DEL CURSO: {curso.nombreCurso} =====")
        for estudiante in estudiantes:
            print(f"Cédula   : {estudiante.cedula}")
            print(f"Nombre   : {estudiante.nombre}")
            print(f"Correo   : {estudiante.correo}")
            print(f"Carrera  : {estudiante.carrera}")
            print(f"Paralelo : {estudiante.paralelo}")
            print("-" * 50)

        evaluaciones = evaluacion_dao.listarPorCursoYDocente(curso.idCurso, self.cedula)
        if not evaluaciones:
            print("\nEste curso no tiene evaluaciones registradas\n")
            return

        print(f"\n===== EVALUACIONES DEL CURSO: {curso.nombreCurso} =====")
        for evaluacion in evaluaciones:
            descripcion = evaluacion.descripcion if evaluacion.descripcion else "Sin descripción"

            print(f"ID evaluación : {evaluacion.idEvaluacion}")
            print(f"Título        : {evaluacion.titulo}")
            print(f"Materia       : {evaluacion.nombreMateria}")
            print(f"Fecha         : {evaluacion.fecha}")
            print(f"Ponderación   : {evaluacion.ponderacion}%")
            print(f"Descripción   : {descripcion}")
            print("-" * 50)

        cedulaEstudiante = input("\nIngrese la cédula del estudiante a calificar: ").strip()
        if not cedulaEstudiante:
            print("\nLa cédula del estudiante es obligatoria\n")
            return

        try:
            idEvaluacion = int(input("Ingrese el ID de la evaluación: ").strip())
        except ValueError:
            print("\nEl ID de la evaluación debe ser un número entero\n")
            return

        try:
            nota = float(input("Ingrese la nota: ").strip())
        except ValueError:
            print("\nLa nota debe ser un número natural o decimal\n")
            return

        if nota < 0 or nota > 10:
            print("\nLa nota debe estar entre 0 y 10\n")
            return

        descripcion = input("Ingrese una descripción de la calificación: ").strip()
        
        if len(descripcion) > 100:
            print("La descripción no puede exceder los 100 caracteres")
            return
        
        estudiante_obj = None
        for estudiante in estudiantes:
            if estudiante.cedula == cedulaEstudiante:
                estudiante_obj = estudiante
                break

        if estudiante_obj is None:
            print("\nEse estudiante no pertenece a este curso\n")
            return

        evaluacion_obj = None
        for evaluacion in evaluaciones:
            if evaluacion.idEvaluacion == idEvaluacion:
                evaluacion_obj = evaluacion
                break

        if evaluacion_obj is None:
            print("\nEsa evaluación no pertenece a este curso\n")
            return

        if calificacion_dao.guardar(cedulaEstudiante, curso.idCurso, idEvaluacion, nota, descripcion):
            print("\nCalificación guardada correctamente\n")

            gestor = GestorNotificaciones()
            gestor.agregar_observador(estudiante_obj)

            mensaje = FormateadorNotificaciones.nueva_calificacion(
            curso.nombreCurso,
            evaluacion_obj.nombreMateria,
            evaluacion_obj.titulo,
            nota
            )

            gestor.notificar_todos(mensaje)

        else:
            print("\nNo se pudo guardar la calificación\n")


    def verCalificaciones(self, curso_dao, calificacion_dao):
        curso = self.seleccionarCursoPropio(curso_dao, "\nIngrese el ID del curso para ver sus calificaciones: ")
        if curso is None:
            return

        calificaciones = calificacion_dao.listarPorCursoYDocente(curso.idCurso, self.cedula)
        if not calificaciones:
            print(f"\nNo hay calificaciones registradas en el curso {curso.nombreCurso}\n")
            return

        print(f"\n===== CALIFICACIONES DEL CURSO: {curso.nombreCurso} =====")
        for calificacion in calificaciones:
            descripcion = calificacion.descripcion if calificacion.descripcion else "Sin descripción"
            print(f"ID calificación : {calificacion.idCalificacion}")
            print(f"Estudiante      : {calificacion.nombreEstudiante} ({calificacion.cedulaEstudiante})")
            print(f"Evaluación      : {calificacion.tituloEvaluacion}")
            print(f"Materia         : {calificacion.nombreMateria}")
            print(f"Nota            : {calificacion.nota}")
            print(f"Descripción     : {descripcion}")
            print("-" * 20)


    def editarCalificacion(self, curso_dao, calificacion_dao):
        curso = self.seleccionarCursoPropio(curso_dao, "\nIngrese el ID del curso donde está la calificación: ")
        if curso is None:
            return

        calificaciones = calificacion_dao.listarPorCursoYDocente(curso.idCurso, self.cedula)
        if not calificaciones:
            print(f"\nNo hay calificaciones registradas en el curso {curso.nombreCurso}\n")
            return

        print(f"\n===== CALIFICACIONES DEL CURSO: {curso.nombreCurso} =====")
        for calificacion in calificaciones:
            descripcion = calificacion.descripcion if calificacion.descripcion else "Sin descripción"

            print(f"ID calificación : {calificacion.idCalificacion}")
            print(f"Estudiante      : {calificacion.nombreEstudiante} ({calificacion.cedulaEstudiante})")
            print(f"Evaluación      : {calificacion.tituloEvaluacion}")
            print(f"Materia         : {calificacion.nombreMateria}")
            print(f"Nota            : {calificacion.nota}")
            print(f"Descripción     : {descripcion}")
            print("-" * 50)
            
        try:
            idCalificacion = int(input("\nIngrese el ID de la calificación a editar: ").strip())
        except ValueError:
            print("\nEl ID de la calificación debe ser un número entero\n")
            return

        calificacion = calificacion_dao.buscarPorIdYDocente(idCalificacion, self.cedula)
        if calificacion is None:
            print("\nNo existe esa calificación o no te pertenece\n")
            return

        descripcion_actual = calificacion.descripcion if calificacion.descripcion else ""

        nueva_nota = input(f"Nueva nota [{calificacion.nota}]: ").strip()
        nueva_descripcion = input(f"Nueva descripción [{descripcion_actual}]: ").strip()

        if nueva_nota == "":
            nota = calificacion.nota
        else:
            try:
                nota = float(nueva_nota)
            except ValueError:
                print("\nLa nota debe ser un número válido\n")
                return

        if nota < 0 or nota > 10:
            print("\nLa nota debe estar entre 0 y 10\n")
            return

        descripcion = descripcion_actual if nueva_descripcion == "" else nueva_descripcion

        if calificacion_dao.editar(idCalificacion, nota, descripcion):
            print("\nCalificación actualizada correctamente\n")

            estudiante = calificacion_dao.buscarEstudianteDeCalificacion(idCalificacion)
            if estudiante is not None:
                gestor = GestorNotificaciones()
                gestor.agregar_observador(estudiante)

                descripcion = descripcion if descripcion else "Sin descripción"

                mensaje = FormateadorNotificaciones.calificacion_actualizada(
                curso.nombreCurso,
                calificacion.nombreMateria,
                calificacion.tituloEvaluacion,
                nota,
                descripcion
                )

                gestor.notificar_todos(mensaje)

        else:
            print("\nNo se pudo actualizar la calificación\n")


    def eliminarCalificacion(self, curso_dao, calificacion_dao):
        curso = self.seleccionarCursoPropio(curso_dao, "\nIngrese el ID del curso donde está la calificación: ")
        if curso is None:
            return

        calificaciones = calificacion_dao.listarPorCursoYDocente(curso.idCurso, self.cedula)
        if not calificaciones:
            print(f"\nNo hay calificaciones registradas en el curso {curso.nombreCurso}\n")
            return

        print(f"\n===== CALIFICACIONES DEL CURSO: {curso.nombreCurso} =====")
        for calificacion in calificaciones:
            descripcion = calificacion.descripcion if calificacion.descripcion else "Sin descripción"

            print(f"ID calificación : {calificacion.idCalificacion}")
            print(f"Estudiante      : {calificacion.nombreEstudiante} ({calificacion.cedulaEstudiante})")
            print(f"Evaluación      : {calificacion.tituloEvaluacion}")
            print(f"Materia         : {calificacion.nombreMateria}")
            print(f"Nota            : {calificacion.nota}")
            print(f"Descripción     : {descripcion}")
            print("-" * 50)

        try:
            idCalificacion = int(input("\nIngrese el ID de la calificación a eliminar: ").strip())
        except ValueError:
            print("\nEl ID de la calificación debe ser un número entero\n")
            return

        calificacion = calificacion_dao.buscarPorIdYDocente(idCalificacion, self.cedula)
        if calificacion is None:
            print("\nNo existe esa calificación o no te pertenece\n")
            return

        confirmar = input("¿Seguro que deseas eliminarla? (s/n): ").strip().lower()
        if confirmar != "s":
            print("\nOperación cancelada\n")
            return

        if calificacion_dao.eliminar(idCalificacion):
            print("\nCalificación eliminada correctamente\n")
        else:
            print("\nNo se pudo eliminar la calificación\n")


    def crearEvaluacion(self, curso_dao, materia_dao, evaluacion_dao, asignacionCurso_dao):
        curso = self.seleccionarCursoPropio(curso_dao, "\nIngrese el ID del curso: ")
        if curso is None:
            return
        curso = curso.strip().uppercase()

        if not self.idMateria:
            print("\nNo tienes una materia asignada como docente\n")
            return

        materia = materia_dao.buscarPorId(self.idMateria)
        if materia is None:
            print("\nLa materia asignada al docente no existe\n")
            return
       
        print(f"\n===== CREAR EVALUACIÓN EN {curso.nombreCurso} =====")
        print(f"Materia del docente: {materia.nombre} ({materia.idMateria})")

        titulo = input("Título de la evaluación: ").strip()
        if len(titulo) > 50:
            print("El título no puede exceder los 50 caracteres")
            return
        
        descripcion = input("Descripción: ").strip()
        fecha = input("Fecha (AAAA-MM-DD): ").strip()

        if not titulo or not descripcion or not fecha:
            print("\nTodos los campos son obligatorios\n")
            return

        try:
            ponderacion = int(input("Ponderación (%): ").strip())
            if ponderacion <= 0 or ponderacion > 100:
                print("\nLa ponderación debe estar entre 1 y 100\n")
                return
        except ValueError:
            print("\nLa ponderación debe ser un número entero\n")
            return

        try:
            datetime.strptime(fecha, "%Y-%m-%d")
        except ValueError:
            print("\nLa fecha debe tener el formato AAAA-MM-DD\n")
            return

        if evaluacion_dao.guardar(curso.idCurso, materia.idMateria, titulo, descripcion, fecha, ponderacion):
            print("\nEvaluación creada correctamente\n")

             #IMPLEMENTACIÓN DEL OBSERVER
            estudiantes = asignacionCurso_dao.buscarEstudiantesPorCursoYDocente(curso.idCurso, self.cedula)

            if estudiantes:
                gestor = GestorNotificaciones()

                for estudiante in estudiantes:
                    gestor.agregar_observador(estudiante)
                
                mensaje = FormateadorNotificaciones.nueva_evaluacion(
                curso.nombreCurso,
                materia.nombre,
                titulo,
                fecha,
                ponderacion
                )
                
                gestor.notificar_todos(mensaje)
                
            else:
                print("No hay estudiantes asignados al curso para notificar")
        
        else:
            print("\nNo se pudo crear la evaluación\n")


    def verEvaluaciones(self, evaluacion_dao):
        print("\n=============== MIS EVALUACIONES ===============")
        evaluaciones = evaluacion_dao.listarPorDocente(self.cedula)

        if not evaluaciones:
            print(f"\nNo tienes evaluaciones registradas\n")
            return

        for evaluacion in evaluaciones:
            descripcion = evaluacion.descripcion if evaluacion.descripcion else "Sin descripción"
            materia = evaluacion.nombreMateria if evaluacion.nombreMateria else "Sin materia"
            
            print(f"ID evaluación : {evaluacion.idEvaluacion}")
            print(f"Título        : {evaluacion.titulo}")
            print(f"Curso         : {evaluacion.nombreCurso} ({evaluacion.idCurso})")
            print(f"Materia       : {materia}")
            print(f"Fecha         : {evaluacion.fecha}")
            print(f"Ponderación   : {evaluacion.ponderacion}%")
            print(f"Descripción   : {descripcion}")
            print("-" * 50)


    def editarEvaluacion(self, evaluacion_dao):
        print("\n=============== EDITAR EVALUACIÓN ===============")
        evaluaciones = evaluacion_dao.listarPorDocente(self.cedula)
        
        if not evaluaciones:
            print("\nNo tienes evaluaciones registradas\n")
            return

        print("\n===== MIS EVALUACIONES =====")
        for ev in evaluaciones:
            descripcion = ev.descripcion if ev.descripcion else "Sin descripción"
            materia = ev.nombreMateria if ev.nombreMateria else "Sin materia"

            print(f"ID evaluación : {ev.idEvaluacion}")
            print(f"Curso         : {ev.nombreCurso} ({ev.idCurso})")
            print(f"Materia       : {materia}")
            print(f"Título        : {ev.titulo}")
            print(f"Descripción   : {descripcion}")
            print(f"Fecha         : {ev.fecha}")
            print(f"Ponderación   : {ev.ponderacion}%")
            print("-" * 50)
    
        id_evaluacion = input("\nIngrese el ID de la evaluación a editar: ").strip()
        if not id_evaluacion:
            print("\nDebe ingresar un ID de Evaluación\n")
            return

        try:
            idEvaluacion = int(id_evaluacion)
        except ValueError:
            print("\nEl ID de la evaluación debe ser un número entero\n")
            return

        evaluacion = evaluacion_dao.buscarPorId(id_evaluacion)
        if evaluacion is None:
            print("\nNo existe una evaluación con ese ID\n")
            return

        pertenece = False
        for ev in evaluaciones:
            if ev.idEvaluacion == idEvaluacion:
                pertenece = True
                break
        
        if not pertenece:
            print("\nNo puedes editar evaluaciones de otros docentes\n")
            return

        if str(evaluacion.idMateria).strip() != str(self.idMateria).strip():
            print("\nNo puedes editar una evaluación de una materia distinta a la tuya\n")
            return

        descripcion_actual = evaluacion.descripcion if evaluacion.descripcion else ""

        print("\nIngrese los nuevos datos de la evaluación (Enter para conservar el valor actual)")
        
        nuevo_titulo = input(f"Nuevo título [{evaluacion.titulo}]: ").strip()
        if len(nuevo_titulo) > 50:
            print("\nEl título no puede exceder los 50 caracteres\n")
            return
        
        nueva_descripcion = input(f"Nueva descripción [{descripcion_actual}]: ").strip()
        nueva_fecha = input(f"Nueva fecha [{evaluacion.fecha}] (AAAA-MM-DD): ").strip()

        try:
            nueva_ponderacion = int(input(f"Nueva ponderación [{evaluacion.ponderacion}]: ").strip())
            if nueva_ponderacion <= 0 or nueva_ponderacion > 100:
                print("\nLa ponderación debe estar entre 1 y 100\n")
                return
        except ValueError:
            print("\nLa ponderación debe ser un número entero\n")
            return

        titulo = evaluacion.titulo if nuevo_titulo == "" else nuevo_titulo
        descripcion = descripcion_actual if nueva_descripcion == "" else nueva_descripcion
        fecha = str(evaluacion.fecha) if nueva_fecha == "" else nueva_fecha
        ponderacion = int(evaluacion.ponderacion) if nueva_ponderacion == "" else nueva_ponderacion

        if not nuevo_titulo or not nueva_descripcion or not nueva_fecha or not nueva_ponderacion:
            print("\nTodos los campos son obligatorios\n")
            return

        try:
            datetime.strptime(nueva_fecha, "%Y-%m-%d")
        except ValueError:
            print("\nLa fecha debe tener el formato AAAA-MM-DD\n")
            return

        if evaluacion_dao.editar(idEvaluacion, titulo, descripcion, fecha, ponderacion):
            print("\nEvaluación editada correctamente\n")
        else:
            print("\nNo se pudo editar la evaluación\n")


    def eliminarEvaluacion(self, evaluacion_dao):
        print("\n===== ELIMINAR EVALUACIÓN =====")
        evaluaciones = evaluacion_dao.listarPorDocente(self.cedula)
        if not evaluaciones:
            print("\nNo tienes evaluaciones registradas\n")
            return

        print("\n===== MIS EVALUACIONES =====")
        for ev in evaluaciones:
            descripcion = ev.descripcion if ev.descripcion else "Sin descripción"
            print(f"ID evaluación : {ev.idEvaluacion}")
            print(f"Curso         : {ev.nombreCurso}")
            print(f"Materia       : {ev.nombreMateria}")
            print(f"Título        : {ev.titulo}")
            print(f"Descripción   : {descripcion}")
            print(f"Fecha         : {ev.fecha}")
            print(f"Ponderación   : {ev.ponderacion}%")
            print("-" * 50)

        id_evaluacion = input("\nIngrese el ID de la evaluación a eliminar: ").strip()
        if not id_evaluacion:
            print("\nDebe ingresar un ID de evaluación\n")
            return

        try:
            idEvaluacion = int(id_evaluacion)
        except ValueError:
            print("\nEl ID de la evaluación debe ser un número entero\n")
            return

        evaluacion = evaluacion_dao.buscarPorId(idEvaluacion)
        if evaluacion is None:
            print("\nNo existe una evaluación con ese ID\n")
            return

        pertenece = False
        for ev in evaluaciones:
            if ev.idEvaluacion == idEvaluacion:
                pertenece = True
                break

        if not pertenece:
            print("\nNo puedes eliminar evaluaciones de otros docentes\n")
            return

        confirmar = input("¿Está seguro de eliminar esta evaluación? (s/n): ").strip().lower()
        if confirmar != "s":
            print("\nOperación cancelada\n")
            return

        if evaluacion_dao.eliminar(idEvaluacion):
            print("\nEvaluación eliminada correctamente\n")
        else:
            print("\nNo se pudo eliminar la evaluación\n")

    
    def verHorario(self, horario_dao):
        print("\n=============== MI HORARIO ===============")
        horario = horario_dao.listarPorDocente(self.cedula)

        if not horario:
            print("\nNo tienes cursos con horario asignado\n")
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