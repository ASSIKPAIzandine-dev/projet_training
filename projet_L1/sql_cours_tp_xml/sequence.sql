DROP DATABASE IF EXISTS sequence;
CREATE DATABASE sequence;
\c sequence

CREATE SEQUENCE id_client_seq 
INCREMENT 1
START 1 ;



SELECT nextval('id_client_seq');
SELECT nextval('id_client_seq');
SELECT nextval('id_client_seq');

CREATE TABLE client (id INT DEFAULT nextval('id_client_seq') PRIMARY KEY,nom VARCHAR(50),prenom VARCHAR(50),sexe VARCHAR(1),age INT);


INSERT INTO client 
VALUES (01,'sossoukpe', 'doudou', 'M', 15);
INSERT INTO client 
VALUES (02,'lamboni', 'afi', 'F', 20);
INSERT INTO client 
VALUES (03,'Jean', 'merveille', 'M', 30);

SELECT currval('id_client_seq');

ALTER SEQUENCE id_client_seq RESTART WITH 100;



INSERT INTO client (nom, prenom, sexe, age) 
VALUES ('Mohamed', 'Ali', 'M', 35);
SELECT * FROM client;

CREATE SEQUENCE facture_seq 
INCREMENT 10 
MAXVALUE 5050
START 5000;

SELECT nextval('facture_seq');
SELECT nextval('facture_seq'); 
SELECT nextval('facture_seq'); 
SELECT nextval('facture_seq'); 
SELECT nextval('facture_seq'); 
SELECT nextval('facture_seq'); 

SELECT SETVAL  ('id_client_seq' ,1);

DELETE FROM client;


INSERT INTO client 
VALUES (01,'sossoukpe', 'doudou', 'M', 15);
INSERT INTO client 
VALUES (02,'lamboni', 'afi', 'F', 20);
INSERT INTO client 
VALUES (03,'Jean', 'merveille', 'M', 30);

