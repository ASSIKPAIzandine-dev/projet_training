import pygame
import time
# initialisation du jeux
pygame.init()

# definition de la fenetre ie la surface
screen=pygame.display.set_mode((1080,720))
pygame.display.set_caption("COURS DE JEUX VIDEO N°2")

clock=pygame.time.Clock()
running=True
current_x=0
current_y=0
direction=1



while running:
    # parcourrir les evenements
    for event in pygame.event.get():
         if event.type==pygame.QUIT:
             running=False
    
    # updates 
    screen.fill("green")
    
    surface=pygame.Surface((100,100))
    surface_rec=surface.get_rect(top=50)
    surface_rec.left=60
    # print(surface_rec)
    
    screen.blit(surface,(0,0))
    
    # image
    
    logo=pygame.image.load('./images/logo.png')
    surface_rec_logo=logo.get_rect()
    
    screen_with=screen.get_width()
    screen_heigh=screen.get_height()
    
    screen.blit(logo,surface_rec_logo)
    
    personnage=pygame.Surface((150,150))
    personnage.fill("blue")
    
    personnage_with=personnage.get_width()
    personnage_heigth=personnage.get_height()
    
    # x=(screen_with //2)-(personnage_with//2)
    # y=(screen_heigh //2)-(personnage_heigth//2)
    

    
    screen.blit(personnage,(current_x,current_y))
    vitesse=10
    current_x+= vitesse*direction 
    
    
    if current_x == (screen_with-personnage_with):
         direction=-1
    if(current_x==0):
        direction=1
   
        
        
    
    
    
    # render
    pygame.display.flip()
    clock.tick(60)



# quiter le jeux
pygame.quit()
