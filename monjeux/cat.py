import pygame
import os
print(os.getcwd)

class Cat(pygame.sprite.Sprite):
    
    image:pygame.Surface=None
    rect:pygame.Rect=None
    frames:list[pygame.Surface]
    current_cat_x=0
    
    def __init__(self):
        super().__init__()
        self.load_sprite_sheet()
        self.image = self.frames[0]
        self.rect=self.image.get_rect()
        
    def load_sprite_sheet(self):
            sprite_sheets=pygame.image.load("/home/izandine/jeux_video/src/images/cat_spritesheet.png").convert_alpha()
            FRAME_WITDH=204
            FRAME_HEIGH=204
            self.frames=[]

            # 0 a 2
            for i in range (3):
                 frame= sprite_sheets.subsurface((i*FRAME_WITDH,0,FRAME_WITDH,FRAME_HEIGH))
                 self.frames.append(frame)
                 
                 
    def move_right(self):
             self.rect.x+=10
       
    def move_left(self):
             self.rect.x-=10


        
        
        
        
        
        
        