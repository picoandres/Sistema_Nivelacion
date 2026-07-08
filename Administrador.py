from Usuario import Usuario
from HorarioFactory import obtenerFabricaHorario
from CursoNivelacion import CursoNivelacion

class Administrador(Usuario):
    def __init__(self, cedula, nombre, correo, contrasena, rol, idAdmin, sede, telefono):
        super().__init__(cedula, nombre, correo, contrasena, rol)
        self.idAdmin = idAdmin
        self.sede = sede
        self.telefono = telefono
        self.historialAcciones = []

    def verPerfil(self):
        super().verPerfil()
        print(f"Sede            : {self.sede}")
        print(f"Teléfono        : {self.telefono}")
    
    def cambiarContrasena(self, usuario_dao):
        return super().cambiarContrasena(usuario_dao)


    def registrarAccion(self, mensaje):
        self.historialAcciones.append(mensaje)

    def mostrarHistorial(self):
        if not self.historialAcciones:
            print("\nSin acciones registradas")
            return

        print(f"\n──── HISTORIAL DE ACCIONES — {self.nombre} ────")
        for i, accion in enumerate(self.historialAcciones, 1):
            print(f"  {i}. {accion}")
        print()

 
    def mostrarCursos(self, curso_dao):
        cursos = curso_dao.listar()
        if not cursos:
            print("\nNo hay cursos registrados\n")
            return

        print("\n===================== CURSOS =====================")
        for curso in cursos:
            print(f"ID        : {curso.idCurso}")
            print(f"Nombre    : {curso.nombreCurso}")
            print(f"Modalidad : {curso.modalidad}")
            print(f"Jornada   : {curso.jornada}")
            print(f"Docente   : {curso.nombreDocente}")
            print("-" * 50)

    def mostrarEstudiantes(self, estudiantes):
        if not estudiantes:
            print("\nNo hay estudiantes registrados\n")
            return

        print("\n=================== ESTUDIANTES ==================")
        for estudiante in estudiantes:
            print(f"Cédula   : {estudiante.cedula}")
            print(f"Nombre   : {estudiante.nombre}")
            print(f"Correo   : {estudiante.correo}")
            print(f"Carrera  : {estudiante.carrera}")
            print(f"Paralelo : {estudiante.paralelo}")
            print("-" * 50)

    def mostrarDocentes(self, docentes):
        if not docentes:
            print("\nNo hay docentes registrados\n")
            return

        print("\n==================== DOCENTES ====================")
        for docente in docentes:
            materia = docente.idMateria if docente.idMateria else "Sin materia"
            print(f"Cédula           : {docente.cedula}")
            print(f"Nombre           : {docente.nombre}")
            print(f"Correo           : {docente.correo}")
            print(f"Profesión        : {docente.profesion}")
            print(f"Especialidad     : {docente.especialidad}")
            print(f"Tipo de docente  : {docente.obtenerTipoDocente()}")
            print(f"Tipo de contrato : {docente.obtenerTiempoContrato()}")
            print(f"ID de Materia    : {materia}")
            print("-" * 50)


    def crearCurso(self, curso_dao, horario_dao, gestor_aulas):
        import re

        while True:
            idCurso = input("ID del curso: ").strip().upper()

            if not re.fullmatch(r"[A-Z][0-9]{2}", idCurso):
                print("\nDebe ingresar una letra mayúscula seguida de dos números.")
                continue

            numero = int(idCurso[1:])

            if not (1 <= numero <= 99):
                print("\nEl número debe estar entre 01 y 99.")
                continue

            if curso_dao.buscar(idCurso):
                print("\nYa existe un curso con ese ID.")
                continue
            break
        
        while True:
            nombreCurso = input("Nombre del curso: ").strip()

            if nombreCurso:
                break

            print("El nombre no puede estar vacío.")


        while True:
            modalidad = input("Modalidad (presencial / virtual / híbrida): ").strip().lower()

            if modalidad in ["presencial", "virtual", "hibrida", "híbrida"]:
                modalidad = modalidad.replace("híbrida", "hibrida")
                break

            print("Modalidad inválida.")

        while True:
            jornada = input("Jornada (matutina / vespertina / nocturna ): ").strip().lower()

            if jornada in ["matutina", "vespertina", "nocturna"]:
                break

            print("Jornada inválida.")

        while True:
            print("Ejemplo: lunes-viernes ,lunes, miércoles y viernes ")
            dia = input("Día: ").strip().lower()

            if dia in ["lunes-viernes", "lunes, miércoles y viernes", "lunes, miercoles y viernes"]:
                break

            print("Día inválido.")

        while True:
            aula = input("Aula: ").strip()

            if aula:
                break

            print("Debe ingresar un aula.")

        if not idCurso or not nombreCurso or not modalidad or not jornada or not dia or not aula:
            print("\nTodos los campos son obligatorios")
            return

        try:
            fabrica = obtenerFabricaHorario(jornada)
            horario = fabrica.crearHorario(dia, aula, self.nombre)

            if not horario.verificarAula(gestor_aulas):
                print("\nEl aula ya está ocupada en ese día y horario\n")
                return

            curso = CursoNivelacion(idCurso,nombreCurso, modalidad, jornada, horario)

            if curso_dao.guardar(curso):
                print(f"\nCurso {nombreCurso} ({idCurso}) creado exitosamente\n")
                self.registrarAccion(f"Se creó el curso: {nombreCurso} ({idCurso})")
            else:
                print("\nNo se pudo crear el curso\n")

            if not horario_dao.guardar(idCurso, horario):
                print("\nEl curso se creó, pero no se pudo guardar el horario\n")
                return

        except Exception as e:
            print("Error al crear el curso:", e)


    def registrarMateria(self, materia_dao):
        print("\n=============== REGISTRO DE MATERIA ================")

        import re

        while True:
            idMateria = input("ID de la materia: ").strip().upper()

            if len(idMateria) > 5:
                print("\nEl ID de la materia no puede tener más de 5 caracteres.")
                continue

            if not re.fullmatch(r"[A-Za-z0-9\-]+", idMateria):
                print("\nEl ID solo puede contener letras, números y guiones.")
                continue

            if materia_dao.buscar(idMateria):
                print("\nYa existe una materia con ese ID.")
                continue
            break

        while True:
            nombre = input("Nombre: ").strip()

            if nombre:
                break

            print("El nombre no puede estar vacío.")
        
        while True:
            descripcion = input("Descripción: ").strip()

            if descripcion:
                break

            print("La descripción no puede estar vacía.")

        while True:
            try:
                horas = int(input("Horas: ").strip())

                if horas > 0:
                    break

                print("Las horas deben ser mayores a 0.")

            except ValueError:
                print("Debe ingresar un número entero.")

        estado = True

        from Materia import Materia
        materia = Materia(idMateria, nombre, descripcion, horas, estado)

        if materia_dao.guardar(materia):
            self.registrarAccion(f"Se registró la materia: {nombre}")
            print(f"\nMateria {nombre} ({idMateria}) registrada correctamente\n")
        else:
            print("\nNo se pudo registrar la materia\n")


    def listarCursos(self, curso_dao):
        self.mostrarCursos(curso_dao)

    def listarEstudiantes(self, estudiante_dao):
        estudiantes = estudiante_dao.listar()
        self.mostrarEstudiantes(estudiantes)

    def listarDocentes(self, docente_dao):
        docentes = docente_dao.listar()
        self.mostrarDocentes(docentes)


    def asignarDocenteACurso(self, curso_dao, docente_dao, cursoMateria_dao):
        print("\n=============== ASIGNAR DOCENTE A CURSO ===============")
        self.mostrarCursos(curso_dao)

        docentes = docente_dao.listar()
        self.mostrarDocentes(docentes)

        while True:
            idCurso = input("\nID del Curso: ").strip().upper()

            if not idCurso:
                print("Debe ingresar un ID de curso.")
                continue

            curso = curso_dao.buscar(idCurso)

            if curso:
                break

            print("No existe un curso con ese ID.")

        while True:
            cedula_docente = input("Cédula del docente: ").strip()

            if not cedula_docente:
                print("Debe ingresar la cédula del docente.")
                continue

            docente = docente_dao.buscar(cedula_docente)

            if docente:
                break

            print("No existe un docente con esa cédula.")

        if not cursoMateria_dao.existe(idCurso, docente.idMateria):
            print("\nLa materia del docente no está asignada al curso\n")
            return        

        if curso_dao.asignarDocente(idCurso, cedula_docente):
            print(f"\nDocente {docente.nombre} asignado correctamente al curso {curso.nombreCurso}\n")
            self.registrarAccion(f"Docente {docente.nombre} ({cedula_docente}) asignado al curso {curso.nombreCurso} ({idCurso})")
        else:
            print("\nNo se pudo asignar el docente al curso\n")


    def asignarEstudianteACurso(self, curso_dao, estudiante_dao, asignacionCurso_dao):
        self.mostrarCursos(curso_dao)

        estudiantes = estudiante_dao.listar()
        if not estudiantes:
            print("\nNo hay estudiantes registrados\n")
            return
        
        self.mostrarEstudiantes(estudiantes)

        while True:
            cedula = input("\nCédula del estudiante: ").strip()

            if not cedula:
                print("Debe ingresar la cédula del estudiante.")
                continue

            estudiante = estudiante_dao.buscar(cedula)

            if estudiante:
                break

            print("No existe un estudiante con esa cédula.")

        while True:
            idCurso = input("ID del curso: ").strip().upper()

            if not idCurso:
                print("Debe ingresar el ID del curso.")
                continue

            curso = curso_dao.buscar(idCurso)

            if curso:
                break

            print("No existe un curso con ese ID.")

        if asignacionCurso_dao.existe(cedula, idCurso):
            print("\nEl estudiante ya está asignado a ese curso\n")
            return

        if asignacionCurso_dao.guardar(cedula, idCurso):
            print(f"\nEstudiante {estudiante.nombre} asignado correctamente al curso {curso.nombreCurso}\n")
            self.registrarAccion(f"Estudiante {estudiante.nombre} ({cedula}) asignado al curso {curso.nombreCurso} ({idCurso})")
        else:
            print("\nNo fue posible realizar la asignación\n")

    def asignarMateriaACurso(self, curso_dao, materia_dao, cursoMateria_dao):
        self.mostrarCursos(curso_dao)

        print("\n============== MATERIAS DISPONIBLES ==============")
        materias = materia_dao.listar()
        if not materias:
            print("No hay materias registradas\n")
            return

        for materia in materias:
            print(f"ID          : {materia.idMateria}")
            print(f"Nombre      : {materia.nombre}")
            print(f"Descripción : {materia.descripcion}")
            print(f"Horas       : {materia.horas}")
            print("-" * 50)

        while True:
            idCurso = input("\nIngrese el ID del curso: ").strip().upper()

            if not idCurso:
                print("Debe ingresar el ID del curso.")
                continue

            curso = curso_dao.buscar(idCurso)

            if curso:
                break

            print("No existe un curso con ese ID.")

        while True:
            idMateria = input("Ingrese el ID de la materia: ").strip().upper()

            if not idMateria:
                print("Debe ingresar el ID de la materia.")
                continue

            materia = materia_dao.buscar(idMateria)

            if materia:
                break

            print("No existe una materia con ese ID.")

        if cursoMateria_dao.existe(idCurso, idMateria):
            print("\nLa materia ya está asignada a este curso.\n")
            return

        if cursoMateria_dao.guardar(idCurso, idMateria):
            self.registrarAccion(f"Materia {materia.nombre} ({idMateria}) asignada al curso {curso.nombreCurso} ({idCurso})")
            print(f"\nMateria {materia.nombre} asignada al curso {curso.nombreCurso} correctamente\n")
        else:
            print("\nNo se pudo asignar la materia al curso\n")

    def verHorario(self, horario_dao):
        print("\n=============== HORARIO GENERAL ===============")
        horario = horario_dao.listarTodos()

        if not horario:
            print("\nNo hay cursos con horario registrado\n")
            return

        for item in horario:
            docente = item.nombreDocente if item.nombreDocente else "Sin asignar"
            aula = item.aula if item.aula is not None else "Aula virtual"

            print(f"Curso        : {item.nombreCurso} ({item.idCurso})")
            print(f"Modalidad    : {item.modalidad}")
            print(f"Jornada      : {item.jornada}")
            print(f"Docente      : {docente}")
            print(f"Día          : {item.dia}")
            print(f"Hora         : {item.horaInicio} - {item.horaFin}")
            print(f"Aula         : {aula}")
            print(f"Asignado por : {item.asignador}")
            print("-" * 50)


    def __str__(self):
        return f"Administrador | {self.nombre} | Sede: {self.sede} | Área: Nivelación"
