import pygame
import random

# Initialisation
pygame.init()

# --- PARAMÈTRES ---
LARGEUR, HAUTEUR = 1500, 1000 # Un peu plus petit pour mieux tenir sur les écrans
FPS = 60

# Couleurs stylisées
FOND = (10, 10, 30)       # Bleu nuit très sombre
COULEUR_JOUEUR = (0, 255, 255) # Cyan néon
COULEUR_OBSTACLE = (255, 0, 100) # Rose/Rouge néon
BLANC = (255, 255, 255)

# Joueur & Obstacles
JOUEUR_TAILLE = 40
VITESSE_JOUEUR = 10
OBST_LARGEUR, OBST_HAUTEUR = 60, 25
VITESSE_INITIALE = 6

# --- CONFIGURATION ÉCRAN ---
ecran = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("🌌 JEUX D'OBSTACLE ")
horloge = pygame.time.Clock()
font_score = pygame.font.SysFont("Arial", 30, bold=True)
font_big = pygame.font.SysFont("Arial", 60, bold=True)

# --- CLASSES ---
class Etoile:
    def __init__(self):
        self.x = random.randint(0, LARGEUR)
        self.y = random.randint(0, HAUTEUR)
        self.vitesse = random.uniform(1, 4)
    def update(self):
        self.y += self.vitesse
        if self.y > HAUTEUR: self.y = 0

def dessiner_vaisseau(x, y):
    # Un triangle stylisé pour le joueur
    points = [(x + JOUEUR_TAILLE//2, y), (x, y + JOUEUR_TAILLE), (x + JOUEUR_TAILLE, y + JOUEUR_TAILLE)]
    pygame.draw.polygon(ecran, COULEUR_JOUEUR, points)
    # Aura lumineuse
    pygame.draw.polygon(ecran, COULEUR_JOUEUR, points, 2)

# --- VARIABLES DE JEU ---
def reset_game():
    return LARGEUR // 2, [], 0, False, VITESSE_INITIALE

etoiles = [Etoile() for _ in range(100)]
joueur_x, obstacles, score, game_over, vitesse_actuelle = reset_game()
running = True

# --- BOUCLE PRINCIPALE ---
while running:
    ecran.fill(FOND)
    
    # 1. Dessiner le fond étoilé
    for etoile in etoiles:
        etoile.update()
        pygame.draw.circle(ecran, (100, 100, 150), (int(etoile.x), int(etoile.y)), 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.KEYDOWN and game_over and event.key == pygame.K_r:
            joueur_x, obstacles, score, game_over, vitesse_actuelle = reset_game()

    if not game_over:
        # Contrôles
        touches = pygame.key.get_pressed()
        if touches[pygame.K_LEFT] and joueur_x > 0: joueur_x -= VITESSE_JOUEUR
        if touches[pygame.K_RIGHT] and joueur_x < LARGEUR - JOUEUR_TAILLE: joueur_x += VITESSE_JOUEUR

        # Difficulté progressive
        vitesse_actuelle = VITESSE_INITIALE + (score // 10)
        
        # Apparition obstacles
        if random.random() < 0.04:
            x = random.randint(0, LARGEUR - OBST_LARGEUR)
            obstacles.append(pygame.Rect(x, -OBST_HAUTEUR, OBST_LARGEUR, OBST_HAUTEUR))

        # Mise à jour obstacles
        rect_joueur = pygame.Rect(joueur_x, HAUTEUR - 70, JOUEUR_TAILLE, JOUEUR_TAILLE)
        for obs in obstacles[:]:
            obs.y += vitesse_actuelle
            if obs.y > HAUTEUR:
                obstacles.remove(obs)
                score += 1
            if rect_joueur.colliderect(obs):
                game_over = True

    # --- DESSIN ---
    # Dessiner obstacles avec bordure arrondie
    for obs in obstacles:
        pygame.draw.rect(ecran, COULEUR_OBSTACLE, obs, border_radius=7)
        pygame.draw.rect(ecran, BLANC, obs, 2, border_radius=7) # Bordure brillante

    # Joueur
    if not game_over:
        dessiner_vaisseau(joueur_x, HAUTEUR - 70)

    # UI (Score)
    s_txt = font_score.render(f"SCORE: {score}", True, BLANC)
    ecran.blit(s_txt, (20, 20))
    v_txt = font_score.render(f"SPEED: {int(vitesse_actuelle)}", True, COULEUR_JOUEUR)
    ecran.blit(v_txt, (20, 60))

    if game_over:
        # Overlay sombre
        surface_over = pygame.Surface((LARGEUR, HAUTEUR), pygame.SRCALPHA)
        surface_over.fill((0, 0, 0, 150))
        ecran.blit(surface_over, (0,0))
        
        msg = font_big.render("MISSION ÉCHOUÉE", True, COULEUR_OBSTACLE)
        retry = font_score.render("Appuyez sur 'R' pour retenter l'évasion", True, BLANC)
        ecran.blit(msg, (LARGEUR//2 - 250, HAUTEUR//2 - 50))
        ecran.blit(retry, (LARGEUR//2 - 230, HAUTEUR//2 + 30))

    pygame.display.flip()
    horloge.tick(FPS)

pygame.quit()
