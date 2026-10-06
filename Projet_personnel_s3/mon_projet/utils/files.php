<?php

 function readJson(){
    
 
                        $fp_ecriture = fopen('/home/izandine/mon_projet/utils/tache.json', 'r');
                       
                        $taille=filesize('/home/izandine/mon_projet/utils/tache.json');
                        
                        $contenu = fread($fp_ecriture, $taille);
 
                        $converti=json_decode($contenu,true);
                       
                        return $converti;

 }


function writeJson($taches){

                                    $nouveauConverti=json_encode($taches);
                                
                                    $ecriture= fopen('/home/izandine/mon_projet/utils/tache.json', 'w');
                                    fwrite($ecriture, $nouveauConverti);
                               

}
 
          


























 ?>