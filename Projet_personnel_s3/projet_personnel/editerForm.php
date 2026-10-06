<?php

 require 'utils/files.php';
              $taches=readJson();  
              
              $nom= $_GET["nom"]; 
              //var_dump($libelle);
              
              $tache_trouver=null;
              foreach ($taches as $tach ){
                                        if($tach["nom"]===$nom){
                                            //$tache_trouver=$tach;
                                            $tach["nom"]=$nom;
                                            $tach["description"]=$description;
                                            $tach["date"]=$date;
                                            $tach["heure"]=$heure;
                                            break;

                            }
                }
                writeJson($taches);
                echo "tache a été mis à jour !";





?>

<a href="index.php">retour</a>

