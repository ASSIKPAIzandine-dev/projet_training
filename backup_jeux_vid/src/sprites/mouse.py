import pygame

class Mouse(pygame.sprite.Sprite):
        image:pygame.Surface=None
        rect:pygame.Rect=None
         
        def __init__(self,position):
            super().__init__()
            self.load_sprite_sheet() 
      
        def update(self):
            super().update()
            
        
        def load_sprite_sheet(self):
            self.image=pygame.image.load("/home/izandine/jeux_video/src/images/food.jpg").convert_alpha()
            
    
    

