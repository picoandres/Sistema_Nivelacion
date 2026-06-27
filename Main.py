from CursoNivelacion import CursoNivelacion
from Estudiante import Estudiante
from HorarioFactory import obtener_fabrica_horario
from Docente import Docente
from Administrador import Administrador
from Usuario import Usuario

#importacion de los objetos de SQL
from SistemaDAO import EstudianteDAO, DocenteDAO

#inicializacion de DAOs:
estudiante_dao = EstudianteDAO()
docente_dao = DocenteDAO()
#gestor = GestorAulas()
admin = Administrador( 
    "1305688402",
    "Juan Sendón",
    "admin@uleam.edu.ec",
    "A$EBM#20$26!1",
    "Administrador",
    "A-FCTV-1",
    "Matriz",
    "0999999999",
)

class Sistema():
    def __init__(self):
        self.usuarios = []
        self.cursos = []
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
                    carrera,
                    paralelo
                    )

                if estudiante_dao.guardar(estudiante):
                    admin.registrarEstudiante(estudiante)
                    self.usuarios.append(estudiante)
                    print("Estudiante guardado correctamente")
                else:
                    print("Error al guardar estudiante")

            if opcion == "2":
                cedula = input("Cédula: ")
                nombre = input("Nombre: ")
                correo = input("Correo: ")
                contrasena = input("Contraseña: ")
                titulo = input("Título Académico: ")
                especialidad = input("Especialidad: ")
                anosExperiencia = int(input("Años de experiencia: "))
            
                docente = Docente(
                    cedula,
                    nombre,
                    correo,
                    contrasena,
                    "Docente",
                    titulo,
                    especialidad,
                    anosExperiencia
                )

                if docente_dao.guardar(docente):
                    admin.registrarDocente(docente)
                    self.usuarios.append(docente)
                    print("Docente guardado correctamente")
                else:
                    print("Error al guardar docente")

            elif opcion == "3":
                Sistema.iniciarSesion()

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
            print("3. Regresar")

            opcion = input("Escoja una opción: ")

            if opcion == "1":
                correo = input("Correo: ")
                contrasena = input("Contraseña: ")
                
                for usuario in self.usuarios:
                    if usuario.autenticar(correo, contrasena):
                        self.redirigirUsuario(usuario)
                        return

            elif opcion == "2":
                pass

            elif opcion == "3":
                Sistema.sistema_nivelacion()
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
            print("1. Crear curso")
            print("2. Asignar docente a curso")
            print("3. Listar estudiantes")
            print("4. Listar docentes")
            print("5. Listar cursos")
            print("6. Ver historial")
            print("7. Salir")

            opcion = input("Escoja una opción: ")

            if opcion == "1":
                print("CREAR CURSO:")
                idCurso = input("ID del curso: ")
                nombreCurso = input("Nombre del curso: ")
                modalidad = input("Modalidad: ")
                jornada = input("Jornada: ")
                dia = input("Dia: ")
                aula = input("Aula: ")

                try:

                    fabrica = obtener_fabrica_horario(jornada)
                    horario = fabrica.crear_horario(
                        dia,
                        aula,
                    )

                    curso = CursoNivelacion(
                        idCurso,
                        nombreCurso,
                        modalidad,
                        jornada,
                        horario
                    )

                    admin.registrarAccion()
                    admin.crearCurso(curso)
                    self.cursos.append(curso)
                    print(f"Curso '{nombreCurso}' creado y asignado a la jornada {jornada}")
                except Exception as e:
                    print("Error al crear el curso: ", e)

            elif opcion == "2":
                print("-----ASIGNAR DOCENTE-----")
                nombreDocente = input("ingrese el nombre del docente: ")
                curso.asignar_docente(nombreDocente)

            elif opcion == "3":
                admin.listarEstudiantes()
            elif opcion == "4":
                admin.listarDocentes()
            elif opcion == "5":
                print("LISTAR CURSOS ACTIVOS")
                admin.listarCursos()
            elif opcion == "6":
                admin.mostrarHistorial()
            elif opcion == "7":
                print("Sistema Finalizado")
                break
            else:
                print("Opción inválida, intente de nuevo\n")


    def menuDocente():
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
                pass
            elif opcion == "2":
                pass
            elif opcion == "3":
                pass
            elif opcion == "4":
                pass
            elif opcion == "5":
                pass
            elif opcion == "6":
                pass
            elif opcion == "7":
                pass
            elif opcion == "8":
                print("Sistema Finalizado")
                break
            else:
                print("Opción inválida, intente de nuevo\n")

    def menuEstudiante():
        while True:
            print("\n===== MENÚ ESTUDIANTE =====")
            print("1. Ver perfil")
            print("2. Ver notas")
            print("3. Ver asistencia")
            print("4. Subir documento")
            print("5. Ver documentos")
            print("6. Recuperar contraseña")
            print("7. Cerrar sesión")

            opcion = input("Escoja una opción: ")

            if opcion == "1":
                pass
            elif opcion == "2":
                pass
            elif opcion == "3":
                pass
            elif opcion == "4":
                pass
            elif opcion == "5":
                pass
            elif opcion == "6":
                pass
            elif opcion == "7":
                print("Sistema Finalizado")
                break
            else:
                print("Opción inválida, intente de nuevo\n")
                
Sistema.sistemaNivelacion()