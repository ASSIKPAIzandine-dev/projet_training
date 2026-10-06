\c abdel
DROP DATABASE IF EXISTS gestion_stock;
CREATE DATABASE gestion_stock;
\c gestion_stock

--- la creation des tables de la base de donnee gestion_stockseqMatiere
CREATE SEQUENCE id_produit_seq INCREMENT 1 MINVALUE 1 START 1;
CREATE SEQUENCE id_client_seq INCREMENT 1 MINVALUE 1 START 1;
CREATE SEQUENCE id_vente_seq INCREMENT 1 MINVALUE 1 START 1;
CREATE SEQUENCE id_categorie_seq INCREMENT 1 MINVALUE 1 START 1;
CREATE SEQUENCE id_paiment_seq INCREMENT 1 MINVALUE 1 START 1;
CREATE SEQUENCE id_ligne_vente_seq INCREMENT 1 MINVALUE 1 START 1;
CREATE SEQUENCE id_ligne_approvisionnement_seq INCREMENT 1 MINVALUE 1 START 1;
CREATE SEQUENCE id_approvisionnement_seq INCREMENT 1 MINVALUE 1 START 1;


CREATE TABLE categorie(id_categorie integer  default nextval('id_categorie_seq') constraint pk_id_categorie primary key,nom varchar);
CREATE TABLE produit(id_produit integer default nextval ('id_produit_seq') constraint pk_id_produit primary key,code_produit varchar,libelle varchar(50),pu_vente integer,qtite_produit integer,date_perimption date,id_categorie integer, foreign key (id_categorie)references categorie);
CREATE TABLE client(id_client integer default nextval('id_client_seq') primary key,code_client varchar,nom varchar,prenom varchar,sexe varchar check(sexe in('f','m')) ,numero_tel integer,adresse varchar,date_nais date );
CREATE TABLE vente( id_vente integer  default nextval('id_vente_seq') constraint pk_id_vente primary key, date_vente  timestamp default now() ,prix_total integer default 0,id_client integer, foreign key (id_client) references client);

CREATE TABLE paiement(id_paiement integer default nextval('id_paiment_seq') constraint pk_id_paiement primary key,montant integer,date_paiement timestamp default now(),id_vente integer, foreign key (id_vente) references vente,statu varchar default 'en cours');
CREATE TABLE ligne_vente(id_ligne_vente integer  default nextval('id_ligne_vente_seq') constraint pk_id_ligne_vente primary key,quantite_vendue integer,id_produit integer,foreign key (id_produit) references produit,id_vente integer, foreign key (id_vente) references vente,montant integer default 0);
CREATE TABLE approvisionnement(id_approvisionnement integer default nextval('id_approvisionnement_seq') constraint pk_id_approvisionnement primary key, code_approvisionnement varchar ,prix_total_appro integer default 0,date_appro timestamp default now());
CREATE TABLE ligne_approvisionnement(id_ligne_approvisionnement integer default nextval('id_ligne_approvisionnement_seq') constraint pk_id_ligne_approvisionnement primary key,montant_appro integer default 0,prix_achat integer,qt_approvisionnement integer,id_produit integer, foreign key(id_produit) references produit,id_approvisionnement integer ,foreign key(id_approvisionnement) references approvisionnement);


insert into categorie(nom) values('alimentation');
insert into categorie(nom) values('cosmetique');
insert into categorie(nom) values('agricole');

----- creation des triggers et des fonctions de la base de donnee gestion_stock
--code trigger pour le produit

CREATE SEQUENCE produit_code_num_seq
INCREMENT 1
MINVALUE 1
START 1;

CREATE OR REPLACE FUNCTION generate_simple_product_code()
RETURNS TRIGGER AS $$
DECLARE 
    codes varchar ;
BEGIN
    codes := UPPER(SUBSTRING(new.libelle FROM 1 FOR 4)) || '00' || NEXTVAL('produit_code_num_seq');
    update produit set code_produit= codes where id_produit =new.id_produit;
    return new;   
END;
$$ LANGUAGE plpgsql;

create trigger code_tigger after insert on produit 
for each row 
execute procedure generate_simple_product_code();



--code trigger pour l approvissionnement

CREATE SEQUENCE produit_code_num_seq_appro
INCREMENT 1
MINVALUE 1
START 1;

CREATE OR REPLACE FUNCTION generate_approvi_code()
RETURNS TRIGGER AS $$
DECLARE 
    codes varchar :='APPR';
BEGIN
    codes := codes || '00' || NEXTVAL('produit_code_num_seq_appro');
    update approvisionnement set code_approvisionnement= codes where id_approvisionnement =new.id_approvisionnement;
    return new;   
END;
$$ LANGUAGE plpgsql;

create trigger code_tigger after insert on approvisionnement 
for each row 
execute procedure generate_approvi_code();




--trigger pour la quantite
/*
CREATE OR REPLACE FUNCTION generate_qtite()
RETURNS TRIGGER AS $$
DECLARE
  qte integer ; 
BEGIN 
  select qtite_produit into qte from produit where id_produit=new.id_produit ;
  update approvisionnement set qt_approvisionnement=qte where id_approvisionnement=new.id_approvisionnement;
  return new;
END;
$$
LANGUAGE plpgsql;

create trigger qtite after insert on produit for each row 
execute PROCEDURE generate_qtite(); 
*/


CREATE SEQUENCE code_num_seq_client
INCREMENT 1
MINVALUE 1
START 1;

CREATE OR REPLACE FUNCTION generate_client_code()
RETURNS TRIGGER AS $$
DECLARE 
    codes varchar :='CLT';
BEGIN
    codes := codes || '00' || NEXTVAL('code_num_seq_client');
    update client set code_client= codes where id_client =new.id_client;
    return new;   
END;
$$ LANGUAGE plpgsql;

create trigger code_tigger after insert on client 
for each row 
execute procedure generate_client_code();


------trigger pour la mise a jour de la quantite du produit apres une vente
-- Elle est déclenchée après l'insertion d'une nouvelle ligne de vente
create or REPLACE FUNCTION mise_a_jour_produit() returns trigger
as $$
BEGIN
   update produit set qtite_produit = qtite_produit-new.quantite_vendue where id_produit=new.id_produit;
   return new ;

END ;
$$
LANGUAGE plpgsql ;

CREATE TRIGGER mise_a_jour_produit after INSERT ON ligne_vente
FOR EACH ROW 
execute PROCEDURE mise_a_jour_produit() ;

------trigger pour la mise a jour du montant de la ligne de vente
-- Cette fonction met à jour le montant de la ligne de vente en fonction du prix de vente
-- du produit et de la quantité vendue
-- Elle est déclenchée après l'insertion d'une nouvelle ligne de vente
create or REPLACE FUNCTION mise_a_jour_montant() returns trigger
as $$
DECLARE
    prix integer ;
BEGIN
   select pu_vente into prix from produit where id_produit=new.id_produit ;
   update ligne_vente set montant = (prix*quantite_vendue) where id_produit=new.id_produit ;
   return new;
END ;
$$
LANGUAGE plpgsql;

CREATE TRIGGER mise_a_jour_montant after INSERT ON ligne_vente 
FOR EACH ROW 
execute PROCEDURE mise_a_jour_montant();

-----trigger pour la mise a jour du prix total de la vente
-- Cette fonction met à jour le prix total de la vente en fonction des montants des lignes
-- de vente associées à cette vente
-- Elle est déclenchée après chaque mise à jour d'une ligne de vente
create or REPLACE FUNCTION mise_a_jour_prix_total() returns trigger
as $$
DECLARE
   prix integer;
BEGIN
   select sum(montant) into prix from ligne_vente where id_vente=new.id_vente;
   update vente set prix_total=prix where id_vente=new.id_vente ;
   return new;
END;
$$
LANGUAGE plpgsql ;

CREATE TRIGGER mise_a_jour_prix_total AFTER update ON ligne_vente
FOR EACH ROW 
execute PROCEDURE mise_a_jour_prix_total();





--trigger pour la mise a jour du statut du paiement
-- Cette fonction met à jour le statut des paiements en fonction du montant total de la vente
create or replace function mise_ajour_statu() returns trigger 
as $$
DECLARE
   montant_vente integer;
   som_montant_payer integer;
BEGIN
    select prix_total into montant_vente from vente where id_vente=new.id_vente;
    select sum(montant) into som_montant_payer from paiement where id_vente = new.id_vente;
    
    if som_montant_payer >= montant_vente then
       update paiement set statu ='valide' where id_vente=new.id_vente;
       return new;
    end if;   

    return new; 
END;
$$
LANGUAGE 'plpgsql' ;

create trigger mise_ajour_statu after insert on paiement 
for each row 
execute PROCEDURE mise_ajour_statu();




------trigger pour la mise a jour du montant de l'approvisionnement
-- Cette fonction met à jour le montant de l'approvisionnement en fonction du prix d'achat
-- et de la quantité d'approvisionnement
-- Elle est déclenchée après l'insertion d'une nouvelle ligne d'approvisionnement
create or REPLACE FUNCTION mise_a_jour_montant_appro() returns trigger
as $$
BEGIN
   update ligne_approvisionnement set montant_appro = (new.prix_achat * new.qt_approvisionnement) where id_ligne_approvisionnement=new.id_ligne_approvisionnement ;
   return new;
END ;
$$
LANGUAGE plpgsql;

CREATE TRIGGER mise_a_jour_montant_appro after INSERT ON ligne_approvisionnement 
FOR EACH ROW 
execute PROCEDURE mise_a_jour_montant_appro();



create or REPLACE FUNCTION mise_a_jour_prix_total_appro() returns trigger
as $$
DECLARE
   prix integer;
BEGIN
   select sum(montant_appro) into prix from ligne_approvisionnement where id_approvisionnement=new.id_approvisionnement;
   update approvisionnement set prix_total_appro=prix where id_approvisionnement=new.id_approvisionnement ;
   return new;
END;
$$
LANGUAGE plpgsql ;

CREATE TRIGGER mise_a_jour_prix_total_appro AFTER update ON ligne_approvisionnement
FOR EACH ROW 
execute PROCEDURE mise_a_jour_prix_total_appro();




