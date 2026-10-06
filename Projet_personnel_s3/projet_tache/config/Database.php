<?php
namespace Config;

class Database{
        private static $instance =null;
        public $pdo=null;

        private  function __construct() {
            $dsn=__DIR__. "/../database/database.db";
            $this->pdo=new  \PDO("sqlite:".$dsn);
         

         }  
           

         public static function getInstance(){
            if(self::$instance===null){
                self::$instance=new self();
            }
            return self::$instance;
          }
        public static function initDB(){
            $instanceDatabase=self::getInstance();
            $ddl=__DIR__. "/../database/ddl.sql";
            $dml=__DIR__. "/../database/dml.sql";

            if(file_exists($ddl)){
                $sql=file_get_contents($ddl);
                $stmt=$instanceDatabase->pdo->exec($sql);
                echo "table inserer dans bd";
            }

            if(file_exists($dml)){
                $sql=file_get_contents($dml);
                $stmt=$instanceDatabase->pdo->exec($sql);
                echo "donnée inserer dans bd";
            }
        }


        
























}