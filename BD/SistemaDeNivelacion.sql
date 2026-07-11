USE SistemaDeNivelacion;
GO

--Tabla Padre
CREATE TABLE Usuario(
	cedula VARCHAR(10),
	nombre VARCHAR(80) NOT NULL,
	correo VARCHAR(100) UNIQUE NOT NULL,
	contrasena VARCHAR(255) NOT NULL,
	rol VARCHAR(20) NOT NULL,

	CONSTRAINT PK_Cedula PRIMARY KEY (cedula)
);

-- Tablas Hijas
CREATE TABLE Estudiante(
	cedula VARCHAR(10) PRIMARY KEY,
	carrera VARCHAR(50) NOT NULL,

	CONSTRAINT FK_Estudiante_Usuario 
	FOREIGN KEY (cedula) REFERENCES Usuario(cedula) ON DELETE CASCADE
);

CREATE TABLE Docente(
	cedula VARCHAR(10),
	profesion VARCHAR(50),
	especialidad VARCHAR(50),
    tipoDocente  VARCHAR(20) NOT NULL,
    tiempoContrato VARCHAR(20) NOT NULL,

	CONSTRAINT PK_Docente_Cedula PRIMARY KEY(cedula),
	CONSTRAINT FK_Docente_Usuario
	FOREIGN KEY (cedula) REFERENCES Usuario(cedula) ON DELETE CASCADE
);

CREATE TABLE Administrador(
	cedula VARCHAR(10),
	id_admin INT UNIQUE,
	sede VARCHAR(50),
	telefono VARCHAR(20),

	CONSTRAINT PK_Administrador_Cedula PRIMARY KEY (cedula),

	CONSTRAINT FK_Administrador_Usuario 
	FOREIGN KEY (cedula) REFERENCES Usuario(cedula) ON DELETE CASCADE
);

CREATE TABLE Curso(
    idCurso VARCHAR(10),
    nombreCurso VARCHAR(100) NOT NULL,
    modalidad VARCHAR(20) NOT NULL,

    CONSTRAINT PK_Curso PRIMARY KEY(idCurso)
);

CREATE TABLE Paralelo(
    idParalelo VARCHAR(10)PRIMARY KEY,
    idCurso VARCHAR(10) NOT NULL,
    paralelo VARCHAR(10) NOT NULL,
    jornada VARCHAR(20) NOT NULL,
    cupoMaximo INT NOT NULL,
    estado BIT NOT NULL DEFAULT 1,

    CONSTRAINT FK_Paralelo_Curso
        FOREIGN KEY(idCurso) REFERENCES Curso(idCurso),

    CONSTRAINT UQ_Paralelo_Curso_Paralelo
        UNIQUE (idCurso, paralelo)
);

CREATE TABLE Matricula(
    cedulaEstudiante VARCHAR(10) PRIMARY KEY,
    idParalelo VARCHAR(10) NOT NULL,
    fechaAsignacion DATE DEFAULT GETDATE(),

    CONSTRAINT FK_Matricula_Estudiante
    FOREIGN KEY(cedulaEstudiante) REFERENCES Estudiante(cedula),

    CONSTRAINT FK_Matricula_Paralelo
    FOREIGN KEY(idParalelo) REFERENCES Paralelo(idParalelo)
);

CREATE TABLE Materia(
    idMateria VARCHAR(10),
    nombre VARCHAR(100) NOT NULL,
    descripcion VARCHAR(100) NULL,
    horas INT NOT NULL,
    estado BIT NOT NULL DEFAULT 1,

    CONSTRAINT PK_Materia PRIMARY KEY (idMateria)
);

CREATE TABLE AsignacionDocente(
    idAsignacion INT IDENTITY(1,1) PRIMARY KEY,
    cedulaDocente VARCHAR(10) NOT NULL,
    idParalelo VARCHAR(10) NOT NULL,
    idMateria VARCHAR(10) NOT NULL,

    CONSTRAINT FK_AsignacionDocente_Docente
        FOREIGN KEY (cedulaDocente) REFERENCES Docente(cedula),

    CONSTRAINT FK_AsignacionDocente_Paralelo
        FOREIGN KEY (idParalelo) REFERENCES Paralelo(idParalelo),

    CONSTRAINT FK_AsignacionDocente_Materia
        FOREIGN KEY (idMateria) REFERENCES Materia(idMateria),

    CONSTRAINT UQ_AsignacionDocente_ParaleloMateria
        UNIQUE (idParalelo, idMateria)
);

CREATE TABLE ParaleloMateria(
    idParalelo VARCHAR(10),
    idMateria VARCHAR(10),

    CONSTRAINT PK_ParaleloMateria PRIMARY KEY (idParalelo, idMateria),

    CONSTRAINT FK_ParaleloMateria_Paralelo FOREIGN KEY (idParalelo) REFERENCES Paralelo(idParalelo),

    CONSTRAINT FK_ParaleloMateria_Materia FOREIGN KEY (idMateria) REFERENCES Materia(idMateria)
);

CREATE TABLE Evaluacion(
    idEvaluacion INT IDENTITY(1,1) PRIMARY KEY,
    idParalelo VARCHAR(10) NOT NULL,
    idMateria VARCHAR(10) NOT NULL,
    titulo VARCHAR(50) NOT NULL,
    descripcion VARCHAR(200) NULL,
    fecha DATE NOT NULL,
    ponderacion DECIMAL(5,2) NOT NULL,

    CONSTRAINT FK_Evaluacion_ParaleloMateria
        FOREIGN KEY (idParalelo, idMateria)
        REFERENCES ParaleloMateria(idParalelo, idMateria)
);

CREATE TABLE Calificacion(
    idCalificacion INT IDENTITY(1,1) PRIMARY KEY,
    cedulaEstudiante VARCHAR(10) NOT NULL,
    idEvaluacion INT NOT NULL,
    nota DECIMAL(4,2) NOT NULL,
    retroalimentacion VARCHAR(200) NULL,

    CONSTRAINT FK_Calificacion_Estudiante
        FOREIGN KEY (cedulaEstudiante) REFERENCES Estudiante(cedula),

    CONSTRAINT FK_Calificacion_Evaluacion
        FOREIGN KEY (idEvaluacion) REFERENCES Evaluacion(idEvaluacion),

    CONSTRAINT UQ_Calificacion_Estudiante_Evaluacion
        UNIQUE (cedulaEstudiante, idEvaluacion)
);

CREATE TABLE Horario(
    idHorario INT IDENTITY(1,1) PRIMARY KEY,
    idParalelo VARCHAR(10) NOT NULL,
    dia VARCHAR(20) NOT NULL,
    horaInicio TIME NOT NULL,
    horaFin TIME NOT NULL,
    aula VARCHAR(20) NULL,
    asignador VARCHAR(50) NOT NULL,

    CONSTRAINT FK_Horario_Paralelo
    FOREIGN KEY (idParalelo) REFERENCES Paralelo(idParalelo),

    CONSTRAINT CK_Horario_Horas
        CHECK (horaInicio < horaFin)
);


-- Primeros usuarios
INSERT INTO Usuario VALUES
(1317938437, 'Andrés Pico', 'e1317938437@universidad.edu.ec', 'andres123', 'Estudiante'),
(1301234567, 'Edgardo Panchana', 'admin@universidad.edu.ec', 'admin123', 'Administrador'),
(1309876543, 'Harold Ormaza', 'd1309876543@universidad.edu.ec', 'harold123', 'Docente');

INSERT INTO Administrador VALUES (1301234567, 1, 'Matriz', '0981234567');


-- Para Curso de Nivelación de Software
 -- Docente
INSERT INTO Estudiante VALUES (1317938437, 'Software', NULL);
INSERT INTO Docente VALUES (1309876543, 'Ingeniero en sistemas', 'Tecnologías de la Información', 'Titular', 'Tiempo Completo', NULL);

 -- Estudiantes
INSERT INTO Usuario VALUES (1301111111, 'Jefferson Moreira', 'e1301111111@universidad.edu.ec', 'jefferson123', 'Estudiante');
INSERT INTO Estudiante VALUES (1301111111, 'Software', NULL);

INSERT INTO Usuario VALUES (1302222222, 'Ruber Naranjo', 'e1302222222@universidad.edu.ec', 'ruber123', 'Estudiante');
INSERT INTO Estudiante VALUES (1302222222, 'Software', NULL);


  -- Usado para probar el patrón Bridge
INSERT INTO Usuario VALUES (1301928374, 'Bryan Vera', 'd1301928374@universidad.edu.ec', 'bryan123', 'Docente');
INSERT INTO Docente VALUES (1301928374, 'Ingeniero comercial', 'Gerencia Comercial', 'Suplente', 'Tiempo Parcial', NULL);


-- Para Curso de Nivelación de Arquitectura
 -- Docente
INSERT INTO Usuario VALUES (1309182736, 'Pablo García', 'd1309182736@universidad.edu.ec', 'pablo123', 'Docente');
INSERT INTO Docente VALUES (1309182736, 'Arquitecto', 'Arquitectura Comercial e Industrial', 'Titular', 'Tiempo Completo', NULL);
 -- Estudiante
INSERT INTO Usuario VALUES (1311409233, 'Sofía Toala', 'e1311409233@universidad.edu.ec', 'sofia123', 'Estudiante');
INSERT INTO Estudiante VALUES (1311409233, 'Arquitectura', NULL);


-- SELECTS
SELECT * FROM Usuario;
SELECT * FROM Administrador;
SELECT * FROM Estudiante;
SELECT * FROM Docente;
SELECT * FROM Curso;
SELECT * FROM Paralelo; -- Cada paralelo tiene 1 docente asignado por cédula
SELECT * FROM Matricula; -- Estudiante asignado a un curso
SELECT * FROM Materia;
SELECT * FROM AsignacionDocente;
SELECT * FROM ParaleloMateria;
SELECT * FROM Evaluacion;
SELECT * FROM Calificacion;
SELECT * FROM Horario;

-- Para eliminar tablas por si acaso (en orden descendente, es importante por los FK)
DROP TABLE Horario;
DROP TABLE Calificacion;
DROP TABLE Evaluacion;
DROP TABLE ParaleloMateria;
DROP TABLE AsignacionDocente;
DROP TABLE Materia;
DROP TABLE Matricula;
DROP TABLE Paralelo;
DROP TABLE Curso;
DROP TABLE Docente;
DROP TABLE Estudiante;
DROP TABLE Administrador;
DROP TABLE Usuario;