<?php
use App\Controllers\TacheController;
$router=new AltoRouter();
$tache=new TacheController();

$router->map("GET","/",[$tache,"index"]);
$router->map("GET","/tache/[i:id]/detail",[$tache,"show"]);
$router->map("GET","/tache/create",[$tache,"createForm"]);
$router->map("POST","/tache",[$tache,"storeAction"]);

$router->map("GET","/tache/[i:id]/edit",[$tache,"editForm"]);
$router->map("POST","/tache/[i:id]/update",[$tache,"updateAction"]);

$router->map("POST","/tache/[i:id]/delete",[$tache,"deleteAction"]);

   $match = $router->match();
    if( is_array($match) && is_callable( $match['target'] ) ) {
	    call_user_func_array( $match['target'], $match['params'] );
    } else {
        // no route was matched
        header( $_SERVER["SERVER_PROTOCOL"] . ' 404 Not Found');
    }
?>
