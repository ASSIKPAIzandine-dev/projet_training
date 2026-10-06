<?php
namespace App\Controllers;


interface CRUD{
        
    public function index();

    public function deleteAction($id);

    public function editForm($id);
    
    public function updateAction($id);

    public function show ($id);

    public function createForm();

    public function storeAction();














}