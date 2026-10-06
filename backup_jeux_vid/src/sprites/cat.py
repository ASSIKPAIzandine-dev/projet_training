import pygame
import os
print(os.getcwd)

class Cat(pygame.sprite.Sprite):
    
        image:pygame.Surface=None
        rect:pygame.Rect=None
        frames:list[pygame.Surface]
        current_cat_x=0
        current_frame_index:int
    
        def __init__(self,position):
                super().__init__()
                self.load_sprite_sheet()     
                self.current_frame_index=0
                self.image = self.frames[self.current_frame_index]
                # self.position=position
                self.rect=self.image.get_rect()
                self.nb_eat_food=0
                
        def eat(self):
                if(list_souris):
                        self.nb_eat_food+=1
                        
        def update(self):
                super().update()
        
                keys=pygame.key.get_pressed()
                if(keys[pygame.K_RIGHT]):
                  self.move_right()
                  print("je suis dans update")  
                if(keys[pygame.K_LEFT]):
                  self.move_left()

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
                self.animate_right()
        
        def move_left(self):
            self.animated_left()

        def  animate_right(self):
        
                self.rect.x+=10
                self.current_frame_index+=1
                if(self.current_frame_index==len(self.frames)):
                    self.current_frame_index=0
                self.image = self.frames[self.current_frame_index]

        def animated_left(self):
                 self.rect.x-=10
                 self.current_frame_index+=1
                 if(self.current_frame_index==len(self.frames)):
                     self.current_frame_index=0
                 self.image = self.frames[self.current_frame_index]

             


        
        
        
        
        
        
        