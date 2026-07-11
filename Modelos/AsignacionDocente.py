class AsignacionDocente:
    def __init__(self, cedulaDocente, idParalelo, idMateria,
                 nombreDocente, nombreCurso, nombreMateria, nombreParalelo=None):
        self.cedulaDocente = cedulaDocente
        self.idParalelo = idParalelo
        self.idMateria = idMateria

        # Para consultas con JOIN
        self.nombreDocente = nombreDocente
        self.nombreCurso = nombreCurso
        self.nombreMateria = nombreMateria
        self.nombreParalelo = nombreParalelo


    def mostrarInfo(self):
        docente = self.nombreDocente if self.nombreDocente else self.cedulaDocente
        materia = self.nombreMateria if self.nombreMateria else self.idMateria
        paralelo = self.nombreParalelo if self.nombreParalelo else self.idParalelo

        print(f"Docente  : {docente}")
        print(f"Paralelo : {paralelo}")
        print(f"Materia  : {materia}")