create database productos; 

CREATE TABLE productos (
    codigo INTEGER PRIMARY KEY,
    nombre VARCHAR(255),
    precio DECIMAL,
    cantidad INTEGER, 
	CONSTRAINT chk_codigo_mayor_a_dos CHECK (codigo >= 2)
);

CREATE TABLE prodcutoElectronico (
	codigo INTEGER PRIMARY KEY,
	marca VARCHAR(155), 
	FOREIGN KEY (codigo) REFERENCES productos(codigo)
); 

CREATE TABLE prodcutoAlimenticio (
	codigo INTEGER PRIMARY KEY,
	categoria VARCHAR(255), 
	FOREIGN KEY (codigo) REFERENCES productos(codigo)
); 

select * from "productos"; 
select * from "prodcutoelectronico";
select * from "prodcutoalimenticio";
