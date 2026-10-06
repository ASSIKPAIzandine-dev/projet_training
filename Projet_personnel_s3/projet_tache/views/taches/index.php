<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>page Accueil</title>
</head>
<body>
      <h1>TO DO LIST</h1>
    <table border="2" >
        <thead >
            <th>nom_de_la_tache</th>
            <th>Description de la tache</th>
            <th>DateEcheance</th>
            <th>Heure</th>
            <th>Action</th>
        </thead>
            <tbody>
                <?php foreach ($listeTache as $liste) : ?>
                 <td> <?= $liste["nom"] ?>  </td>
                  <td> <?= $liste["description"] ?>  </td>
                 <td> <?= $liste["dateEcheance"] ?>  </td>
                 <td> <?= $liste["heure"] ?>  </td>
                <td>
                    <button type="submit">UPDATE</button>
                    <button type="submit">DELETE</button>
                    <button type="submit">SHOW</button>
                     

                </td>
                


            </tbody>
          
    <?php endforeach ;?>
    </table>
    <a href=""><button type="submit">Ajouter une tache</button> </a>

</body>
</html>