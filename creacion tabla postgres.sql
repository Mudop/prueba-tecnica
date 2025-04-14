create table candidatos(
 id SERIAL primary key,
 nombre VARCHAR(100),
 apellido VARCHAR(100),
 tipo_documento VARCHAR(10),
 cedula VARCHAR(50) UNIQUE,
 fecha_nacimiento DATE,
 rh VARCHAR(5),
 ciudad_expedicion VARCHAR(100),
 ciudad_nacimiento VARCHAR(100),
 ciudad_domicilio VARCHAR(100)
)



create table ofertas(
id SERIAL primary key,
cliente VARCHAR(100),
cargo VARCHAR(100),
description text,
ciudad VARCHAR(100)
)


create table ordenes(
id SERIAL primary key,
cliente VARCHAR(100),
cargo VARCHAR(100),
examenes TEXT
)
