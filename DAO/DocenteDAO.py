from BaseDeDatos import ConexionSQLServer # DEBE MODIFICARSE #
from Modelos.Docente import Docente
from Modelos.TipoDocente import Titular, Suplente
from Modelos.TiempoContrato import TiempoCompleto, TiempoParcial
from Modelos.Materia import Materia

class DocenteDAO:
    def __init__(self):
        self.db = ConexionSQLServer()
        
    def crearTipoDocente(self, valor):
        if valor == "Suplente":
            return Suplente()
        return Titular()

    def crearTiempoContrato(self, valor):
        if valor == "Tiempo Parcial":
            return TiempoParcial()
        return TiempoCompleto()


    def existe(self, cedula):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:
            sql = """
            SELECT 1
            FROM Docente
            WHERE cedula = ?
            """
            self.db.cursor.execute(sql, (cedula,))
            return self.db.cursor.fetchone() is not None

        except Exception as e:
            print("Error al verificar docente:", e)
            return False

        finally:
            self.db.cerrarConexion()


    def guardar(self, docente: Docente):
        conexion = self.db.conectar()
        if not conexion:
            return False
        
        try:
            cedula = str(docente.cedula).strip()
            nombre = str(docente.nombre).strip()
            correo = str(docente.correo).strip()
            contrasena = str(docente.obtenerContrasena()).strip()
            rol = str(docente.rol).strip()
            profesion = str(docente.profesion).strip()
            especialidad = str(docente.especialidad).strip()
            idMateria = str(docente.idMateria).strip() if docente.idMateria is not None else ""

            if not cedula or not nombre or not correo or not contrasena or not rol:
                print("Los datos básicos del docente son obligatorios")
                return False

            if not profesion or not especialidad or not idMateria:
                print("Profesión, especialidad e idMateria son obligatorios")
                return False

            if rol != "Docente":
                print("El rol del usuario debe ser Docente")
                return False

            sql_cedula = """
            SELECT 1
            FROM Usuario
            WHERE cedula = ?
            """
            self.db.cursor.execute(sql_cedula, (cedula,))
            if self.db.cursor.fetchone() is not None:
                print("Ya existe un usuario con esa cédula")
                return False

            sql_correo = """
            SELECT 1
            FROM Usuario
            WHERE correo = ?
            """
            self.db.cursor.execute(sql_correo, (correo,))
            if self.db.cursor.fetchone() is not None:
                print("Ya existe un usuario con ese correo")
                return False

            sql_materia = """
            SELECT 1
            FROM Materia
            WHERE idMateria = ?
            """
            self.db.cursor.execute(sql_materia, (idMateria,))
            if self.db.cursor.fetchone() is None:
                print("No existe una materia con ese ID")
                return False

            sql_usuario ="""
             INSERT INTO Usuario
            (
                cedula,
                nombre,
                correo,
                contrasena,
                rol
            )

            VALUES (?, ?, ?, ?, ?)
            """
            self.db.cursor.execute(sql_usuario, (
                docente.cedula,
                docente.nombre,
                docente.correo,
                docente.contrasena,
                docente.rol
            ))

            tipo_docente = docente.obtenerTipoDocente()
            tiempo_contrato = docente.obtenerTiempoContrato()

            sql_docente ="""
            INSERT INTO Docente
            (
                cedula,
                profesion,
                especialidad,
                tipoDocente,
                tiempoContrato,
                idMateria
            )

            VALUES (?, ?, ?, ?, ?, ?)
            """
            self.db.cursor.execute(sql_docente, (
                docente.cedula,
                docente.profesion,
                docente.especialidad,
                tipo_docente,
                tiempo_contrato,
                docente.idMateria
            ))
            conexion.commit()
            return True
        
        except Exception as e:
            conexion.rollback()
            print(f"Error al guardar docente en BD: {e}")
            return False
        
        finally:
            self.db.cerrarConexion()
    

    def buscar(self, cedula):
        conexion = self.db.conectar()
        if not conexion:
            return None

        try:
            sql = """
            SELECT
                u.cedula,
                u.nombre,
                u.correo,
                u.contrasena,
                u.rol,
                d.profesion,
                d.especialidad,
                d.tipoDocente,
                d.tiempoContrato,
                d.idMateria
            FROM Usuario u
            INNER JOIN Docente d
                ON u.cedula = d.cedula
            WHERE u.cedula = ?
            """

            self.db.cursor.execute(sql, (cedula,))
            fila = self.db.cursor.fetchone()

            if fila is None:
                return None

            tipo_docente = self.crearTipoDocente(fila.tipoDocente)
            tiempo_contrato = self.crearTiempoContrato(fila.tiempoContrato)

            docente = Docente(
                fila.cedula,
                fila.nombre,
                fila.correo,
                fila.contrasena,
                fila.rol,
                fila.profesion,
                fila.especialidad,
                tipo_docente,
                tiempo_contrato,
                fila.idMateria
            )

            return docente

        except Exception as e:
            print("Error al buscar docente:", e)
            return None

        finally:
            self.db.cerrarConexion()


    def listar(self):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:
            sql = """
            SELECT
                u.cedula,
                u.nombre,
                u.correo,
                u.contrasena,
                u.rol,
                d.profesion,
                d.especialidad,
                d.tipoDocente,
                d.tiempoContrato,
                d.idMateria
            FROM Usuario u
            INNER JOIN Docente d
                ON u.cedula = d.cedula
            ORDER BY u.nombre
            """

            self.db.cursor.execute(sql)
            resultados = self.db.cursor.fetchall()

            docentes = []
            for fila in resultados:
                tipo_docente = self.crearTipoDocente(fila.tipoDocente)
                tiempo_contrato = self.crearTiempoContrato(fila.tiempoContrato)

                docente = Docente(
                    fila.cedula,
                    fila.nombre,
                    fila.correo,
                    fila.contrasena,
                    fila.rol,
                    fila.profesion,
                    fila.especialidad,
                    tipo_docente,
                    tiempo_contrato,
                    fila.idMateria
                )

                docentes.append(docente)

            return docentes

        except Exception as e:
            print("Error al listar docentes:", e)
            return []

        finally:
            self.db.cerrarConexion()


    def asignarMateria(self, cedulaDocente, idMateria):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:
            cedulaDocente = str(cedulaDocente).strip()

            if not cedulaDocente:
                print("La cédula del docente es obligatoria")
                return False
            
            idMateria = str(idMateria).strip()

            if not idMateria:
                print("El ID de la materia es obligatoria")
                return False

            # Verificar que el docente exista en la tabla Docente
            sql_docente = """
            SELECT idMateria
            FROM Docente
            WHERE cedula = ?
            """
            self.db.cursor.execute(sql_docente, (cedulaDocente,))
            docente = self.db.cursor.fetchone()

            if docente is None:
                print("No existe un docente con esa cédula")
                return False

            # Verificar que la materia exista
            sql_materia = """
            SELECT 1
            FROM Materia
            WHERE idMateria = ?
            """
            self.db.cursor.execute(sql_materia, (idMateria,))
            if self.db.cursor.fetchone() is None:
                print("No existe una materia con ese ID")
                return False

            # Si ya tiene esa materia, no hacer nada
            if docente.idMateria == idMateria:
                print("Ese docente ya tiene asignada esa materia")
                return False

            # Validar si el docente ya tiene una materia asignada
            sql_materia_asignada = """
            SELECT idMateria
            FROM Docente
            WHERE cedulaDocente = ?
            """
            self.db.cursor.execute(sql_materia_asignada, (cedulaDocente,))
            if self.db.cursor.fetchone() is not None:
                print("No se puede cambiar la materia del docente porque ya tiene cursos asignados")
                return False

             # Validar si ya tiene evaluaciones registradas
            sql_evaluaciones = """
            SELECT 1
            FROM Evaluacion e
            INNER JOIN Curso c
                ON e.idCurso = c.idCurso
            WHERE c.cedulaDocente = ?
            """
            self.db.cursor.execute(sql_evaluaciones, (cedulaDocente,))
            if self.db.cursor.fetchone() is not None:
                print("No se puede cambiar la materia del docente porque ya tiene evaluaciones registradas")
                return False

            # Para ahora sí asignar la materia al docente
            sql_update = """
            UPDATE Docente
            SET idMateria = ?
            WHERE cedula = ?
            """
            self.db.cursor.execute(sql_update, (idMateria, cedulaDocente))

            if self.db.cursor.rowcount == 0:
                print("No se pudo asignar la materia al docente")
                return False

            conexion.commit()
            return True

        except Exception as e:
            conexion.rollback()
            print("Error al asignar materia al docente:", e)
            return False

        finally:
            self.db.cerrarConexion()


    def listarConMateria(self):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:
            sql = """
            SELECT
                u.cedula,
                u.nombre,
                u.correo,
                d.profesion,
                d.especialidad,
                d.tipoDocente,
                d.tiempoContrato,
                d.idMateria,
                m.nombre AS nombreMateria
            FROM Docente d
            INNER JOIN Usuario u
                ON d.cedula = u.cedula
            LEFT JOIN Materia m
                ON d.idMateria = m.idMateria
            ORDER BY u.nombre
            """

            self.db.cursor.execute(sql)
            return self.db.cursor.fetchall()

        except Exception as e:
            print("Error al listar docentes con materia:", e)
            return []

        finally:
            self.db.cerrarConexion()


    def buscarMateriaDocente(self, cedulaDocente):
        conexion = self.db.conectar()
        if not conexion:
            return None

        try:
            sql = """
            SELECT
                d.idMateria,
                m.nombre,
                m.descripcion,
                m.horas
            FROM Docente d
            INNER JOIN Materia m
                ON d.idMateria = m.idMateria
            WHERE d.cedula = ?
            """

            self.db.cursor.execute(sql, (cedulaDocente,))
            fila = self.db.cursor.fetchone()
            
            if fila is None:
                return None
            
            return Materia(
                fila.idMateria,
                fila.nombre,
                fila.descripcion,
                fila.horas
            )

        except Exception as e:
            print("Error al buscar la materia del docente:", e)
            return None

        finally:
            self.db.cerrarConexion()