DROP DATABASE IF EXISTS matable;
CREATE DATABASE matable;
\c matable

CREATE TABLE matable (nom varchar,prenom varchar,age INT);
insert into matable
values ('agboa','afi',19);
insert into matable
values ('lamboni','merveil',22);
insert into matable
values ('douti','maria',24);

create role user1 login password 'pwd1';
create role user2 login password 'pwd2';
create role user3 login password 'pwd3';
create role user4 login password 'pw4';
create role user5 login password 'pwd5';

create group groupe1 ;

GRANT groupe1 TO user1;

GRANT groupe1 TO user2;

GRANT SELECT ON matable TO user1 WITH GRANT OPTION;
GRANT UPDATE ON matable TO user2 WITH GRANT OPTION;

CREATE ROLE groupe2;

GRANT groupe2 TO user1;
GRANT groupe2 TO user3;























