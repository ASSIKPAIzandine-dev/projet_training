<?php
namespace App\Controllers;

class Controller{
 
    public function render($path,$data=[]){
        extract($data);
        require __DIR__. "/../../views/".$path;
    }


















}