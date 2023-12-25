select * from pythonistas;
insert into pythonistas(nombre, apellido, ciudad, nivel_de_habilidad, fecha_de_registro, edad)
values('romina','villavicencio','malaga','avanzado','2023-12-20', 20);
insert into pythonistas(nombre, apellido, ciudad, nivel_de_habilidad, fecha_de_registro, edad)
values('gabriel','villacis','guayaquil','avanzado','2023-12-20', 19);

select nombre,apellido from pythonistas
where edad>19;
