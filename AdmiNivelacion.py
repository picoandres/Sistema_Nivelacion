from Usuario import Usuario
from Docente import Docente
from Estudiante import Estudiante

class Administrador(Usuario):

    def __init__(self, cedula, nombre, correo, contrasena,
                 sede, areaResponsable, telefono):
        super().__init__(cedula, nombre, correo, contrasena)

        self.__sede = sede                        # encapsulado (privado)
        self.__areaResponsable = areaResponsable  # encapsulado (privado)
        self.telefono = telefono

        self.docentes = []
        self.estudiantes = []
        self.cursos = []

        self.__historialAcciones = []

    @property
    def sede(self):
        return self.__sede

    @sede.setter
    def sede(self, nueva_sede):
        if not nueva_sede or not isinstance(nueva_sede, str):
            raise ValueError("La sede debe ser un texto válido.")
        self.__sede = nueva_sede
        self.__registrarAccion(f"Sede actualizada a: {nueva_sede}")

    @property
    def areaResponsable(self):
        return self.__areaResponsable

    @areaResponsable.setter
    def areaResponsable(self, nueva_area):
        if not nueva_area or not isinstance(nueva_area, str):
            raise ValueError("El área responsable debe ser un texto válido.")
        self.__areaResponsable = nueva_area
        self.__registrarAccion(f"Área responsable actualizada a: {nueva_area}")

    def verPerfil(self):
        super().verPerfil()
        print(f"Sede          : {self.__sede}")
        print(f"Área          : {self.__areaResponsable}")
        print(f"Teléfono      : {self.telefono}")

    def registrarDocente(self, docente):
        """Agrega un Docente al sistema, validando que sea instancia correcta."""
        if not isinstance(docente, Docente):
            raise TypeError("Solo se pueden registrar objetos de tipo Docente.")

        for d in self.docentes:
            if d.cedula == docente.cedula:
                print(f"⚠ El docente con cédula {docente.cedula} ya está registrado.")
                return

        self.docentes.append(docente)
        self.__registrarAccion(f"Docente registrado: {docente.nombre} (C.I: {docente.cedula})")
        print(f" Docente '{docente.nombre}' registrado exitosamente.")

    def eliminarDocente(self, cedula):
        """Elimina un docente por cédula."""
        for docente in self.docentes:
            if docente.cedula == cedula:
                self.docentes.remove(docente)
                self.__registrarAccion(f"Docente eliminado: {docente.nombre} (C.I: {cedula})")
                print(f" Docente con cédula {cedula} eliminado.")
                return
        print(f" No se encontró un docente con cédula {cedula}.")

    def buscarDocente(self, cedula):
        for docente in self.docentes:
            if docente.cedula == cedula:
                return docente
        return None

    def listarDocentes(self):
        if not self.docentes:
            print("No hay docentes registrados en el sistema.")
            return
        print("\n──── DOCENTES REGISTRADOS ────")
        for i, d in enumerate(self.docentes, 1):
            print(f"  {i}. {d.nombre}  |  Especialidad: {d.especialidad}  |  C.I: {d.cedula}")
        print()

    def registrarEstudiante(self, estudiante):
        """Agrega un Estudiante al sistema."""
        if not isinstance(estudiante, Estudiante):
            raise TypeError("Solo se pueden registrar objetos de tipo Estudiante.")

        for e in self.estudiantes:
            if e.cedula == estudiante.cedula:
                print(f" El estudiante con cédula {estudiante.cedula} ya está registrado.")
                return

        self.estudiantes.append(estudiante)
        self.__registrarAccion(f"Estudiante registrado: {estudiante.nombre} (C.I: {estudiante.cedula})")
        print(f" Estudiante '{estudiante.nombre}' registrado exitosamente.")

    def eliminarEstudiante(self, cedula):
        for estudiante in self.estudiantes:
            if estudiante.cedula == cedula:
                self.estudiantes.remove(estudiante)
                self.__registrarAccion(f"Estudiante eliminado: {estudiante.nombre} (C.I: {cedula})")
                print(f" Estudiante con cédula {cedula} eliminado.")
                return
        print(f" No se encontró un estudiante con cédula {cedula}.")

    def buscarEstudiante(self, cedula):
        for estudiante in self.estudiantes:
            if estudiante.cedula == cedula:
                return estudiante
        return None

    def listarEstudiantes(self):
        """Muestra todos los estudiantes registrados."""
        if not self.estudiantes:
            print("No hay estudiantes registrados en el sistema.")
            return
        print("\n──── ESTUDIANTES REGISTRADOS ────")
        for i, e in enumerate(self.estudiantes, 1):
            print(f"  {i}. {e.nombre}  |  Carrera: {e.carrera}  |  Paralelo: {e.paralelo}  |  C.I: {e.cedula}")
        print()

    def crearCurso(self, curso):
        for c in self.cursos:
            if c.idCurso == curso.idCurso:
                print(f" El curso con ID '{curso.idCurso}' ya existe.")
                return

        self.cursos.append(curso)
        self.__registrarAccion(f"Curso creado: {curso.nombreCurso} (ID: {curso.idCurso})")
        print(f" Curso '{curso.nombreCurso}' creado exitosamente.")

    def asignarDocenteACurso(self, idCurso, cedula_docente):
        """Busca el curso y el docente, y realiza la asignación."""
        curso = self.__buscarCurso(idCurso)
        if curso is None:
            print(f" No se encontró el curso con ID '{idCurso}'.")
            return

        docente = self.buscarDocente(cedula_docente)
        if docente is None:
            print(f" No se encontró un docente con cédula {cedula_docente}.")
            return

        try:
            curso.asignarDocente(docente)
            docente.asignarCurso(curso)
            self.__registrarAccion(
                f"Docente '{docente.nombre}' asignado al curso '{curso.nombreCurso}'"
            )
            print(f"✔ Docente '{docente.nombre}' asignado al curso '{curso.nombreCurso}'.")
        except Exception as e:
            print(f" Error al asignar docente: {e}")

    def listarCursos(self):
        if not self.cursos:
            print("No hay cursos registrados en el sistema.")
            return
        print("\n──── CURSOS DE NIVELACIÓN ────")
        for i, c in enumerate(self.cursos, 1):
            docente_nombre = c.docente.nombre if c.docente else "Sin asignar"
            print(f"  {i}. [{c.idCurso}] {c.nombreCurso}  |  "
                  f"Modalidad: {c.modalidad}  |  Jornada: {c.jornada}  |  "
                  f"Docente: {docente_nombre}")
        print()

    def __registrarAccion(self, mensaje):
        self.__historialAcciones.append(mensaje)

    def mostrarHistorial(self):
        if not self.__historialAcciones:
            print("Sin acciones registradas.")
            return
        print(f"\n──── HISTORIAL DE ACCIONES — {self.nombre} ────")
        for i, accion in enumerate(self.__historialAcciones, 1):
            print(f"  {i}. {accion}")
        print()

    def ultimaAccion(self):
        if self.__historialAcciones:
            return self.__historialAcciones[-1]
        return "Sin registros"


    def __buscarCurso(self, idCurso):
        for curso in self.cursos:
            if curso.idCurso == idCurso:
                return curso
        return None

    def __str__(self):
        return (f"Administrador | {self.nombre} | Sede: {self.__sede} "
                f"| Área: {self.__areaResponsable}")    