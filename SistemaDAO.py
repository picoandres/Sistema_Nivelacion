from BaseDeDatos import ConexionSQLServer
from Estudiante import Estudiante
from Docente import Docente
from Administrador import Administrador
from CursoNivelacion import CursoNivelacion

class UsuarioDAO:
    def __init__(self):
        self.db = ConexionSQLServer()
    def buscarUsuario(self, correo, contrasena):
        conexion = self.db.conectar()
        if not conexion:
            return None
        
        try:
            sql = """
            SELECT *
            FROM Usuario
            WHERE correo = ? AND contrasena = ?
            """

            self.db.cursor.execute(sql, (correo, contrasena))

            usuario = self.db.cursor.fetchone()
        
            if usuario is None:
                return None

            cedula = usuario.cedula
            nombre = usuario.nombre
            correo = usuario.correo
            contrasena = usuario.contrasena
            rol = usuario.rol

            if rol == "Estudiante":

                sql = """
                SELECT carrera, paralelo
                FROM Alumnos
                WHERE cedula = ?
                """

                self.db.cursor.execute(sql, (cedula,))
                datos = self.db.cursor.fetchone()

                return Estudiante(
                    cedula,
                    nombre,
                    correo,
                    contrasena,
                    rol,
                    datos.carrera,
                    datos.paralelo
                )

            elif rol == "Docente":

                sql = """
                SELECT titulo, especialidad
                FROM Docente
                WHERE cedula = ?
                """

                self.db.cursor.execute(sql, (cedula,))
                datos = self.db.cursor.fetchone()

                return Docente(
                    cedula,
                    nombre,
                    correo,
                    contrasena,
                    rol,
                    datos.titulo,
                    datos.especialidad,
                )

            # ===== ADMINISTRADOR =====
            elif rol == "Administrador":

                sql = """
                SELECT id_admin, sede, telefono
                FROM Administrador
                WHERE cedula = ?
                """

                self.db.cursor.execute(sql, (cedula,))
                datos = self.db.cursor.fetchone()

                return Administrador(
                    cedula,
                    nombre,
                    correo,
                    contrasena,
                    rol,
                    datos.id_admin,
                    datos.sede,
                    datos.telefono
                )
            return None

        except Exception as e:
            print("Error: ", e)
            return None

        finally:
            self.db.cerrarConexion()        


class EstudianteDAO:
    def __init__(self):
        self.db = ConexionSQLServer()

    def guardar(self, estudiante: Estudiante):
        conexion = self.db.conectar()
        if not conexion:
            return False
        
        try:
            #insertar en Usuario (padre)
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
                estudiante.cedula, estudiante.nombre, estudiante.correo,
                estudiante.contrasena, estudiante.rol
            ))
            #Insertar Estudiante (Hijo)
            sql_estudiante ="""
            INSERT INTO Alumnos
            (
                cedula,
                carrera,
                paralelo
            )
            VALUES (?, ?, ?)
            """
            self.db.cursor.execute(sql_estudiante, (
                estudiante.cedula, estudiante.carrera, estudiante.paralelo,
            ))
            conexion.commit()
            return True
        
        except Exception as e:
            conexion.rollback()
            print(f"Error al guardar estudiante en BD: {e}")
            return False
        
        finally:
            self.db.cerrarConexion()

    def listar(self):
        conexion = self.db.conectar()
        if not conexion:
            return []
        
        try:
            sql = """
            SELECT U.cedula,
               U.nombre,
               U.correo,
               A.carrera,
               A.paralelo
            FROM Usuario U
            INNER JOIN Alumnos A
            ON U.cedula = A.cedula
            """

            self.db.cursor.execute(sql)

            return self.db.cursor.fetchall()
        
        except Exception as e:
            print("Error: ", e)
            return []
        
        finally:
            self.db.cerrarConexion()


class DocenteDAO:
    def __init__(self):
        self.db = ConexionSQLServer()
        
    def guardar(self, docente: Docente):
        conexion = self.db.conectar()
        if not conexion:
            return False
        
        try:
            #insertar en Usuario (padre)
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
                docente.cedula, docente.nombre, docente.correo,
                docente.contrasena, docente.rol
            ))
            #Insertar Docente (Hijo)
            sql_docente ="""
            INSERT INTO Docente
            (
                cedula,
                titulo,
                especialidad
            )

            VALUES (?, ?, ?)
            """
            self.db.cursor.execute(sql_docente, (
                docente.cedula, docente.titulo, docente.especialidad
            ))
            conexion.commit()
            return True
        
        except Exception as e:
            conexion.rollback()
            print(f"Error al guardar docente en BD: {e}")
            return False
        
        finally:
            self.db.cerrarConexion()
    
    def listar(self):
        conexion = self.db.conectar()

        if not conexion:
            return []

        try:
            sql = """
            SELECT U.cedula,
               U.nombre,
               U.correo,
               D.titulo,
               D.especialidad
            FROM Usuario U
            INNER JOIN Docente D
            ON U.cedula = D.cedula
            """

            self.db.cursor.execute(sql)

            return self.db.cursor.fetchall()

        except Exception as e:
            print("Error: ", e)
            return []

        finally:
            self.db.cerrarConexion()


class AdministradorDAO:
    def __init__(self):
        self.db = ConexionSQLServer()
    
    def buscarPorCedula(self, cedula):
        conexion = self.db.conectar()
        if not conexion:
            return None
        
        try:
            sql = """
            SELECT
                U.cedula,
                U.nombre,
                U.correo,
                U.contrasena,
                U.rol,
                A.id_admin,
                A.sede,
                A.telefono
            FROM Usuario U
            INNER JOIN Administrador A
                ON U.cedula = A.cedula
            WHERE U.cedula = ?
            """

            self.db.cursor.execute(sql, (cedula,))

            datos = self.db.cursor.fetchone()
            if datos is None:
                return None

            return Administrador(
                datos.cedula,
                datos.nombre,
                datos.correo,
                datos.contrasena,
                datos.rol,
                datos.id_admin,
                datos.sede,
                datos.telefono
            )

        except Exception as e:
            print("Error:", e)
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
                U.cedula,
                U.nombre,
                U.correo,
                A.id_admin,
                A.sede,
                A.telefono
            FROM Usuario U
            INNER JOIN Administrador A
                ON U.cedula = A.cedula
            """

            self.db.cursor.execute(sql)
            return self.db.cursor.fetchall()

        except Exception as e:
            print("Error:", e)
            return []

        finally:
            self.db.cerrarConexion()


class CursoDAO:
    def __init__(self):
        self.db = ConexionSQLServer()
    
    def guardar(self, curso):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:
            sql = """
            INSERT INTO Curso
            (
                idCurso,
                nombreCurso,
                modalidad,
                jornada,
                cedulaDocente
            )

            VALUES (?, ?, ?, ?, ?)
            """

            cedula_docente = None
            if curso.docente is not None:
                cedula_docente = curso.docente.cedula

            self.db.cursor.execute(sql, (
                curso.idCurso,
                curso.nombreCurso,
                curso.modalidad,
                curso.jornada,
                cedula_docente
            ))

            conexion.commit()
            return True

        except Exception as e:
            conexion.rollback()
            print("Error al guardar curso en BD:", e)
            return False

        finally:
            self.db.cerrarConexion()

    def listar(self):
        conexion = self.db.conectar()
        if not conexion:
            return []
        
        try:
            sql = """
            SELECT
                c.idCurso,
                c.nombreCurso,
                c.modalidad,
                c.jornada,
                c.cedulaDocente,
                u.nombre AS nombreDocente
            FROM Curso c
            LEFT JOIN Docente d
                ON c.cedulaDocente = d.cedula
            LEFT JOIN Usuario u
                ON d.cedula = u.cedula
            ORDER BY c.idCurso;
            """

            self.db.cursor.execute(sql)
            return self.db.cursor.fetchall()
        
        except Exception as e:
            print("Error: ", e)
            return []
        
        finally:
            self.db.cerrarConexion()

    def buscar(self, idCurso):
        conexion = self.db.conectar()
        if not conexion:
            return None
        
        try:
            sql = """
            SELECT *
            FROM Curso
            WHERE idCurso = ?
            """

            self.db.cursor.execute(sql, idCurso)
            return self.db.cursor.fetchone()
        
        except Exception as e:
            print("Error: ", e)
            return None
        
        finally:
            self.db.cerrarConexion()

    def asignarDocente(self, idCurso, cedulaDocente):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:
            sql = """
            UPDATE Curso
            SET cedulaDocente = ?
            WHERE idCurso = ?
            """

            self.db.cursor.execute(sql, (cedulaDocente, idCurso))
            conexion.commit()
            return True
        
        except Exception as e:
            print("Error: ", e)
            return False
        
        finally:
            self.db.cerrarConexion()

    def listarCursosDocente(self, cedulaDocente):
        conexion = self.db.conectar()
        if not conexion:
            return []
        
        try:
            sql = """
            SELECT *
            FROM Curso
            WHERE cedulaDocente = ?
            """

            self.db.cursor.execute(sql, cedulaDocente,)
            return self.db.cursor.fetchall()
        except Exception as e:
            print("Error: ", e)
            return []
        
        finally:
            self.db.cerrarConexion()

    def buscarPorDocente(self, cedulaDocente):
        conexion = self.db.conectar()
        if not conexion:
            return []

        try:
            sql = """
            SELECT
                idCurso,
                nombreCurso,
                modalidad,
                jornada
            FROM Curso
            WHERE cedulaDocente = ?
            ORDER BY idCurso
            """

            self.db.cursor.execute(sql, (cedulaDocente,))
            return self.db.cursor.fetchall()

        except Exception as e:
            print("Error:", e)
            return []

        finally:
            self.db.cerrarConexion()