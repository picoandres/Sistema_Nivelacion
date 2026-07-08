from UsuarioDAO import UsuarioDAO
from EstudianteDAO import EstudianteDAO
from DocenteDAO import DocenteDAO
from AdministradorDAO import AdministradorDAO
from CursoDAO import CursoDAO
from AsignacionCursoDAO import AsignacionCursoDAO
from CalificacionDAO import CalificacionDAO
from MateriaDAO import MateriaDAO
from CursoMateriaDAO import CursoMateriaDAO
from EvaluacionDAO import EvaluacionDAO
from HorarioDAO import HorarioDAO
from GestorNotificaciones import GestorNotificaciones
from GestorAulas import GestorAulas

class Sistema():
    def __init__(self):
        self.usuario_actual = None
        self.usuario_dao = UsuarioDAO()
        self.estudiante_dao = EstudianteDAO()
        self.docente_dao = DocenteDAO()
        self.administrador_dao = AdministradorDAO()
        self.curso_dao = CursoDAO()
        self.materia_dao = MateriaDAO()
        self.asignacionCurso_dao = AsignacionCursoDAO()
        self.cursoMateria_dao = CursoMateriaDAO()
        self.calificacion_dao = CalificacionDAO()
        self.evaluacion_dao = EvaluacionDAO()
        self.horario_dao = HorarioDAO()
        self.gestor = GestorNotificaciones()
        self.gestor_aulas = GestorAulas(self.horario_dao)

    def sistemaNivelacion(self):
        while True:
            print("----------SISTEMA NIVELACION----------")
            print("1. Iniciar sesión")
            print("2. Salir")

            opcion = input("Escoja una opción: ")

            if opcion == "1":
                correo = input("Correo: ")
                contrasena = input("Contraseña: ")
                
                usuario = self.usuario_dao.buscarUsuario(correo, contrasena)

                if usuario:
                    print(f"\nBienvenido {usuario.nombre}")
                    self.usuario_actual = usuario
                    self.redirigirUsuario(usuario)
                    return
                else:
                    print("Correo o contraseña incorrectos")

    
            elif opcion == "2":
                print("Tenga buen dia")
                break

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
            print("2. Cambiar contraseña")
            print("3. Crear curso")
            print("4. Registrar materia")
            print("5. Asignar docente a curso")
            print("6. Asignar estudiante a curso")
            print("7. Asignar materia a curso")
            print("8. Listar estudiantes")
            print("9. Listar docentes")
            print("10. Listar cursos")
            print("11. Ver horario")
            print("12. Ver historial")
            print("13. Cerrar sesión")

            opcion = input("Escoja una opción: ").strip()

            if opcion == "1":
                self.usuario_actual.verPerfil()

            elif opcion == "2":
                self.usuario_actual.cambiarContrasena()

            elif opcion == "3":
                self.usuario_actual.crearCurso(self.curso_dao, self.horario_dao, self.gestor_aulas)

            elif opcion == "4":
                self.usuario_actual.registrarMateria(self.materia_dao)

            elif opcion == "5":
                self.usuario_actual.asignarDocenteACurso(self.curso_dao,self.docente_dao, self.cursoMateria_dao)

            elif opcion == "6":
                self.usuario_actual.asignarEstudianteACurso(self.curso_dao,self.estudiante_dao,self.asignacionCurso_dao)

            elif opcion == "7":
                self.usuario_actual.asignarMateriaACurso(self.curso_dao,self.materia_dao,self.cursoMateria_dao)

            elif opcion == "8":
                self.usuario_actual.listarEstudiantes(self.estudiante_dao)

            elif opcion == "9":
                self.usuario_actual.listarDocentes(self.docente_dao)

            elif opcion == "10":
                self.usuario_actual.listarCursos(self.curso_dao)

            elif opcion == "11":
                self.usuario_actual.verHorario(self.horario_dao)

            elif opcion == "12":
                self.usuario_actual.mostrarHistorial()

            elif opcion == "13":
                print("Cerrando sesión\n")
                self.usuario_actual = None
                break

            else:
                print("\nOpción inválida, intente de nuevo\n")


    def menuDocente(self):
        while True:
            print("\n===== MENÚ DOCENTE =====")
            print("1. Ver perfil")
            print("2. Cambiar contraseña")
            print("3. Ver cursos asignados")
            print("4. Ver mi materia")
            print("5. Ver estudiantes")
            print("6. Calificar estudiante")
            print("7. Ver calificaciones")
            print("8. Editar calificación")
            print("9. Eliminar calificación")
            print("10. Crear evaluación")
            print("11. Ver evaluaciones")
            print("12. Editar evaluación")
            print("13. Eliminar evaluación")
            print("14. Ver horario")
            print("15. Cerrar sesión")

            opcion = input("Escoja una opción: ")

            if opcion == "1":
                self.usuario_actual.verPerfil(self.docente_dao)

            elif opcion == "2":
                self.usuario_actual.cambiarContrasena()

            elif opcion == "3":
                self.usuario_actual.verCursosAsignados(self.curso_dao)

            elif opcion == "4":
                self.usuario_actual.verMateria(self.docente_dao)

            elif opcion == "5":
                self.usuario_actual.verEstudiantes(self.curso_dao, self.asignacionCurso_dao)

            elif opcion == "6":
                self.usuario_actual.calificarEstudiante(self.curso_dao, self.asignacionCurso_dao, self.evaluacion_dao, self.calificacion_dao)

            elif opcion == "7":
                self.usuario_actual.verCalificaciones(self.curso_dao, self.calificacion_dao)

            elif opcion == "8":
                self.usuario_actual.editarCalificacion(self.curso_dao, self.calificacion_dao)

            elif opcion == "9":
                self.usuario_actual.eliminarCalificacion(self.curso_dao, self.calificacion_dao)

            elif opcion == "10":
                self.usuario_actual.crearEvaluacion(self.curso_dao, self.materia_dao, self.evaluacion_dao, self.asignacionCurso_dao)

            elif opcion == "11":
                self.usuario_actual.verEvaluaciones(self.evaluacion_dao)

            elif opcion == "12":
                self.usuario_actual.editarEvaluacion(self.evaluacion_dao)
            
            elif opcion == "13":
                self.usuario_actual.eliminarEvaluacion(self.evaluacion_dao)

            elif opcion == "14":
                self.usuario_actual.verHorario(self.horario_dao)

            elif opcion == "15":
                print("Cerrando sesión\n")
                self.usuario_actual = None
                break

            else:
                print("\nOpción inválida, intente de nuevo\n")


    def menuEstudiante(self):
        while True:
            print("\n===== MENÚ ESTUDIANTE =====")
            print("1. Ver perfil")
            print("2. Cambiar contraseña")
            print("3. Mis cursos")
            print("4. Ver notas")
            print("5. Ver horario")
            print("6. Cerrar sesión")

            opcion = input("Escoja una opción: ")

            if opcion == "1":
                self.usuario_actual.verPerfil()

            elif opcion == "2":
                self.usuario_actual.cambiarContrasena(self.usuario_dao)

            elif opcion == "3":
                self.usuario_actual.verCursos(self.asignacionCurso_dao)

            elif opcion == "4":
                self.usuario_actual.verNotas(self.calificacion_dao)

            elif opcion == "5":
                self.usuario_actual.verHorario(self.horario_dao)

            elif opcion == "6":
                print("Cerrando sesión\n")
                self.usuario_actual = None
                break
            
            else:
                print("\nOpción inválida, intente de nuevo\n")

sistema = Sistema()
sistema.sistemaNivelacion()