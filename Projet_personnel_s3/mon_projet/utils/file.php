<?php

    //9) manipulation de produits.json avec les fonctions readJson() et writeJSON()



 function readJson(){
                        
    
 
                        $fp_ecriture = fopen('/home/izandine/ecommerce/utils/produit.json', 'r');
                        // recuperation de la taille du fichier par la fonction filesize (nom_fichier)
                        $taille=filesize('/home/izandine/ecommerce/utils/produit.json');
                        
                        $contenu = fread($fp_ecriture, $taille);
 
                        $converti=json_decode($contenu,true);
                        //var_dump($converti);
                        return $converti;

 }
 //var_dump(readJson());


function writeJson($produits){


                   


                           
                                        

                                


                                    $nouveauConverti=json_encode($produits);
                                    //var_dump($nouveauConverti);


                                    $ecriture= fopen('/home/izandine/ecommerce/utils/produit.json', 'w');


                                    fwrite($ecriture, $nouveauConverti);
                               

}





















             






 





















































?>

