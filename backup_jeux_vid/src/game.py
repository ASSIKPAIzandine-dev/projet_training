import pygame
from sprites.cat import Cat
from sprites.mouse import Mouse
from typing import List

class Game:
        screen:pygame.Surface=None
        clock:pygame.time.Clock=None
        def __init__(self,title:str,size:tuple):
                pygame.init()

                self.screen=pygame.display.set_mode(size)
                pygame.display.set_caption(title)
                self.clock=pygame.time.Clock()
            
                #self.cat=Cat()
            
                self.cats_group=pygame.sprite.Group()
                self.cat=Cat((500,500))
                self.cats_group.add(self.cat)

                self.mouses_group=pygame.sprite.Group()
                self.mouses_group.add(Mouse((100,150)))
                
                self.font=pygame.font.Font("./src/sprites/mon_font",15)
                self.font.render("Score",True,(255,0,0))
                
        def update_game(self):
                print("update game")
                      
        def play_music(self):
                pygame.mixer.init()
                pygame.mixer.music.load("/home/izandine/jeux_video/src/musiques/play.mp3")
                pygame.mixer.music.play(loops=-1)
          
        def Game_run_loop(self):
            self.play_music()
            self.cats_group.update()
            running = True

            while running:    
                for event in pygame.event.get():                
                    if event.type == pygame.QUIT:
                        running = False

                self.screen.fill("white")
                self.cats_group.draw(self.screen)
                self.mouses_group.draw(self.screen)
                  
                pygame.display.flip()
                self.clock.tick(40)

# # quiter le jeux
        pygame.quit()

       
        
        
