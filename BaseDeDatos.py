import pyodbc #--> en caso de que suelte error es por que la libreria no se encuentra descargada, use pip install pyodbc en su terminal.

class ConexionSQLServer:
    def __init__(self):
      #se conecta a un SQL local
        self.server = 'localhost\\SQLEXPRESS'
        self.database = 'SistemaDeNivelacion'

        self.conexion = None
        self.cursor = None

  #Crea la base de datos en caso de no existir
    def crearBaseDeDatos(self):
        try:
            conexion = pyodbc.connect(
                f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                f"SERVER={self.server};"
                f"Trusted_Connection=yes;"
            )

          #interprete entre python y SQL
            cursor = conexion.cursor()

            cursor.execute(f"""
                IF NOT EXISTS (
                    SELECT name FROM sys.databases 
                    WHERE name = '{self.database}'
                )
                CREATE DATABASE {self.database}
            """)

            conexion.commit()
            cursor.close()
            conexion.close()

            print("Base de datos verificada/creada")
        except Exception as e:
            print(f"Error creando BD: {e}")
            


     #Conexion con la base de datos   
    def conectar(self):
        try:
            self.connection_string = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={self.server};"
            f"DATABASE={self.database};"
            f"Trusted_Connection=yes;"
            )

            self.conexion = pyodbc.connect(self.connection_string)
            self.cursor = self.conexion.cursor()

            print("Conexion exitosa con SQL Server")
            return self.conexion
        
        except Exception as e:
            print(f"Error al conectar: {e}")
            return None


    #Desconexion de la base de datos    
    def cerrarConexion(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
            print("Conexion cerrada")


if __name__ == "__main__":
    db = ConexionSQLServer()
    db.crearBaseDeDatos()
    db.conectar()
    db.cerrarConexion()