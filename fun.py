import pygame
import sys
import math

pygame.init()

WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Anime Fighting Game")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 70, 70)
BLUE = (70, 70, 220)
GREEN = (60, 200, 100)
YELLOW = (255, 220, 100)

GROUND_Y = HEIGHT - 50

class Fighter:
    def __init__(self, x, color, controls, facing):
        self.x = x
        self.y = GROUND_Y
        self.color = color
        self.controls = controls
        self.facing = facing
        self.vel_y = 0
        self.on_ground = True
        self.health = 100
        self.attack_timer = 0

    def move(self, keys):
        speed = 5
        if keys[self.controls["left"]]:
            self.x -= speed
            self.facing = -1
        if keys[self.controls["right"]]:
            self.x += speed
            self.facing = 1
        if keys[self.controls["jump"]] and self.on_ground:
            self.vel_y = -15
            self.on_ground = False
        if keys[self.controls["attack"]] and self.attack_timer == 0:
            self.attack_timer = 20

    def apply_physics(self):
        self.vel_y += 1
        self.y += self.vel_y
        if self.y >= GROUND_Y:
            self.y = GROUND_Y
            self.vel_y = 0
            self.on_ground = True

        if self.attack_timer > 0:
            self.attack_timer -= 1

    def body_rect(self):
        return pygame.Rect(self.x - 20, self.y - 90, 40, 70)

    def attack_rect(self):
        if self.attack_timer > 10:
            return pygame.Rect(
                self.x + self.facing * 30,
                self.y - 70,
                40,
                20
            )
        return None

    def draw(self):
        # Aura
        if self.attack_timer > 0:
            pygame.draw.circle(screen, YELLOW, (self.x, self.y - 60), 45, 3)

        # Hair (spiky)
        for i in range(-2, 3):
            pygame.draw.polygon(
                screen,
                BLACK,
                [
                    (self.x + i * 6, self.y - 120),
                    (self.x + i * 6 + 4, self.y - 100),
                    (self.x + i * 6 - 4, self.y - 100),
                ],
            )

        # Head
        pygame.draw.circle(screen, self.color, (self.x, self.y - 100), 14)

        # Eyes (anime big eyes)
        pygame.draw.circle(screen, BLACK, (self.x - 5, self.y - 102), 3)
        pygame.draw.circle(screen, BLACK, (self.x + 5, self.y - 102), 3)

        # Torso
        pygame.draw.rect(screen, self.color, (self.x - 15, self.y - 85, 30, 45))

        # Legs
        pygame.draw.line(screen, self.color, (self.x - 8, self.y - 40), (self.x - 8, self.y), 4)
        pygame.draw.line(screen, self.color, (self.x + 8, self.y - 40), (self.x + 8, self.y), 4)

        # Arm
        arm_y = self.y - 65
        pygame.draw.line(
            screen,
            self.color,
            (self.x, arm_y),
            (self.x + self.facing * 25, arm_y),
            4
        )

        # Energy slash
        atk = self.attack_rect()
        if atk:
            pygame.draw.ellipse(screen, YELLOW, atk)

# Controls
controls_p1 = {
    "left": pygame.K_a,
    "right": pygame.K_d,
    "jump": pygame.K_w,
    "attack": pygame.K_f
}

controls_p2 = {
    "left": pygame.K_LEFT,
    "right": pygame.K_RIGHT,
    "jump": pygame.K_UP,
    "attack": pygame.K_RCTRL
}

p1 = Fighter(250, RED, controls_p1, 1)
p2 = Fighter(650, BLUE, controls_p2, -1)

font = pygame.font.SysFont(None, 40)

while True:
    clock.tick(60)
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    p1.move(keys)
    p2.move(keys)

    p1.apply_physics()
    p2.apply_physics()

    atk1 = p1.attack_rect()
    atk2 = p2.attack_rect()

    if atk1 and atk1.colliderect(p2.body_rect()):
        p2.health -= 1

    if atk2 and atk2.colliderect(p1.body_rect()):
        p1.health -= 1

    pygame.draw.rect(screen, GREEN, (0, GROUND_Y, WIDTH, 50))

    p1.draw()
    p2.draw()

    pygame.draw.rect(screen, RED, (50, 30, p1.health * 2, 20))
    pygame.draw.rect(screen, BLUE, (WIDTH - 250, 30, p2.health * 2, 20))

    if p1.health <= 0:
        screen.blit(font.render("Player 2 Wins!", True, BLACK), (360, 240))
    if p2.health <= 0:
        screen.blit(font.render("Player 1 Wins!", True, BLACK), (360, 240))

    pygame.display.update()
