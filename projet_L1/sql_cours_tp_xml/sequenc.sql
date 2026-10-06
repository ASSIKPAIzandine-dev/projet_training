DROP DATABASE IF EXISTS sequences;
CREATE DATABASE sequences;
\c sequences


create table commende (id_commende int not null,nom_client varchar (100) not null);

alter table commende add constraint pk_id_commande primary key(id_commende);

insert into commende(nom_client)
values('ifnti');


create sequence seq_id_commende
increment 100
minvalue 2000
start 2000;


alter sequence seq_id_commende
increment 100
minvalue 1000
start 3000;


alter table commende
alter column id_commende
set default nextval('seq_id_commende');

insert into commende(nom_client)
values('ifnti');

insert into commende(nom_client)
values('kbu');

insert into commende(nom_client)
values('ifnti-kbu');

insert into commende(nom_client)
values('ifnti-soss');





