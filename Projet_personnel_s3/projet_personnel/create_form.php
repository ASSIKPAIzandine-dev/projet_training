
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="index.css">

</head>
<body  style="font-size:0.9em;">
    

    <a href="http://localhost:8000">
        
    </a>

    <h2>Enregistrement du produit</h2>
    
  
    <form action="index.php" method="post">
        <fieldset style="width: 50%;"  class="mon-fieldset">
            <legend>Formulaire d'enregistrement</legend>
           <div class="champ">
            
           <div class="libelle">
                <label for="libelle">Libelle</label><br>
                <input class="entre" type="text" name="libelle" id="libelle" placeholder="libelle"><br>

            </div>

            <div class="description">
                <label for="description">Description</label><br>
                <textarea class="entre" name="description" id="description" placeholder="description"
                    cols="24"></textarea>
            </div>

            <div class="prixUnit">
                <label for="prixUnit">Prix unitaire</label><br>
                <input class="entre" type="number" name="prixUnit" id="prixUnit" placeholder="prixUnit"><br>
            </div>

            <div class="qtite">
                <label for="quantite">Quantite</label><br>
                <input class="entre" type="number" name="quantite" id="quantite" placeholder="quantite"><br>
            </div>

            <div class="disponible">
                <label for="disponible">Disponible</label>
                <input class="entre" type="checkbox" name="disponible" id="disponible" placeholder="disponible"><br>
            </div><br>

            <input class="btn" type="submit" value="Enregistrer">
            </div>
        </fieldset>
        <a href="index.php">retour a la page précédente</a>
      
    </form>

 </body>
</html>

