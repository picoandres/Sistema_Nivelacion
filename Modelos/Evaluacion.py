class Evaluacion:
    def __init__(self, idEvaluacion, idParalelo, idMateria, titulo, descripcion, fecha, ponderacion,
                 nombreCurso=None, nombreMateria=None, nombreParalelo=None):
        self.idEvaluacion = idEvaluacion
        self.idParalelo = idParalelo
        self.idMateria = idMateria
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha = fecha
        self.ponderacion = ponderacion

        # Atributos para sentencias JOIN cuando se consulte en la BD mediante el DAO
        self.nombreCurso = nombreCurso
        self.nombreMateria = nombreMateria
        self.nombreParalelo = nombreParalelo
        
    def mostrarInfo(self):
        descripcion = self.descripcion if self.descripcion else "Sin descripción"
        nombreMateria = self.nombreMateria if self.nombreMateria else self.idMateria
        nombreParalelo = self.nombreParalelo if self.nombreParalelo else self.idParalelo

        print(f"ID evaluación : {self.idEvaluacion}")
        print(f"Paralelo      : {nombreParalelo}")
        print(f"Materia       : {nombreMateria}")
        print(f"Título        : {self.titulo}")
        print(f"Descripción   : {descripcion}")
        print(f"Fecha         : {self.fecha}")
        print(f"Ponderación   : {self.ponderacion}%")