# Followed instructions by TechWithTim on YouTube
import pygame
import os 

# Sets display
WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!") 

# Sets background
PURPLE = (230, 230, 250)
BLACK = (0, 0, 0)
BLUE = (0, 0, 250)
PINK = (0, 0, 0)

BORDER = pygame.Rect((WIDTH-5)//2, 0, 10, HEIGHT)

# Sets FPS constant variable
FPS = 60 
VELO = 5
BULLET_VELO = 10
MAX_BULLETS = 5 

SHIP_WIDTH, SHIP_HEIGHT = 50, 50

PLAYER_1_HIT = pygame.USEREVENT + 1 
PLAYER_2_HIT = pygame.USEREVENT + 2 

# Player 1 spaceship 
PLAYER_1 = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
PLAYER_1 = pygame.transform.rotate(pygame.transform.scale(PLAYER_1, (SHIP_WIDTH, SHIP_HEIGHT)), 90) # Changes size and rotation

# Player 2 spaceship
PLAYER_2 = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
PLAYER_2 = pygame.transform.rotate(pygame.transform.scale(PLAYER_2, (SHIP_WIDTH, SHIP_HEIGHT)), 270) # Changes size and rotation



# Function to draw display
def draw_window(player_1, player_2, player_1_bullets, player_2_bullets):
    # Background 
    WIN.fill(PURPLE)

    # Border 
    pygame.draw.rect(WIN, BLACK, BORDER)

    # Player 1 
    WIN.blit(PLAYER_1, (player_1.x, player_1.y))

    # Player 2 
    WIN.blit(PLAYER_2, (player_2.x, player_2.y))
    pygame.display.update()

    # Player 1 Bullets 
    for bullet in player_1_bullets:
        pygame.draw.rect(WIN, BLUE, bullet)
    
    # PLayer 2 Bullets 
    for bullet in player_2_bullets:
        pygame.draw.rect(WIN, PINK, bullet)



def player_1_movement(keys_pressed, player_1):
        # Player 1 Movement 
        if keys_pressed[pygame.K_w] and player_1.y - VELO > 0: # Up 
            player_1.y -= VELO 
        if keys_pressed[pygame.K_a] and player_1.x - VELO > 0: # Left
            player_1.x -= VELO 
        if keys_pressed[pygame.K_s] and player_1.y + VELO + player_1.height < HEIGHT: # Down
            player_1.y += VELO
        if keys_pressed[pygame.K_d] and player_1.x + VELO + player_1.width < BORDER.x: # Right 
            player_1.x += VELO

def player_2_movement(keys_pressed, player_2):
        # Player 2 Movement 
        if keys_pressed[pygame.K_UP] and player_2.y - VELO > 0: # Up 
            player_2.y -= VELO 
        if keys_pressed[pygame.K_LEFT] and player_2.x - VELO > BORDER.x + BORDER.width: # Left
            player_2.x -= VELO 
        if keys_pressed[pygame.K_DOWN] and player_2.y + VELO + player_2.height < HEIGHT: # Down
            player_2.y += VELO
        if keys_pressed[pygame.K_RIGHT] and player_2.x + VELO + player_2.width < WIDTH: # Right 
            player_2.x += VELO


def handle_bullets(player_1_bullets, player_2_bullets, player_1, player_2):
    for bullet in player_1_bullets: 
        bullet.x += BULLET_VELO
        if player_2.colliderect(bullet):
            pygame.event.post(pygame.event.Event(PLAYER_2_HIT))
            player_1_bullets.remove(bullet)
    
    for bullet in player_2_bullets: 
        bullet.x -= BULLET_VELO
        if player_1.colliderect(bullet):
            pygame.event.post(pygame.event.Event(PLAYER_1_HIT))
            player_2_bullets.remove(bullet)


def main():

    player_1 = pygame.Rect(10, 362, SHIP_WIDTH, SHIP_HEIGHT)
    player_2 = pygame.Rect(690, 362, SHIP_WIDTH, SHIP_HEIGHT)

    player_1_bullets = []
    player_2_bullets = []

    clock = pygame.time.Clock()
    running = True 
    while running:
        # Ensures will not go past 60hz
        clock.tick(FPS)
        # Quits game if hit x 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Monitors the bullet mechanic
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(player_1_bullets) <= MAX_BULLETS:
                    bullet = pygame.Rect(player_1.x + player_1.width, player_1.y + player_1.height // 2 - 3, 10, 5)
                    player_1_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(player_2_bullets) <= MAX_BULLETS:
                    bullet = pygame.Rect(player_2.x, player_2.y + player_2.height // 2 - 3, 10, 5)
                    player_2_bullets.append(bullet)


        keys_pressed = pygame.key.get_pressed()
        player_1_movement(keys_pressed, player_1)
        player_2_movement(keys_pressed, player_2)

        handle_bullets(player_1_bullets, player_2_bullets, player_1, player_2) 

        draw_window(player_1, player_2, player_1_bullets, player_2_bullets)

    pygame.quit()


if __name__ == "__main__":
    main()
