select * from pythonistas;

select * from pythonistas where apellido = 'villacis';

select nombre, apellido from pythonistas where ciudad = 'guayaquil';

select * from pythonistas where edad < 15;

select * from pythonistas where nombre = 'romina' or nombre = 'dina';

select * from pythonistas where nombre in ('romina','dina');

select * from pythonistas where nivel_de_habilidad = 'avanzado' and edad>= 20;

update pythonistas 
set edad = 18, ciudad = 'miami'
where nombre in ('joel','gabriel');

update pythonistas
set nivel_de_habilidad = 'intermedio';

delete from pythonistas
where apellido = 'villavicencio';

update pythonistas
set sexo = 'f'
where id = 3;

update pythonistas
set sexo = 'm'
where id <> 3;