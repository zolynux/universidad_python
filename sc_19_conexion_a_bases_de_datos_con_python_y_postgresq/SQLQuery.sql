CREATE DATABASE test_db;

USE test_db;

CREATE TABLE public.persona (
    id_persona SERIAL PRIMARY KEY NOT NULL,          -- Columna de tipo SERIAL para un ID autoincremental
    nombre VARCHAR(50),    -- Columna para el nombre (máximo 50 caracteres)
    apellido VARCHAR(50),  -- Columna para el apellido (máximo 50 caracteres)
    email VARCHAR(100)       -- Columna para el email (máximo 100 caracteres, único)
);

INSERT INTO Persona (nombre, apellido, email)
VALUES ('Juan', 'Perez', 'jperez@mail.com');
    
INSERT INTO Persona (nombre, apellido, email)
VALUES ('Karla', 'Gomez', 'kgomez@mail.com');

SELECT * FROM Persona;