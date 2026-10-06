import pygame
import random

LARGEUR, HAUTEUR = 1800, 1600
FPS = 60
JOUEUR_TAILLE = 40
VITESSE_JOUEUR = 8

# Couleurs
FOND = (15, 15, 35)
CYAN = (0, 255, 255)
ROSE_NEON = (255, 0, 150)
VERT_NEON = (50, 255, 50)
BLANC = (255, 255, 255)
JAUNE = (255, 255, 0)

pygame.init()
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("JEUX D'OBSTACLE ⚡")
horloge = pygame.time.Clock()
police = pygame.font.SysFont("Arial", 30, bold=True)

def reset_jeu():
    # joueur_x, joueur_y, obs_v, obs_h, score, perdu, ancienne_vitesse
    return (LARGEUR // 2, HAUTEUR // 2, [], [], 0, False, 0)

# --- VARIABLES ---
joueur_x, joueur_y, obs_verticaux, obs_horizontaux, score, perdu, last_v_level = reset_jeu()
flash_timer = 0  # Pour l'effet visuel lors du changement de vitesse

running = True
while running:
    ecran.fill(FOND)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and perdu and event.key == pygame.K_r:
            joueur_x, joueur_y, obs_verticaux, obs_horizontaux, score, perdu, last_v_level = reset_jeu()

    if not perdu:
        # Calcul de la vitesse bonus basée sur le score
        vitesse_bonus = score // 20
        vitesse_actuelle = 6 + vitesse_bonus # Base de 6
        
        # Détection du changement de vitesse pour l'effet de flash
        if vitesse_bonus > last_v_level:
            last_v_level = vitesse_bonus
            flash_timer = 30 # Le texte restera jaune pendant 30 frames

        # 1. MOUVEMENT JOUEUR
        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT] and joueur_x > 0: joueur_x -= VITESSE_JOUEUR
        if touches[pygame.K_RIGHT] and joueur_x < LARGEUR - JOUEUR_TAILLE: joueur_x += VITESSE_JOUEUR
        if touches[pygame.K_UP] and joueur_y > 0: joueur_y -= VITESSE_JOUEUR
        if touches[pygame.K_DOWN] and joueur_y < HAUTEUR - JOUEUR_TAILLE: joueur_y += VITESSE_JOUEUR

        # 2. GÉNÉRATION OBSTACLES
        if random.random() < 0.04:
            obs_verticaux.append(pygame.Rect(random.randint(0, LARGEUR-30), -50, 30, 30))
        if random.random() < 0.03:
            obs_horizontaux.append(pygame.Rect(-50, random.randint(0, HAUTEUR-30), 30, 30))

        # 3. MISE À JOUR ET COLLISIONS
        rect_joueur = pygame.Rect(joueur_x, joueur_y, JOUEUR_TAILLE, JOUEUR_TAILLE)

        for obs in obs_verticaux[:]:
            obs.y += vitesse_actuelle
            if obs.y > HAUTEUR:
                obs_verticaux.remove(obs)
                score += 1
            if rect_joueur.colliderect(obs): perdu = True

        for obs in obs_horizontaux[:]:
            obs.x += (vitesse_actuelle - 1) # Un peu plus lent horizontalement
            if obs.x > LARGEUR:
                obs_horizontaux.remove(obs)
                score += 1
            if rect_joueur.colliderect(obs): perdu = True

    # --- DESSIN ---
    for obs in obs_verticaux:
        pygame.draw.rect(ecran, VERT_NEON, obs, border_radius=5)
    for obs in obs_horizontaux:
        pygame.draw.rect(ecran, ROSE_NEON, obs, border_radius=5)

    if not perdu:
        pygame.draw.rect(ecran, CYAN, rect_joueur, border_radius=8)
        pygame.draw.rect(ecran, BLANC, rect_joueur, 2, border_radius=8)

    # UI : Affichage Score et Vitesse
    txt_score = police.render(f"SCORE: {score}", True, BLANC)
    ecran.blit(txt_score, (20, 20))
    
    # Choix de la couleur de la vitesse (Flash jaune si changement)
    couleur_vitesse = JAUNE if flash_timer > 0 else CYAN
    if flash_timer > 0: flash_timer -= 1
    
    txt_speed = police.render(f"SPEED: {6 + (score // 20)}", True, couleur_vitesse)
    ecran.blit(txt_speed, (20, 60))

    if perdu:
        overlay = pygame.Surface((LARGEUR, HAUTEUR), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 180))
        ecran.blit(overlay, (0,0))
        msg = police.render("CRASH ! Appuie sur 'R' pour recommencer", True, BLANC)
        ecran.blit(msg, (LARGEUR//2 - 250, HAUTEUR//2))

    pygame.display.flip()
    horloge.tick(FPS)

pygame.quit()
