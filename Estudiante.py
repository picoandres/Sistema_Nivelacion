from Usuario import Usuario
from Materia import Materia

class Estudiante(Usuario):
    def __init__(self, cedula, nombre, correo, contrasena, rol, carrera, paralelo):
        super().__init__(cedula, nombre, correo, contrasena, rol)
        self.carrera = carrera
        self.paralelo = paralelo
        self.notas = []
        self.documentos_subidos = []

    def verPerfil(self):
        super().verPerfil()
        print(f"Nombre: {self.nombre}")
        print(f"correo: {self.correo}")
        print(f"Carrera: {self.carrera}")
        print(f"Paralelo: {self.paralelo}")
        print(f"Total de materias con nota: {len(self.notas)}")

    def verNotas(self):
        if not self.notas:
            print("Aun no tienes notas registradas.")
            return

        for Materia(), nota in self.notas.items():
            print(f"{Materia}: {nota}")
        print(f"promedio actual: {self.calcular_promedio():.2f}")
        print("=" * 30)
    #el sistema calcula el promedio del estudiante
    def calcular_promedio(self):
        if not self.notas:
            return 0.0
        return sum(self.notas.values()) / len(self.notas)

    def verAsistencia(self):
        pass
    #Metodo de subir documentos beta
    def subirDocumentos(self, nombre_documento, tipo):
        documento = {
            "nombre": nombre_documento,
            "tipo": tipo,
            "fecha": "2025-04-03",
            "estado": "Pendiente"
        }
        self.documentos_subidos.append(documento)
        print(f"Documento {nombre_documento} ha sido subido exitosamente.")
        return documento
    #El estudiante podra ver sus documentos subidos
    def verDocumentosSubidos(self):
        if not self.documentos_subidos:
            print("No has subido documentos todavia.")
            return
        for doc in self.documentos_subidos:
            print(f"{doc['nombre']} ({doc['tipo']}) | {doc['estado']}")