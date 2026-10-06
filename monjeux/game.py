import pygame
from sprites.cat import Cat

class Game:
    screen:pygame.Surface=None
    clock:pygame.time.Clock=None
    def __init__(self,title:str,size:tuple):
        pygame.init()
        self.screen=pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        
        self.clock=pygame.time.Clock()
        self.cat=Cat()
        print(self.cat)
       

          
    def update(self):
          self.screen.fill("black")
          self.screen.blit(self.cat.image,self.cat.rect)
          
          keys=pygame.key.get_pressed()
          if(keys[pygame.K_RIGHT]):
                self.cat.move_right()
                
          if(keys[pygame.K_LEFT]):
                 self.cat.move_left()
          
          
           
    def Game_run_loop(self):
        running = True
        
        while running:    
            for event in pygame.event.get():                
                if event.type == pygame.QUIT:
                    running = False
                    
            self.update()     
            pygame.display.flip()
            self.clock.tick(40)
            



# # quiter le jeux
    pygame.quit()

       
        
        
