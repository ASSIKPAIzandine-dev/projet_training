import pygame
import time
import random
# initialiser pygame
pygame.init()

# afficher la fenetre de pygame par la propriete et la taille est en pixel(px)
screen=pygame.display.set_mode((1080,720))
#print(sreen)
pygame.display.set_caption("COURS SUR JEUX VIDEO")


#maintenir la fenetre en vie
running=True
# creer un tabmleau de couleur a chaque rendu ca change de couleur aléatoire a chaque iteration

colors=["green","red","black","white","yellow","orange","blue"]
#  avoir un temps
deplacer=50
clock=pygame.time.Clock()

# print(clock)
# print(screen.get_rect())


# boucle de jeu while car on ne sait pas combien de fois on va iterer mais on connait qd on s'arrete
while running:
    # print(clock.get_fps())
    #listen events

    # print("pygame listen events :")
    # print(len(pygame.event.get()))

    #rechercher l'evenement et trouver event de la fenetre pour la fermer 
    for event in pygame.event.get():
         if event.type==pygame.QUIT:
             
                 # arreter le programe une fois que le type pygame est trouver
                 running=False
                 
    #modify state (modifier)
    screen.fill("red")
   
    surface=pygame.Surface((150,100))
    surface.fill("yellow")
    
    # depacer du gauche vers la droite
    deplacer+=100
    screen.blit(surface,(deplacer,50))  
    
     
      
    
           
    # choice=random.choice(colors)
    # screen.fill(choice) 
    #faire un nouveau rendu(render)
    pygame.display.flip()
    
    # mettre un temps pour chaque couleur d'image
    clock.tick(1)
        
pygame.quit()


 