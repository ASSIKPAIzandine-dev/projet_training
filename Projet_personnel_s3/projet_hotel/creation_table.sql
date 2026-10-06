\c izandine
drop database gestion_hotel;
create database gestion_hotel;
\c gestion_hotel



create table Utilisateur(id integer primary key, username varchar,mot_de_passe varchar,roles varchar);

insert into Utilisateur VALUES(1,'ALI','pass01','employe');

insert into Utilisateur VALUES(2,'BABA','pass02','gerant');

insert into Utilisateur VALUES(3,'SALIOU hassane','pass03','caissier');
insert into Utilisateur VALUES(4,'BALO Josiane','pass04','administrateur');



