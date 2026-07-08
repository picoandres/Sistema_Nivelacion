from BaseDeDatos import ConexionSQLServer
from CursoNivelacion import CursoNivelacion

class CursoDAO:
    def __init__(self):
        self.db = ConexionSQLServer()
    

    def guardar(self, curso: CursoNivelacion):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:
            if curso is None:
                print("No se recibió un curso válido")
                return False
            
            if not curso.idCurso or not str(curso.idCurso).strip():
                print("El ID del curso es obligatorio")
                return False

            if not curso.nombreCurso or not str(curso.nombreCurso).strip():
                print("El nombre del curso es obligatorio")
                return False
            
            if not curso.modalidad or not str(curso.modalidad).strip():
                print("La modalidad es obligatoria")
                return False

            if not curso.jornada or not str(curso.jornada).strip():
                print("La jornada es obligatoria")
                return False
            
            sql_existe = """
            SELECT 1
            FROM Curso
            WHERE idCurso = ?
            """
            self.db.cursor.execute(sql_existe, (curso.idCurso,))
            if self.db.cursor.fetchone() is not None:
                print("Ya existe un curso con ese ID")
                return False
            
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
            resultados = self.db.cursor.fetchall()

            cursos = []
            for fila in resultados:
                curso = CursoNivelacion(
                    fila.idCurso,
                    fila.nombreCurso,
                    fila.modalidad,
                    fila.jornada,
                    None
                )

                curso.cedulaDocente = fila.cedulaDocente
                curso.nombreDocente = fila.nombreDocente if fila.nombreDocente else "Sin asignar"

                cursos.append(curso)

            return cursos
        
        except Exception as e:
            print("Error al listar cursos: ", e)
            return []
        
        finally:
            self.db.cerrarConexion()


    def buscar(self, idCurso):
        conexion = self.db.conectar()
        if not conexion:
            return None
        
        try:
            if not idCurso or not str(idCurso).strip():
                return None

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
            WHERE c.idCurso = ?
            """

            self.db.cursor.execute(sql, (idCurso,))
            fila = self.db.cursor.fetchone()
            if fila is None:
                return None

            curso = CursoNivelacion(
            fila.idCurso,
            fila.nombreCurso,
            fila.modalidad,
            fila.jornada,
            None
            )

            curso.cedulaDocente = fila.cedulaDocente
            curso.docente = fila.nombreDocente if fila.nombreDocente else "Sin asignar"

            return curso
        
        except Exception as e:
            print("Error al buscar curso: ", e)
            return None
        
        finally:
            self.db.cerrarConexion()


    def asignarDocente(self, idCurso, cedula_docente):
        conexion = self.db.conectar()
        if not conexion:
            return False

        try:
            if not idCurso or not str(idCurso).strip():
                print("Debe ingresar un ID de curso")
                return False

            if not cedula_docente or not str(cedula_docente).strip():
                print("Debe ingresar la cédula del docente")
                return False
            
            sql_curso = """
            SELECT cedulaDocente
            FROM Curso
            WHERE idCurso = ?
            """
            self.db.cursor.execute(sql_curso, (idCurso,))
            curso = self.db.cursor.fetchone()

            if curso is None:
                print("No existe un curso con esa ID")
                return False

            sql_docente = """
            SELECT 1
            FROM Docente
            WHERE cedula = ?
            """
            self.db.cursor.execute(sql_docente, (cedula_docente,))
            docente = self.db.cursor.fetchone()

            if docente is None:
                print("\nNo existe un docente con esa cédula")
                return False

            if curso.cedulaDocente == cedula_docente:
                print("\nEse docente ya está asignado a este curso")
                return False

            sql = """
            UPDATE Curso
            SET cedulaDocente = ?
            WHERE idCurso = ?
            """

            self.db.cursor.execute(sql, (cedula_docente, idCurso))
            conexion.commit()
            return True
        
        except Exception as e:
            print("Error al asignar docente al curso: ", e)
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
            ORDER BY idCurso
            """

            self.db.cursor.execute(sql, cedulaDocente,)
            return self.db.cursor.fetchall()
        
        except Exception as e:
            print("Error al listar cursos del docente: ", e)
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
            print("Error al buscar cursos del docente:", e)
            return []

        finally:
            self.db.cerrarConexion()


    def buscarPorIdYDocente(self, idCurso, cedulaDocente):
        conexion = self.db.conectar()
        if not conexion:
            return None

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
            LEFT JOIN Usuario u
                ON c.cedulaDocente = u.cedula
            WHERE c.idCurso = ? AND c.cedulaDocente = ?
            """

            self.db.cursor.execute(sql, (idCurso, cedulaDocente))
            return self.db.cursor.fetchone()

        except Exception as e:
            print("Error al buscar curso del docente:", e)
            return None

        finally:
            self.db.cerrarConexion()