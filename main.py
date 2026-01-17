import pygame
import sys

# --- 1. SETUP ---
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Police Chase")

# Colors (RGB)
BLACK = (0, 0, 0)
POLICE_BLUE = (0, 0, 255)
THIEF_RED = (255, 0, 0)

# Player variables (The Police)
player_x = 400
player_y = 300
player_size = 50
player_speed = 5

# Bandit variables (The Thief)
bandit_x = 100
bandit_y = 100
bandit_size = 50
bandit_speed = 3

# Clock to control FPS
clock = pygame.time.Clock()

# --- 2. THE GAME LOOP ---
running = True
while running:
    
    # A. Event Handling (Input)
    # -------------------------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get pressed keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # B. Game Logic (Update)
    # ----------------------
    # Keep player inside the screen (Boundary check)
    if player_x < 0:
        player_x = 0
    if player_x > SCREEN_WIDTH - player_size:
        player_x = SCREEN_WIDTH - player_size
        
    if player_y < 0:
        player_y = 0
    if player_y > SCREEN_HEIGHT - player_size:
        player_y = SCREEN_HEIGHT - player_size

    # C. Drawing (Render)
    # -------------------
    screen.fill(BLACK) # 1. Clear screen
    
    # 2. Draw the player (The Police)
    pygame.draw.rect(screen, POLICE_BLUE, [player_x, player_y, player_size, player_size])

    # 2. Draw the bandit (The Thief)
    pygame.draw.rect(screen, THIEF_RED, [bandit_x, bandit_y, bandit_size, bandit_size])

    # 3. Update the display
    pygame.display.flip()

    # 60 FPS
    clock.tick(60)

pygame.quit()
sys.exit()