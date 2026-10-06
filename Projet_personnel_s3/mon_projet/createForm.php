
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TO DO_LIST </title>
    <link rel="stylesheet" href="style.css">
</head>

<body class="body2" id="bdy">

<h1 class="titre">ENREGISTREMENT D'UNE TACHE  </h1>
    <form action="index.php" method="post" class="forme" id="formes">
    <fieldset style="width: 50%;" class="mon-fieldset">
        <legend class="ma_legende">Créer une nouvelle tâche</legend>

        <div class="mon_champ">
            <div class="nom_tache">
                <label for="nom">Nom</label><br>
                <input class="saisie" type="text" name="nom" id="nom" placeholder="nom"><br> 
            </div>
           
            <div class="description">
                <label for="description">Description de la  tâche</label><br>
                <textarea class="saisie" name="description" id="description" placeholder="description" cols="15"></textarea> <br> 
            --
            </div>

            <div class="date">
                <label for="date">Date d’échéance :</label> <br>
                <input type="date" id="date" name="date" class="saisie" >
            </div>
            
            <div class="heure">
                <label for="heure">Heure de la tache</label><br>
                <input class="saisie" type="time" name="heure" id="heure" placeholder="heure"><br>  <br>
            </div>

            
            <div class="bouton">

                <input type="submit" value="Envoyer"><br>
                
            </div>


        </form>

        </div>

  
    </fieldset>
    <a href="index.php" class="monLien">retour a la page précédente</a>
  </form>

  <script>
         
     let monBody=document.body;

     let changerCouleur=function (event){
   
    if(event.detail==1){
        monBody.style.backgroundColor="orange";

    }else if( event.detail==2) {
        monBody.style.backgroundColor="rgba(0, 255, 13, 1)";

    } else {
        monBody.style.backgroundColor="green";
        
    }
}

 
monBody.addEventListener("click",changerCouleur);

const element = document.querySelector("#formes"); 
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