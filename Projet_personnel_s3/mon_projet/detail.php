
    <?php
              require 'utils/files.php';
              $taches=readJson();  
              
              $nom= $_GET["nom"]; 
              //var_dump($libelle);
              
              $tache_trouver=null;
              foreach ($taches as $tach ){
                                        if($tach["nom"]===$nom){
                                            $tache_trouver=$tach;
                                            
                                        }
                        

              }
              //var_dump($tach_trouver);

             
             
             
             
             
             
             
             ?>



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Details des taches</title>
      <link rel="stylesheet" href="style.css">
</head>
<body id="contenu">
    
    <div class="detail">

        <h2>Details des taches</h2>
          
        <div class="taches">
            <span>Nom : </span> <span>
                <?= $tache_trouver["nom"] ;?>
            </span>
        </div>
        <div class="description">
            <span>Description : </span> <span>
              
                 <?= $tache_trouver["description"] ?>
            
            </span>
        </div>
        <div class="date">
            <span>Date de la tache : </span> <span>
                <?= $tache_trouver["date"]?>
            </span>
        </div>
        <div class="heure">
            <span>Heure de la tache : </span> <span>
                <?= $tache_trouver["heure"] ?>
            </span>
        </div>
       
       <a href="index.php">Retour </a>

      

    </div>


</body>
</html>
    
    
    