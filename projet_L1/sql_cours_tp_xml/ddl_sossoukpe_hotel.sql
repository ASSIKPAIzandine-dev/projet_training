DROP DATABASE IF EXISTS hotel;
CREATE DATABASE hotel;
\c hotel;

create table chambre(numchambre int constraint pk_numchambre primary key, prix int, nbrlit int, nbrpersonne int, confort varchar(50) );
---create table client(numclient int constraint pk_numclient primary key, nom varchar(50) not null , prenom  varchar(50) not null,adresse varchar(50) not null );
create table reservation(numclient int,numchambre int,datearrivé date,datedepart date,primary key( numclient,numchambre),foreign key(numclient) references client(numclient),foreign key(numchambre) references chambre(numchambre)); 
create table etudiant(idetudiant int constraint pk_idetudiant primary key,nom varchar);
create table matiere(codemat int primary key,libéllémat varchar,coefmat float);
create table EVALUER(idetudiant int, codemat int, date date,note float, primary key (idetudiant,codemat) ,foreign key (idetudiant) references etudiant(idetudiant),foreign key (codemat) references matiere(codemat));

create table eleve(idele int ,nom varchar,datenaiss varchar);
create table matiere(idmat int ,nom varchar(20),note varchar(20));
create table salle(idele int,idmat int,numsalle int constraint pk_salle primary key (idele,idmat), constraint fr_salles foreign key (idel) references(eleve) constraint fr_salle foreign key idmat references (matiere));
