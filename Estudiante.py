from Usuario import Usuario
from Materia import Materia

class Estudiante(Usuario):
    def __init__(self, CedulaEstudiante, nombre, correo, contrasena, carrera, paralelo, promedio):
        super().__init__(CedulaEstudiante, nombre, correo, contrasena, rol = "Estudiante")
        self.carrera = carrera
        self.paralelo = paralelo
        self.notas = []
        self.DocumentosSubidos= []

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

        for Materia, nota in self.notas.items():
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
        self.DocumentosSubidos.append(documento)
        print(f"Documento {nombre_documento} ha sido subido exitosamente.")
        return documento
    #El estudiante podra ver sus documentos subidos
    def verDocumentosSubidos(self):
        if not self.DocumentosSubidos:
            print("No has subido documentos todavia.")
            return
        for doc in self.DocumentosSubidos:
            print(f"{doc['nombre']} ({doc['tipo']}) | {doc['estado']}")
