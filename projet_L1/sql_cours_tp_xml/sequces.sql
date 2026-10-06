DROP DATABASE IF EXISTS sequces;
CREATE DATABASE sequces;
\c sequces

CREATE SEQUENCE facture_seq
increment 1
start 1000;

CREATE SEQUENCE devis_seq
increment 1
start 500;

create table facture(id int  default  nextval('facture_seq')  primary key ,nomclient varchar(50),montant int);
create table devis(id int default nextval('facture_seq') primary key ,nomclient varchar(50),montant int);

insert into facture(nomclient, montant)
values('sossoukpe',50000);
insert into facture(nomclient, montant)
values('kolani',2000);
insert into facture(nomclient, montant)
values('oukpe',50000);
insert into facture(nomclient, montant)
values('komi',20000);
insert into facture(nomclient, montant)
values('sosso',50000);
insert into facture(nomclient, montant)
values('mama',20000);

insert into devis(nomclient, montant)
values('yuysq',5000);
insert into devis(nomclient, montant)
values('koi',2000);
insert into devis(nomclient, montant)
values('ouyukpe',50000);
insert into devis(nomclient, montant)
values('komi',20000);
insert into devis(nomclient, montant)
values('ssqytso',50000);
insert into devis(nomclient, montant)
values('mamaji',20000);


select * from facture;
select * from devis;

select currval('facture_seq');
