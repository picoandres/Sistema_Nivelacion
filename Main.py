from CursoNivelacion import CursoNivelacion
from Estudiante import Estudiante
from HorarioFactory import obtener_fabrica_horario
from Docente import Docente
from Administrador import Administrador

usuarios = []
cursos = []

admin = Administrador( 
    "1305688402",
    "Juan Sendón",
    "admin@uleam.edu.ec",
    "A$EBM#20$26!1",
    "Administrador",
    "A-FCTV-1",
    "Matriz",
    "0999999999"
)
usuarios.append(admin)

def Sistema():
    while True:
        print("----------SISTEMA NIVELACION----------")
        print("1. Registrar Estudiante")
        print("2. Registrar Docente")
        print("3. Iniciar Sesión")
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

            admin.registrarEstudiante(estudiante)
            usuarios.append(estudiante)
            menuEstudiante()

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
                titulo,
                especialidad
            )

            admin.registrarDocente(estudiante)
            usuarios.append(docente)
            menuDocente()
            return docente

        elif opcion == "3":
            print("Redirigiendo a Inicio de Sesión")
            iniciarSesion()
        elif opcion == "4":
            print("Tenga buen dia")
            break
        else:
            print("Opción inválida, intente de nuevo\n")
        

def iniciarSesion():
    while True:
        print()
        print("----------INICIO DE SESION----------")
        print("1. Iniciar Sesión")
        print("2. Recuperar Contraseña")
        print("3. Regresar")

        opcion = input("Escoja una opción: ")

        if opcion == "1":
            correo = input("Correo: ")
            contrasena = input("Contraseña: ")
            for usuario in usuarios:
                if usuario.correo == correo:
                    if usuario.iniciarSesion(contrasena):
                        print("Inicio de sesión exitoso")
                        redirigirUsuario(usuario)
                        return
                    else:
                        print("Contraseña incorrecta")
                        return
        
            print("Usuario no encontrado")

        elif opcion == "2":
            usuario.recuperarContrasena()
        elif opcion == "3":
            Sistema()
        else:
            print("Opción inválida, intente de nuevo\n")


def redirigirUsuario(usuario):
    if usuario.rol == "Administrador":
        menuAdministrador()
    elif usuario.rol == "Docente":
        menuDocente()
    elif usuario.rol == "Estudiante":
        menuEstudiante()
    else:
        print("Rol no reconocido")


def menuAdministrador():
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
            aula= input("Aula: ")

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
                    jornada
                )
                
                curso.horario = horario

                admin.__registrarAccion()
                admin.crearCurso(curso)
                cursos.append(curso)
                print(f"Curso '{nombreCurso}' creado y asignado a la jornada {jornada}")
            except Exception as e:
                print("Error al crear el curso: ", e)

        elif opcion == "2":
            """
            print("-----ASIGNAR DOCENTE-----")
            idCurso = input("ingrese el id del curso: ")
            cedula_docente = input("ingrese la cedula del docente: ")
            cursoObj = next((c for c in cursos if c.idCurso == cedula_docente).none)
            docenteObj = next(())
            """
            
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

Sistema()
