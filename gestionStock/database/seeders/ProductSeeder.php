<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;
use Illuminate\Support\Facades\DB;

class ProductSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void{
        DB::table('products')->insert([
            [
            'label'=>'pc hp',
            'description'=>'pc puissant avec 8 GB de ram min',
            'price'=>95000,
            'quantity'=>5,
            'created_at'=>now(),
            'updated_at'=>now()
        ],

        [
            'label'=>'chargeur',
            'description'=>'chargeur du pc',
            'price'=>15000,
            'quantity'=>3,
            'created_at'=>now(),
            'updated_at'=>now()
        ],
         [
            'label'=>'portable',
            'description'=>'portable du dernier cri',
            'price'=>65000,
            'quantity'=>9,
            'created_at'=>now(),
            'updated_at'=>now()
        ]
]);
    
}



}
