
SELECT clt_localite,clt_chiffreaffaire
FROM client
WHERE clt_chiffreaffaire>300;

SELECT frs_nom
FROM Fournisseur;

SELECT *
FROM article
WHERE art_poids>500;

SELECT *
FROM client
WHERE clt_localite='Paris';

SELECT *
FROM article
WHERE art_prixvente>=2*art_prixachat;

SELECT *
FROM article 
WHERE art_couleur='rouge' AND art_poids>100;

SELECT *
FROM article
WHERE  art_couleur='rouge'OR art_poids>100;


SELECT *
FROM article
WHERE(art_couleur='rouge' AND art_poids>100)
OR ar_couleur='vert';


SELECT *
FROM article
WHERE art_couleur IN ('rouge','vert');

SELECT *
FROM article
ORDER BY art_poids;

SELECT *
FROM article
WHERE art_poids<=100
ORDER BY art_poids,art_prixachat DESC;



SELECT clt_numero || ' ' || UPPER(clt_nom) || ' -' || clt_pays nom_complet 
FROM client
WHERE clt_localite = 'Paris';

SELECT AVG(lcd_datliv - cmd_date) AS delai, MAX(lcd_datliv -cmd_date) AS max
FROM commande C, lignecommande LC
WHERE C.cmd_numero= LC.lcd_cmd;



SELECT art_couleur, AVG(art_prixvente)
FROM article
WHERE art_prixachat <= 5
GROUP BY art_couleur
ORDER BY art_couleur;


/*SELECT art_couleur,AVG(art_prixvente)
FROM article
GROUP BY art_couleur
HAVING BY AVG(art_prixvente) > 100
ORDER BY art_couleur;*/


SELECT cmd_mag, COUNT(*) 
FROM commande
WHERE cmd_date BETWEEN '940606' and '940607' GROUP BY cmd_mag
HAVING COUNT(*) > 1;


 


































C







