import pygame
import sys
import random

# --- 1. SETUP ---
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Police Chase")
startTime = pygame.time.get_ticks()

# Colors (RGB)
BLACK = (0, 0, 0)
POLICE_BLUE = (0, 0, 255)
THIEF_RED = (251, 112, 0)

# Player variables (The Police)
player_x = 400
player_y = 300
player_size = 50
player_speed = 5
Score = 0

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
    


    # if bandit is to the left of the player, move left
    if bandit_x < player_x:
        bandit_x -= bandit_speed
        
    # if bandit is below the player, move down
    if bandit_y < player_y:
        bandit_y -= bandit_speed

    # if bandit is to the right of the player, move right
    if bandit_x > player_x:
        bandit_x += bandit_speed

    # if bandit is above the player, move up
    if bandit_y > player_y:
        bandit_y -= bandit_speed



    # Keep bandit inside the screen (Boundary check)
    if bandit_x <= 0 or bandit_x >= SCREEN_WIDTH - bandit_size:
        if bandit_x < SCREEN_WIDTH / 2:
            bandit_x += bandit_speed
        else:
            bandit_x -= bandit_speed

    if bandit_y <= 0 or bandit_y >= SCREEN_HEIGHT - bandit_size:
        if bandit_y < SCREEN_HEIGHT / 2:
            bandit_y += bandit_speed
        else:
            bandit_y -= bandit_speed


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

    # Check for collision between player and bandit and update score
    if player_x < bandit_x + bandit_size and player_y < bandit_y + bandit_size and bandit_x < player_x + player_size and bandit_y < player_y + player_size:
        Score += 1
        # Reset bandit position
        bandit_x = random.randint(0, SCREEN_WIDTH - bandit_size)
        bandit_y = random.randint(0, SCREEN_HEIGHT - bandit_size)

    # C. Drawing (Render)
    # -------------------
    screen.fill(BLACK) # 1. Clear screen
    
    #Draw the player (The Police)
    pygame.draw.rect(screen, POLICE_BLUE, [player_x, player_y, player_size, player_size])

    #Draw the bandit (The Thief)
    pygame.draw.rect(screen, THIEF_RED, [bandit_x, bandit_y, bandit_size, bandit_size])

    #Draw the timer
    actualTime = pygame.time.get_ticks()
    elapsedTime = (actualTime - startTime) / 1000
    seconds = int(elapsedTime % 60)
    font = pygame.font.SysFont(None, 36)

    timerDraw = font.render(f"Time: {seconds}s", True, (255, 255, 255))
    screen.blit(timerDraw, (10, 10))

    #Draw the score
    scoreDraw = font.render(f"Score: {Score}", True, (255, 255, 255))
    screen.blit(scoreDraw, (10, 50))

    # 3. Update the display
    pygame.display.flip()

    # 60 FPS
    clock.tick(60)



pygame.quit()
sys.exit()