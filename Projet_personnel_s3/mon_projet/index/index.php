<?php
    require 'utils/file.php';
    $produits=readJson();
    //var_dump($produits);
          
  $libelle= htmlspecialchars($_POST["libelle"]); 
  $description= htmlspecialchars($_POST["description"]);
  $prixUnit= htmlspecialchars($_POST["prixUnit"]);
  $quantite= htmlspecialchars($_POST["quantite"]);
  $disponible= htmlspecialchars($_POST["disponible"]);
  
 

 

 
 
  $produit= [   
            "libelle"=>$libelle,
            "description"=>$description,
            "prixUnit"=>$prixUnit,
            "quantite"=>$quantite,
            "disponible"=>$disponible,
  ];

   $valid=1;
  if (empty($libelle) || empty($prixUnit) || empty($quantite) || $quantite<0 || $prixUnit<0 ){
    $valid=0;
  };       
        
    if($valid){
        $produits[]=$produit;
        //var_dump($produits);
        writeJson($produits);
   
    }  
   
       
  
  

?>


<!DOCTYPE html>
<html lang="fr">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ecommerce</title>
    <!-- <link rel="stylesheet" href="style.css"> -->
 
</head>

<body>




    <a href="http://localhost:8001/create_form.php?libelle=<?= $produit["libelle"] ?>"><button>Ajouter les produits</button></a>
    
    <div class="liste_produits">
               
        <h2>Listes des produits</h2>

        <table border="1">
            <thead>
                <tr>
                    <th>Libelle</th>
                    <th>Prix</th>
                    <th>Quantite</th>
                    <th>Etat</th>
                    <th>Action</th>
                </tr>
            </thead>
            <tbody>
   
                <?php foreach($produits as $produit): ?>

                <tr>
                    <td>
                        <?= $produit["libelle"] ?>
                    </td>
                    <td>
                        <?= $produit["prixUnit"] ?>
                    </td>
                    <td>
                        <?= $produit["quantite"] ?>
                   </td>
                    <td>
                        <?= $produit["disponible"]?>
                    </td>
                    <td><a href="http://localhost:8001/details.php?libelle=<?= $produit["libelle"] ?>"><button>Consulter</button></a>
                       <a href="http://localhost:8001/edit_form.php? libelle=<?=$produit["libelle"] ?>"><button>Modifier</button> </a>
                       <button>Supprimer</button>
                      
                    
                    </td>
                </tr>


                <?php endforeach ?>

            </tbody>
        </table>

    </div>



</body>

</html>
