DROP DATABASE IF EXISTS etudiant;
CREATE DATABASE etudiant;
\c etudiant
create table client(numclt int constraint pk_numclt primary key ,nom varchar,sexe varchar );
create table commande(numcmd int primary key, libelle varchar,qte int,numclt int ,  constraint fk_cmd foreign key (numclt) references client on delete no action); 

select * from client;
select * from commande;

insert into client
values (1,'sossoukpe','m');
insert into client
values (2,'akpassou','f');
insert into client
values (3,'tsdtu','f');
insert into client
values (4,'zyuz','m');
insert into client
values (5,'errjhh','m');

select * from client;
select * from commande;

insert into commande
values (1,'pc',23,1);
insert into commande
values (2,'clavier',25,2);

select * from client;
select * from commande;

delete from client where numclt = 1;
