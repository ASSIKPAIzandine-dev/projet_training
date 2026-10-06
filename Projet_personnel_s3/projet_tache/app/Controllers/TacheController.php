<?php
namespace App\Controllers;
 use App\Models\TacheModel;

class TacheController extends Controller implements CRUD{
      public function index(){
      $tacheModele= new TacheModel();
      //echo "page index";
      $listeTache = TacheModel::all();
      //print_r($listeTache);
      $this->render("taches/index.php",['listeTache'=>$listeTache]);


    }

    public function deleteAction($id){
        echo "page delete action";

    }

    public function editForm($id){
        echo "editForm";
    }
    public function updateAction($id){
        echo "update action";
    }

    public function show ($id){
         echo "show";
    }


    public function createForm(){
        echo "create";

    }
    public function storeAction(){
        echo "store action";
    }



















}