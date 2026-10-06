    <?php
              require 'utils/file.php';
              $produits=readJson();  
              
              $libelle= $_GET["libelle"]; 
              //var_dump($libelle);
              
              $produit_trouver=null;
              foreach ($produits as $produit ){
                                        if($produit["libelle"]===$libelle){
                                            $produit_trouver=$produit;
                                            
                                        }
                                        

              }
              //var_dump($produit_trouver);

             
             
             
             
             
             
             
             ?>




    
    
    
    
    
    <div class="detail">

        <h2>Details de produit</h2>
          
        <div class="libelle">
            <span>Libelle : </span> <span>
                <?= $produit_trouver["libelle"] ;?>
            </span>
        </div>
        <div class="description">
            <span>Description : </span> <span>
              
                 <?= $produit_trouver["description"] ?>
            
            </span>
        </div>
        <div class="prixUnit">
            <span>PrixUnit : </span> <span>
                <?= $produit_trouver["prixUnit"]?>
            </span>
        </div>
        <div class="quantite">
            <span>Quantite : </span> <span>
                <?= $produit_trouver["quantite"] ?>
            </span>
        </div>
        <div class="disponible">
            <span>Disponible : </span> <span>
                <?= $produit_trouver["disponible"] ?>
            </span>
        
        </div> <br>
       <a href="index.php">retour </a>
    </div>