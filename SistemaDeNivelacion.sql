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

CREATE TABLE Docente(
	cedula VARCHAR(20),
	titulo VARCHAR(50),
	especialidad VARCHAR(50),
	anosExperiencia INT,
	CONSTRAINT PK_Docente_cedula PRIMARY KEY(cedula),
	CONSTRAINT FK_Docente_usuario 
	FOREIGN KEY (cedula) REFERENCES Usuario(cedula) ON DELETE CASCADE
);

CREATE TABLE Administrador(
	cedula VARCHAR(20),
	id_admin INT UNIQUE,
	sede VARCHAR(50),
	telefono VARCHAR(20),
	CONSTRAINT PK_Administrador_cedula PRIMARY KEY (cedula),
	CONSTRAINT FK_Administrador_usuario 
	FOREIGN KEY (cedula) REFERENCES Usuario(cedula) ON DELETE CASCADE
);

SELECT * FROM Usuario;
SELECT * FROM Alumnos;
SELECT * FROM Docente;