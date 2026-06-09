from CursoNivelacion import CursoNivelacion
from Estudiante import Estudiante
from Horario import Horario
from Docente import Docente

#Objetos
horario = Horario(
    "Lunes",
    "8:00 a.m",
    "13:00 p.m",
    "Aula A-28"
)

curso = CursoNivelacion(
    "CN-001",
    "Nivelación Software",
    "Virtual",
    "Matutina",
    horario
)

docente = Docente(
    1,
    "Alex Santamaría",
    "alexsantamaria@uleam.edu.ec",
    "alex1596santamaria",
    "Ingeniero en Software",
    "Ingeniería de Requisitos"
)

estudiante = Estudiante(
    10,
    "Andrés Pico",
    "e1317938437@live.uleam.edu.ec",
    "pico1212",
    "Software",
    "A"
)

if estudiante.iniciarSesion("pico1212"):
    print(f"{estudiante.nombre} ha iniciado sesión")
else:
    print("Contraseña incorrecta")

curso.asignarDocente(docente)

docente.calificar(estudiante, 9.5)
print(estudiante.promedio())

estudiante.recuperarContrasena(a="correo", b="telefono", c= "teléfono")
estudiante.cerrarSesion()