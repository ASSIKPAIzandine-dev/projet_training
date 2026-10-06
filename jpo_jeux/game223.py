
import pygame
import random
import sys

pygame.init()

LARGEUR, HAUTEUR = 1500, 1000
OBSTACLE_LARGEUR, OBSTACLE_HAUTEUR = 70, 30
VITESSE_JOUEUR = 7
VITESSE_OBSTACLE = 10
JOUEUR_TAILLE = 50
FPS = 80
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
BLEU = (0, 0, 255)
running=True

ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("JEU D'OBSTACLES")
horloge = pygame.time.Clock()

JOUEUR_X = LARGEUR // 2 - JOUEUR_TAILLE // 2
JOUEUR_Y = HAUTEUR - JOUEUR_TAILLE - 20
obstacles = []
score = 0
game_over = False
font = pygame.font.SysFont(None, 36)

def creer_obstacle():
    x = random.randint(0, LARGEUR - OBSTACLE_LARGEUR)
    y = -OBSTACLE_HAUTEUR
    obstacles.append(pygame.Rect(x, y, OBSTACLE_LARGEUR, OBSTACLE_HAUTEUR))

def afficher_score():
    texte = font.render("Score : {}".format(score), True, NOIR)
    ecran.blit(texte, (10, 10))

def afficher_game_over():
    # Correction des guillemets ici
    texte = font.render("GAME OVER ! Appuyez sur R pour rejouer", True, ROUGE)
    ecran.blit(texte, (LARGEUR // 2 - 250, HAUTEUR // 2))

while running:
    # 1. GESTION DES ÉVÉNEMENTS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
        
        if event.type == pygame.KEYDOWN and game_over:
            if event.key == pygame.K_r:
                # Réinitialisation
                obstacles = []
                score = 0
                game_over = False
                JOUEUR_X = LARGEUR // 2 - JOUEUR_TAILLE // 2

    if not game_over:
        # Déplacement du joueur
        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT] and JOUEUR_X > 0:
            JOUEUR_X -= VITESSE_JOUEUR
            
        if touches[pygame.K_RIGHT] and JOUEUR_X < LARGEUR - JOUEUR_TAILLE:
            JOUEUR_X += VITESSE_JOUEUR

        # Création aléatoire d'obstacles
        if random.random() < 0.03: 
            creer_obstacle()

        # Mouvement et collision
        JOUEUR_rect = pygame.Rect(JOUEUR_X, JOUEUR_Y, JOUEUR_TAILLE, JOUEUR_TAILLE)
        for obstacle in obstacles[:]:
            obstacle.y += VITESSE_OBSTACLE  # Faire descendre l'obstacle
            
            # Si l'obstacle sort de l'écran
            if obstacle.y > HAUTEUR:
                obstacles.remove(obstacle)
                score += 1
            
            # Collision
            if JOUEUR_rect.colliderect(obstacle):
                game_over = True

    # 3. AFFICHAGE
    ecran.fill("green")
    
    # Dessiner le joueur
    pygame.draw.rect(ecran, BLEU, (JOUEUR_X, JOUEUR_Y, JOUEUR_TAILLE, JOUEUR_TAILLE))
    
    # Dessiner les obstacles
    for obstacle in obstacles:
        pygame.draw.rect(ecran, ROUGE, obstacle)
    
    afficher_score()
    
    if game_over:
        afficher_game_over()

    pygame.display.flip()
    horloge.tick(FPS)
      

 
                
    









    
            



pygame.quit()
