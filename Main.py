from Estudiante import Estudiante
from Docente import Docente
from Administrador import Administrador

usuarios = []
admin = Administrador( 
    "0001",
    "Administrador General",
    "admin@uleam.edu.ec",
    "admin123",
    "Matriz",
    "Nivelación",
    "0999999999"
)
usuarios.append(admin)

def Sistema():
    while True:
        print("----------SISTEMA NIVELACION----------")
        print("1. Registrar Estudiante")
        print("2. Registrar Docente")
        print("3. Listar Estudiantes")
        print("4. Listar Docentes")
        print("4. salir")
        opcion = input("Escoja una opción: ")

        if opcion == "1":
            cedula = input("Cédula: ")
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            contrasena = input("Contraseña: ")
            carrera = input("Carrera: ")

            estudiante = Estudiante(
                cedula,
                nombre,
                correo,
                contrasena,
                carrera
            )

            admin.registrarEstudiante(estudiante)
            usuarios.append(estudiante)

        elif opcion == "2":
            cedula = input("Cédula: ")
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            contrasena = input("Contraseña: ")
            titulo= input("Titulo Academico: ")
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
            usuarios.append(Docente)
        elif opcion == "3":
            admin.listarEstudiantes()
        elif opcion == "4":
            admin.listarDocentes()
        elif opcion == "5":
            print("Sistema Finalizado")
            break
        else:
            print("Opción inválida, intente de nuevo\n")


def IniciarSesion():
    while True:
        print("----------SISTEMA NIVELACION----------")
        print("1. iniciar Sesion")
        print("2. Recuperar Contraseña")
        print("3. salir")
        opcion = input("Escoja una opción: ")

        if opcion == "1":
            correo = input("Correo: ")
            contrasena = input("Contraseña: ")

            for usuario in usuarios:
                if usuario.correo == correo:
                    if usuario.iniciarSesion(contrasena):
                        print("Inicio de sesion exitoso")
                        redirigirUsuario(usuario)
                        return
                    else:
                        print("Contraseña incorrecta")
                        return
        
            print("usuario no encontrado")

        elif opcion == "2":
            #Recuperar_Contrasena()
            pass
        elif opcion == "3":
            print("Sistema Finalizado")
            break
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


def menuDocente():
   while True:
        print("\n===== MENÚ DOCENTE =====")
        print("1. Ver perfil")
        print("2. Ver cursos asignados")
        print("3. Ver estudiantes")
        print("4. Calificar estudiante")
        print("5. Crear evaluación")
        print("6. Ver cronograma")
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