import pygame
import time
# initialisation du jeux
pygame.init()

# definition de la fenetre ie la surface
screen=pygame.display.set_mode((1080,720))
pygame.display.set_caption("COURS DE JEUX VIDEO N°3")

clock=pygame.time.Clock()
running=True
cat=pygame.image.load("./images/cat_spritesheet.png").convert_alpha()
# print(cat.get_rect())

FRAME_WITDH=204
FRAME_HEIGH=204

current_cat_x=0
frames=[]

# 0 a 2
for i in range (3):
     frame=cat.subsurface((i*FRAME_WITDH,0,FRAME_WITDH,FRAME_HEIGH))
     frames.append(frame)

    
# frame1=cat.subsurface((0,0,FRAME_WITDH,FRAME_HEIGH))
# frame2=cat.subsurface((204,0,FRAME_WITDH,FRAME_HEIGH))
# frame3=cat.subsurface((2*204,0,FRAME_WITDH,FRAME_HEIGH))

current_frame_index=0
while running:
    # parcourrir les evenements
    for event in pygame.event.get():
         if event.type==pygame.QUIT:
             running=False
        
    # updates 
    keys=pygame.key.get_pressed()
    if(keys[pygame.K_RIGHT]):
        print("KEY LEFT Pressed")
        current_frame_index +=1
        current_cat_x+=10
          
    if(current_frame_index>=len(frames)):
        current_frame_index=0   
    screen.fill("green")
    
    #  surface(frame1) et position x et y
    screen.blit(frames[current_frame_index],(current_cat_x,0))
    # i+=1
    # if(i>=0):
    #     i=0
        
    # screen.blit(frame2,(500,0))
    # screen.blit(frame3,(700,0))
    
    # render
    pygame.display.flip()
    clock.tick(10)

# quiter le jeux
pygame.quit()
