class GestorAulas:
    def __init__(self, horario_dao):
        self.horario_dao = horario_dao   # dependencia inyectada

    def aula_disponible(self, aula, dia, horaInicio, horaFin):
        if aula is None:
            return True

        horarios = self.horario_dao.listarTodos()

        for h in horarios:
            if h.aula != aula:
                continue
            if h.dia.lower() != dia.lower():
                continue

            inicio_nuevo = str(horaInicio)
            fin_nuevo = str(horaFin)
            inicio_existente = str(h.horaInicio)
            fin_existente = str(h.horaFin)

            hay_cruce = not (fin_nuevo <= inicio_existente or inicio_nuevo >= fin_existente)
            if hay_cruce:
                return False

        return True