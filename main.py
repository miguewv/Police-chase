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
    


    # --- SMART BANDIT AI ---
    # Calculate the desired escape direction (away from player)
    escape_x = 0
    escape_y = 0
    
    if bandit_x < player_x:
        escape_x = -bandit_speed  # flee left
    elif bandit_x > player_x:
        escape_x = bandit_speed   # flee right
        
    if bandit_y < player_y:
        escape_y = -bandit_speed  # flee up
    elif bandit_y > player_y:
        escape_y = bandit_speed   # flee down

    # Check if bandit is near walls (define a margin)
    WALL_MARGIN = 5
    near_left = bandit_x <= WALL_MARGIN
    near_right = bandit_x >= SCREEN_WIDTH - bandit_size - WALL_MARGIN
    near_top = bandit_y <= WALL_MARGIN
    near_bottom = bandit_y >= SCREEN_HEIGHT - bandit_size - WALL_MARGIN

    # Smart corner escape: if stuck in corner, slide along the wall
    # Check if trying to escape into a wall
    would_hit_left = near_left and escape_x < 0
    would_hit_right = near_right and escape_x > 0
    would_hit_top = near_top and escape_y < 0
    would_hit_bottom = near_bottom and escape_y > 0

    # If would hit horizontal wall, cancel horizontal movement and boost vertical
    if would_hit_left or would_hit_right:
        escape_x = 0
        # If also stuck vertically, pick a perpendicular escape direction
        if escape_y == 0:
            # Move away from player vertically
            if player_y < SCREEN_HEIGHT / 2:
                escape_y = bandit_speed  # go down
            else:
                escape_y = -bandit_speed  # go up

    # If would hit vertical wall, cancel vertical movement and boost horizontal
    if would_hit_top or would_hit_bottom:
        escape_y = 0
        # If also stuck horizontally, pick a perpendicular escape direction
        if escape_x == 0:
            # Move away from player horizontally
            if player_x < SCREEN_WIDTH / 2:
                escape_x = bandit_speed  # go right
            else:
                escape_x = -bandit_speed  # go left

    # Apply the escape movement
    bandit_x += escape_x
    bandit_y += escape_y

    # Final boundary clamp (safety net)
    if bandit_x < 0:
        bandit_x = 0
    if bandit_x > SCREEN_WIDTH - bandit_size:
        bandit_x = SCREEN_WIDTH - bandit_size
    if bandit_y < 0:
        bandit_y = 0
    if bandit_y > SCREEN_HEIGHT - bandit_size:
        bandit_y = SCREEN_HEIGHT - bandit_size


    # Get pressed keys (arrows)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Get pressed keys (ZQSD - French keyboard)
    if keys[pygame.K_q]:
        player_x -= player_speed
    if keys[pygame.K_d]:
        player_x += player_speed
    if keys[pygame.K_z]:
        player_y -= player_speed
    if keys[pygame.K_s]:
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