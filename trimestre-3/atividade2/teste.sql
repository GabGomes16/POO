create database Teste;
use Teste;

create table Tabela (
	id int not null,
    texto varchar(20) not null,
    constraint pk_Teste primary key (id)
);

insert into Tabela values (5, "Teste");
insert into Tabela values (8,'OUtro teste');

select *
from Tabela