<?php
namespace App\Models;
use Config\Database;

class TacheModel extends Model{
  public static function all(){
    $instanceDatabase=Database::getInstance();
    
    $pdoI=$instanceDatabase->pdo;
    $stmt=$pdoI->prepare("select * from Tache");
    $stmt->execute();
    return $stmt->fetchAll();

    }
    public static function find($id){

    }
     public static function delete($id){

    }
     public static function create($array){

    }
     public static function update($array){

    }


}