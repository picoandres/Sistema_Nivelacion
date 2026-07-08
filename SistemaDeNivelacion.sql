USE SistemaDeNivelacion;
GO

--Tabla Padre
CREATE TABLE Usuario(
	cedula VARCHAR(20),
	nombre VARCHAR(80) NOT NULL,
	correo VARCHAR(100) UNIQUE NOT NULL,
	contrasena VARCHAR(255) NOT NULL,
	rol VARCHAR(20) NOT NULL,
	CONSTRAINT PK_cedula PRIMARY KEY (cedula)
);

-- Tablas Hijas
CREATE TABLE Alumnos(
	cedula VARCHAR(20),
	carrera VARCHAR(50),
	paralelo VARCHAR(10),
	CONSTRAINT PK_Estudiante_cedula PRIMARY KEY (cedula),
	CONSTRAINT FK_Estudiante_usuario 
	FOREIGN KEY (cedula) REFERENCES Usuario(cedula) ON DELETE CASCADE
);
-- Crea la tabla de Docente
CREATE TABLE Docente(
	cedula VARCHAR(20),
	profesion VARCHAR(50),
	especialidad VARCHAR(50),
    tipoDocente  VARCHAR(20) NOT NULL,
    tiempoContrato VARCHAR(20) NOT NULL,
    idMateria VARCHAR(10) NOT NULL,
	CONSTRAINT PK_Docente_cedula PRIMARY KEY(cedula),
	CONSTRAINT FK_Docente_usuario 
	FOREIGN KEY (cedula) REFERENCES Usuario(cedula) ON DELETE CASCADE
);
-- Crea la tabla de los administradores
CREATE TABLE Administrador(
	cedula VARCHAR(20),
	id_admin INT UNIQUE,
	sede VARCHAR(50),
	telefono VARCHAR(20),
	CONSTRAINT PK_Administrador_cedula PRIMARY KEY (cedula),
	CONSTRAINT FK_Administrador_usuario 
	FOREIGN KEY (cedula) REFERENCES Usuario(cedula) ON DELETE CASCADE
);
-- Crea la tabla de los cursos
CREATE TABLE Curso(
    idCurso VARCHAR(20),
    nombreCurso VARCHAR(100) NOT NULL,
    modalidad VARCHAR(30) NOT NULL,
    jornada VARCHAR(20) NOT NULL,
    cedulaDocente VARCHAR(20) NULL,
    CONSTRAINT PK_Curso PRIMARY KEY(idCurso),
    CONSTRAINT FK_Curso_Docente
    FOREIGN KEY(cedulaDocente) REFERENCES Docente(cedula)
);

CREATE TABLE AsignacionCurso(
    cedulaEstudiante VARCHAR(20),
    idCurso VARCHAR(20),

    CONSTRAINT PK_AsignacionCurso
    PRIMARY KEY(cedulaEstudiante,idCurso),

    CONSTRAINT FK_AsignacionCurso_Estudiante
    FOREIGN KEY(cedulaEstudiante)
    REFERENCES Alumnos(cedula),

    CONSTRAINT FK_AsignacionCurso_Curso
    FOREIGN KEY(idCurso)
    REFERENCES Curso(idCurso)
);

CREATE TABLE Materia(
    idMateria VARCHAR(10),
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(200) NULL,
    horas INT NOT NULL,
    estado BIT NOT NULL DEFAULT 1,

    CONSTRAINT PK_Materia PRIMARY KEY (idMateria)
);

CREATE TABLE CursoMateria(
    idCurso VARCHAR(20),
    idMateria VARCHAR(10),
    CONSTRAINT PK_CursoMateria PRIMARY KEY (idCurso, idMateria),
    CONSTRAINT FK_CursoMateria_Curso FOREIGN KEY (idCurso) REFERENCES Curso(idCurso),
    CONSTRAINT FK_CursoMateria_Materia FOREIGN KEY (idMateria) REFERENCES Materia(idMateria)
);

CREATE TABLE Evaluacion(
    idEvaluacion INT IDENTITY(1,1),
    idCurso VARCHAR(20) NOT NULL,
    idMateria VARCHAR(10) NOT NULL,
    titulo VARCHAR(100) NOT NULL,
    descripcion VARCHAR(200) NULL,
    fecha DATE NOT NULL,
    ponderacion DECIMAL(5,2) NOT NULL,

    CONSTRAINT PK_Evaluacion PRIMARY KEY (idEvaluacion),

    CONSTRAINT FK_Evaluacion_Curso
        FOREIGN KEY (idCurso) REFERENCES Curso(idCurso),

    CONSTRAINT FK_Evaluacion_Materia
        FOREIGN KEY (idMateria) REFERENCES Materia(idMateria)
);

CREATE TABLE Calificacion(
    idCalificacion INT IDENTITY(1,1),
    cedulaEstudiante VARCHAR(20) NOT NULL,
    idCurso VARCHAR(20) NOT NULL,
    idEvaluacion INT NOT NULL,
    nota DECIMAL(4,2) NOT NULL,
    descripcion VARCHAR(100) NULL,

    CONSTRAINT PK_Calificacion PRIMARY KEY (idCalificacion),

    CONSTRAINT FK_Calificacion_Estudiante
        FOREIGN KEY (cedulaEstudiante) REFERENCES Alumnos(cedula),

    CONSTRAINT FK_Calificacion_Curso
        FOREIGN KEY (idCurso) REFERENCES Curso(idCurso),

    CONSTRAINT FK_Calificacion_Evaluacion
        FOREIGN KEY (idEvaluacion) REFERENCES Evaluacion(idEvaluacion)
);

CREATE TABLE Horario (
    idHorario INT IDENTITY(1,1) PRIMARY KEY,
    idCurso VARCHAR(20) NOT NULL,
    dia VARCHAR(30) NOT NULL,
    horaInicio TIME NOT NULL,
    horaFin TIME NOT NULL,
    aula VARCHAR(5) NOT NULL,
    asignador VARCHAR(100) NOT NULL,
    FOREIGN KEY (idCurso) REFERENCES Curso(idCurso)
);


-- Primeros usuarios
INSERT INTO Usuario VALUES
(1317938437, 'Andrés Pico', 'e1317938437@universidad.edu.ec', 'andres123', 'Estudiante'),
(1301234567, 'Edgardo Panchana', 'admin@universidad.edu.ec', 'admin123', 'Administrador'),
(1309876543, 'Harold Ormaza', 'd1309876543@universidad.edu.ec', 'harold123', 'Docente');

INSERT INTO Administrador VALUES (1301234567, 1, 'Matriz', '0981234567');


-- Para Curso de Nivelación de Software
INSERT INTO Alumnos VALUES (1317938437, 'Software', 'A24');
INSERT INTO Docente VALUES (1309876543, 'Ingeniero en sistemas', 'Tecnologías de la Información', 'Titular', 'Tiempo Completo', 'NS-1');

INSERT INTO Usuario VALUES (1301111111, 'Jefferson Moreira', 'e1301111111@universidad.edu.ec', 'jefferson123', 'Estudiante');
INSERT INTO Alumnos VALUES (1301111111, 'Software', 'A24');

INSERT INTO Usuario VALUES (1302222222, 'Ruber Naranjo', 'e1302222222@universidad.edu.ec', 'ruber123', 'Estudiante');
INSERT INTO Alumnos VALUES (1302222222, 'Software', 'A24');


  -- Usado para probar el patrón Bridge
INSERT INTO Usuario VALUES (1301928374, 'Bryan Vera', 'd1301928374@universidad.edu.ec', 'bryan123', 'Docente');
INSERT INTO Docente VALUES (1301928374, 'Ingeniero comercial', 'Gerencia Comercial', 'Suplente', 'Tiempo Parcial', 'NS-3');


-- Para Curso de Nivelación de Arquitectura
INSERT INTO Usuario VALUES (1309182736, 'Pablo García', 'd1309182736@universidad.edu.ec', 'pablo123', 'Docente');
INSERT INTO Docente VALUES (1309182736, 'Arquitecto', 'Paisajismo', 'Titular', 'Tiempo Completo', 'NA-1');

INSERT INTO Usuario VALUES (1311409233, 'Sofía Toala', 'e1311409233@universidad.edu.ec', 'sofia123', 'Estudiante');
INSERT INTO Alumnos VALUES (1311409233, 'Arquitectura', 'A35');


-- SELECTS
SELECT * FROM Usuario;
SELECT * FROM Administrador;
SELECT * FROM Alumnos;
SELECT * FROM Docente;
SELECT * FROM Curso;           -- Cada curso tiene 1 docente asignado por cédula
SELECT * FROM AsignacionCurso; -- Estudiante asignado a un curso
SELECT * FROM Materia;
SELECT * FROM CursoMateria;
SELECT * FROM Evaluacion;
SELECT * FROM Calificacion;
SELECT * FROM Horario;