<?php
  require 'utils/files.php';
  $taches=readJson();
  
  $nom= htmlspecialchars($_POST["nom"]); 
  $description= htmlspecialchars($_POST["description"]);
  $date= htmlspecialchars($_POST["date"]);
  $heure= htmlspecialchars($_POST["heure"]);
 
//<input type="reset" value="Réinitialiser">

$tache=[  
        "nom"=>$nom,
        "description"=>$description,
        "date"=>$date,
        "heure"=>$heure
];
            
 //ar_dump($tache);
  
   $valid=1;
  // if (empty($nom) || empty($description) || empty($date)|| empty(heure) || $date<0 || $heure<0 ){

  if (empty($nom) || empty($description)  || $date<0 || $heure<0 ){
    
    
    $valid=0;
  };       
        
    if($valid){
        $taches[]=$tache;
       
        writeJson($taches);
        //var_dump($taches);
   
    }  
 
?>

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>To_do_list</title>
  <link rel="stylesheet" href="style.css">

  
</head>
<body class="monBody">
     
     
    <div class="tables">
      <h1 class="titre">listes des taches</h1>
      <table border="1" width="40%" class="matable" id="tables" >
            <thead>
                <tr>
                    <th>Nom</th>
                    <th>Description</th>
                    <th>Date</th>
                    <th>Heure</th>
                    <th>Action</th>
                    
                </tr>
            </thead>


             <tbody>
                
                <?php foreach($taches as $tach): ?>
                  
                  
                <tr>
                    <td>
                        <?= $tach["nom"] ?>
                        
                    </td>
                    <td>
                        <?= $tach["description"] ?>
                    </td>
                    <td>
                        <?= $tach["date"] ?>
                   </td>
                    <td>
                        <?= $tach["heure"]?>
                    </td>
                    <td><a href="http://localhost:8000/detail.php?nom=<?= $tach["nom"] ?>"><button>Consulter la tache</button></a><br>
                       <a href="http://localhost:8000/editerForm.php? nom=<?=$tach["nom"] ?>"><button>Editer la tache</button> </a><br>
                       <a href="http://localhost:8000/delete.php? nom=<?=$tach["nom"] ?>"><button>Supprimer la tache</button> </td>
                </tr>


                <?php endforeach ?>

            </tbody>

      </table>



  </div>
        <a class="monAjout"    href="http://localhost:8000/createForm.php?nom=<?= $tach["nom"] ?>"><button> <Strong>Ajouter une tache</Strong></button></a>

   <script>
      let monBody=document.body;

     let changerCouleur=function (event){
   
    if(event.detail==1){
        monBody.style.backgroundColor="orange";

    }else if( event.detail==2) {
        monBody.style.backgroundColor="rgba(87, 18, 81, 1)";

    } else {
        monBody.style.backgroundColor="green";
        
    }
}

monBody.addEventListener("click",changerCouleur);

const element = document.querySelector("#tables"); // ou "table"
element.style.position = "absolute";

let x = 0, y = 0;
const stepX = 3, stepY = 2;
const targetX = (window.innerWidth - element.offsetWidth) / 2;
const targetY = (window.innerHeight - element.offsetHeight) / 2;

function deplacer() {
    if (x < targetX) x += stepX;
    if (y < targetY) y += stepY;

    element.style.left = x + "px";
    element.style.top = y + "px";

    if (x >= targetX && y >= targetY) {
        // Arrêt au centre
        console.log("Arrivé au milieu !");
        return;
    }

    requestAnimationFrame(deplacer);
}

deplacer();   

    </script>

</body>
</html>