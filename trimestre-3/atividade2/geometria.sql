create database Geometria;
use Geoetria;

create table Figura (
	numero int not null,
    cor varchar(20) not null,
    constraint pk_Figura primary key(numero)
);

create table Circulo (
	numFigura int not null,
    raio double not null,
    constraint pk_Circulo primary key (numFigura),
    constraint fk_FiguraCirculo foreign key (numFigura)
		references Figura (numero)
        on delete cascade
);

create table Quadrado(
	numFigura int not null,
    lado double not null,
    constraint pk_Quadrado primary key (numFigura),
    constraint fk_FiguraQuadrado foreign key (numFigura)
		references Figura (numero)
        on delete cascade
);

select f.numero, f.cor, c.raio
from Figura f, Circulo c
where f.numero = c.numFigura
union
select f.numero, f.cor, q.lado
from Figura f, Quadrado q
where f.numero = q.numFigura;