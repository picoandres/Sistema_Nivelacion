from CursoNivelacion import CursoNivelacion
from Estudiante import Estudiante
from HorarioFactory import obtenerFabricaHorario
from Docente import Docente
from SistemaDAO import UsuarioDAO, EstudianteDAO, DocenteDAO, AdministradorDAO, CursoDAO
from GestorNotificaciones import GestorNotificaciones

#inicializacion de DAOs:
usuario_dao = UsuarioDAO()
estudiante_dao = EstudianteDAO()
docente_dao = DocenteDAO()
administrador_dao = AdministradorDAO()
curso_dao = CursoDAO()

#Patrón de comportamiento Observer:
gestor = GestorNotificaciones()

class Sistema():
    def __init__(self):
        self.usuario_actual = None

    def sistemaNivelacion(self):
        while True:
            print("----------SISTEMA NIVELACION----------")
            print("1. Registrar Estudiante")
            print("2. Registrar Docente")
            print("3. Iniciar sesión")
            print("4. Salir")

            opcion = input("Escoja una opción: ")

            if opcion == "1":
                cedula = input("Cédula: ")
                nombre = input("Nombre: ")
                correo = input("Correo: ")
                contrasena = input("Contraseña: ")
                carrera = input("Carrera: ")
                paralelo = input("Paralelo: ")
                
                estudiante = Estudiante(
                    cedula,
                    nombre,
                    correo,
                    contrasena,
                    "Estudiante",
                    carrera,
                    paralelo
                    )

                if estudiante_dao.guardar(estudiante):
                    gestor.agregar_observador(estudiante)
                    print("Estudiante guardado en BD correctamente\n")
                    gestor.notificar_Todos("Se registró un nuevo estudiante")
                    gestor.eliminar_observador(estudiante)
                else:
                    print("Error al guardar estudiante en BD\n")

            elif opcion == "2":
                cedula = input("Cédula: ")
                nombre = input("Nombre: ")
                correo = input("Correo: ")
                contrasena = input("Contraseña: ")
                titulo = input("Título Académico: ")
                especialidad = input("Especialidad: ")
            
                docente = Docente(
                    cedula,
                    nombre,
                    correo,
                    contrasena,
                    "Docente",
                    titulo,
                    especialidad
                )

                if docente_dao.guardar(docente):
                    gestor.agregar_observador(docente)
                    print("Docente guardado en BD correctamente\n")
                    gestor.notificar_Todos("Se registró un nuevo Docente")
                    gestor.eliminar_observador(docente)
                else:
                    print("Error al guardar docente en BD\n")

            elif opcion == "3":
                sistema.iniciarSesion()

            elif opcion == "4":
                print("Tenga buen dia")
                break
            else:
                print("Opción inválida, intente de nuevo\n")
        

    def iniciarSesion(self):
        while True:
            print()
            print("----------INICIO DE SESIÓN----------")
            print("1. Iniciar sesión")
            print("2. Recuperar contraseña")
            print("3. Regresar a menú principal")
            print()

            opcion = input("Escoja una opción: ")

            if opcion == "1":
                correo = input("Correo: ")
                contrasena = input("Contraseña: ")
                
                usuario = usuario_dao.buscarUsuario(correo, contrasena)

                if usuario:
                    print(f"\nBienvenido {usuario.nombre}")
                    self.usuario_actual = usuario
                    self.redirigirUsuario(usuario)
                    return
                else:
                    print("Correo o contraseña incorrectos")

            elif opcion == "2":
                pass

            elif opcion == "3":
                return            
            
            else:
                print("Opción inválida, intente de nuevo\n")


    def redirigirUsuario(self, usuario):
        if usuario.rol == "Administrador":
            self.menuAdministrador()
        elif usuario.rol == "Docente":
            self.menuDocente()
        elif usuario.rol == "Estudiante":
            self.menuEstudiante()
        else:
            print("Rol no reconocido")


    def menuAdministrador(self):
        while True:
            print("\n===== MENÚ ADMINISTRADOR =====")
            print("1. Ver perfil")
            print("2. Crear curso")
            print("3. Asignar docente a curso")
            print("4. Listar estudiantes")
            print("5. Listar docentes")
            print("6. Listar cursos")
            print("7. Ver historial")
            print("8. Salir")

            opcion = input("Escoja una opción: ")

            if opcion == "1":
                self.usuario_actual.verPerfil()

            elif opcion == "2":
                idCurso = input("ID del curso: ")
                nombreCurso = input("Nombre del curso: ")
                modalidad = input("Modalidad: ")
                jornada = input("Jornada: ")
                dia = input("Dia: ")
                aula = input("Aula: ")

                try:
                    fabrica = obtenerFabricaHorario(jornada)
                    horario = fabrica.crearHorario(
                        dia,
                        aula,
                        self.usuario_actual.nombre
                    )

                    curso = CursoNivelacion(
                        idCurso,
                        nombreCurso,
                        modalidad,
                        jornada,
                        horario
                    )

                    self.usuario_actual.registrarAccion(f"Se creó el curso: {nombreCurso}")
                    if curso_dao.guardar(curso):
                        print("Curso creado exitosamente")
                    else:
                        print("No se pudo crear el curso")

                except Exception as e:
                    print("Error al crear el curso: ", e)
            
            elif opcion == "3":
                print("-----ASIGNAR DOCENTE-----")
                idCurso = input("ID del Curso: ")
                cedulaDocente = input("Cédula del docente: ")
                curso_dao.asignarDocente(idCurso, cedulaDocente)
                print("Docente asignado")

            elif opcion == "4":
                estudiantes = estudiante_dao.listar()
                print("\n----- ESTUDIANTES -----")
                for e in estudiantes:
                    print(f"{e.nombre} - {e.carrera} - {e.paralelo}")

            elif opcion == "5":
                docentes = docente_dao.listar()
                print("\n----- DOCENTES -----")
                for d in docentes:
                    print(f"{d.nombre} - {d.titulo}")

            elif opcion == "6":
                cursos = curso_dao.listar()
                self.usuario_actual.mostrarCursos(cursos)

            elif opcion == "7":
                pass

            elif opcion == "8":
                print("Cerrando sesión\n")
                break

            else:
                print("Opción inválida, intente de nuevo")


    def menuDocente(self):
        while True:
            print("\n===== MENÚ DOCENTE =====")
            print("1. Ver perfil")
            print("2. Ver cursos asignados")
            print("3. Ver Materias Disponibles")
            print("4. Ver estudiantes")
            print("5. Calificar estudiante")
            print("6. Crear evaluación")
            print("7. Ver cronograma")
            print("8. Cerrar sesión")

            opcion = input("Escoja una opción: ")

            if opcion == "1":
                self.usuario_actual.verPerfil()

            elif opcion == "2":
                cursos = curso_dao.buscarPorDocente(self.usuario_actual.cedula)
                self.usuario_actual.mostrarCursosAsignados(cursos)

            elif opcion == "3":
                pass

            elif opcion == "4":
                pass

            elif opcion == "5":
                pass

            elif opcion == "6":
                titulo_evaluacion = input("Título de evaluación: ")
                descripcion = input("Descripción: ")
                self.usuario_actual.crearEvaluacion(titulo_evaluacion, descripcion)

            elif opcion == "7":
                pass

            elif opcion == "8":
                print("Cerrando sesión\n")
                break

            else:
                print("Opción inválida, intente de nuevo")

    def menuEstudiante(self):
        while True:
            print("\n===== MENÚ ESTUDIANTE =====")
            print("1. Ver perfil")
            print("2. Ver notas")
            print("3. Ver asistencia")
            print("4. Subir documento")
            print("5. Ver documentos")
            print("6. Cambiar contraseña")
            print("7. Cerrar sesión")

            opcion = input("Escoja una opción: ")

            if opcion == "1":
                self.usuario_actual.verPerfil()

            elif opcion == "2":
                self.usuario_actual.verNotas()

            elif opcion == "3":
                pass
                
            elif opcion == "4":
                nombre = input("Nombre del documento: ")
                tipo = input("Tipo de documento: ")
                self.usuario_actual.subir_documentos(nombre, tipo)

            elif opcion == "5":
                self.usuario_actual.verDocumentosSubidos()

            elif opcion == "6":
                nueva = input("Ingrese su nueva contraseña: ")
                self.usuario_actual.cambiarContrasena(nueva)

            elif opcion == "7":
                print("Cerrando sesión\n")
                break
            else:
                print("Opción inválida, intente de nuevo")

sistema = Sistema()
sistema.sistemaNivelacion()