import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Fighting Game")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 200)
GREEN = (0, 200, 0)

# Player settings
player1 = pygame.Rect(100, 250, 50, 100)
player2 = pygame.Rect(650, 250, 50, 100)

p1_health = 100
p2_health = 100

speed = 5
attack_cooldown = 0

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Player 1 controls (WASD + F)
    if keys[pygame.K_a]:
        player1.x -= speed
    if keys[pygame.K_d]:
        player1.x += speed
    if keys[pygame.K_f] and attack_cooldown == 0:
        if player1.colliderect(player2):
            p2_health -= 10
        attack_cooldown = 20

    # Player 2 controls (Arrow keys + L)
    if keys[pygame.K_LEFT]:
        player2.x -= speed
    if keys[pygame.K_RIGHT]:
        player2.x += speed
    if keys[pygame.K_l] and attack_cooldown == 0:
        if player2.colliderect(player1):
            p1_health -= 10
        attack_cooldown = 20

    if attack_cooldown > 0:
        attack_cooldown -= 1

    # Draw players
    pygame.draw.rect(screen, BLUE, player1)
    pygame.draw.rect(screen, RED, player2)

    # Draw health bars
    pygame.draw.rect(screen, GREEN, (50, 20, p1_health * 2, 20))
    pygame.draw.rect(screen, GREEN, (500, 20, p2_health * 2, 20))

    pygame.display.update()

pygame.quit()
sys.exit()
