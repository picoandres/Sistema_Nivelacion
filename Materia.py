class Materia: 
    def __init__(self, idMateria, nombre, descripcion):
        self.idMateria = idMateria
        self.nombre = nombre
        self.descripcion = descripcion
        self.activa = True

    def mostrar_materias_disponibles(self, listaMaterias):
        if len(listaMaterias) == 0:
            print("No hay materias registradas")
            return

        print("----- MATERIAS DISPONIBLES -----")
        for materia in listaMaterias:
            print(f"ID: {materia.idMateria}")
            print(f"Nombre: {materia.nombre}")
            print(f"Descripción: {materia.descripcion}")
            print("-" * 30)

    def actualizar_contenido(self, nuevoNombre, nuevaDescripcion):
        self.nombre = nuevoNombre
        self.descripcion = nuevaDescripcion
        
        print("Materia actualizada correctamente.")
        print(f"ID: {self.idMateria}")
        print(f"Nombre: {self.nombre}")
        print(f"Descripción: {self.descripcion}")

    def habilitar_retiro_materia(self):
        self.activa = False
        print(f"La materia {self.nombre} ha sido retirada.")
""""
# Se debe pasar al main
#funcion mostrar materias disponibles
materia1 = Materia(1, "Algebra Lineal", "Álgebra Lineal")
materia2 = Materia(2, "Base de datos", "integracion de SQL")

listaMaterias = [materia1, materia2]

materia1.mostrarMateriasDisponibles(listaMaterias)

#funcion actualizar materias
materia1.actualizarContenido(
    "Matemáticas Avanzadas",
    "Álgebra y Trigonometría"
)

#funcion deshabilitar materias
materia1.habilitarRetiroMateria()
"""