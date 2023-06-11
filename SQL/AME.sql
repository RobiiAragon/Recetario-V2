CREATE DATABASE AME;

CREATE TABLE pacientes (
  id int(11) NOT NULL,
  nombre varchar(50) NOT NULL,
  fecha_naciemiento date DEFAULT NULL,
  direccion varchar(100) DEFAULT NULL,
  telefono varchar(20) DEFAULT NULL
);


CREATE TABLE tratamientos (
  id int(11) NOT NULL,
  nombre varchar(200) DEFAULT NULL,
  descripcion varchar(200) DEFAULT NULL
);


CREATE TABLE usuarios (
  id int(11) NOT NULL,
  usuario varchar(50) NOT NULL,
  contraseña varchar(100) NOT NULL
);
