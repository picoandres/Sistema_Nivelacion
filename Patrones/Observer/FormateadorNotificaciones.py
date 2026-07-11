class FormateadorNotificaciones:
    @staticmethod
    def nueva_evaluacion(nombreCurso, nombreMateria, titulo, fecha, ponderacion):
        return (
            f"[NUEVA EVALUACIÓN] "
            f"Curso: {nombreCurso} | "
            f"Materia: {nombreMateria} | "
            f"Evaluación: {titulo} | "
            f"Fecha: {fecha} | "
            f"Ponderación: {ponderacion}%"
        )

    @staticmethod
    def nueva_calificacion(nombreCurso, nombreMateria, tituloEvaluacion, nota):
        return (
            f"[NUEVA CALIFICACIÓN] "
            f"Curso: {nombreCurso} | "
            f"Materia: {nombreMateria} | "
            f"Evaluación: {tituloEvaluacion} | "
            f"Nota: {nota}/10"
        )

    @staticmethod
    def calificacion_actualizada(nombreCurso, nombreMateria, tituloEvaluacion, nota, descripcion=None):
        mensaje = (
            f"[CALIFICACIÓN ACTUALIZADA] "
            f"Curso: {nombreCurso} | "
            f"Materia: {nombreMateria} | "
            f"Evaluación: {tituloEvaluacion} | "
            f"Nueva nota: {nota}/10"
        )

        if descripcion:
            mensaje += f" | Observación: {descripcion}"

        return mensaje