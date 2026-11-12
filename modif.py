import pygame
import random

pygame.init()

WIDTH, HEIGHT = 700, 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Color Block Breaker")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

BLACK = (15, 15, 30)
WHITE = (255, 255, 255)
RED = (255, 70, 70)
GREEN = (70, 255, 120)
BLUE = (70, 140, 255)
YELLOW = (255, 220, 70)
PURPLE = (180, 80, 255)
PINK = (255, 80, 180)
CYAN = (70, 240, 255)

COLORS = [RED, GREEN, BLUE, YELLOW, PURPLE, PINK]

class Paddle:
    def __init__(self):
        self.rect = pygame.Rect(290, 500, 120, 18)
        self.speed = 8

    def move(self, direction):
        self.rect.x += direction * self.speed

        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH

    def draw(self):
        pygame.draw.rect(
            screen,
            CYAN,
            self.rect,
            border_radius=8
        )

class Ball:
    def __init__(self):
        self.radius = 9
        self.reset()

    def reset(self):
        self.x = WIDTH // 2
        self.y = 450
        self.dx = random.choice([-5, 5])
        self.dy = -5

    def move(self):
        self.x += self.dx
        self.y += self.dy

        if self.x <= self.radius:
            self.dx *= -1

        if self.x >= WIDTH - self.radius:
            self.dx *= -1

        if self.y <= self.radius:
            self.dy *= -1

        return self.y > HEIGHT

    def draw(self):
        pygame.draw.circle(
            screen,
            WHITE,
            (int(self.x), int(self.y)),
            self.radius
        )

    def get_rect(self):
        return pygame.Rect(
            self.x - self.radius,
            self.y - self.radius,
            18,
            18
        )

class Block:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 60, 25)
        self.color = random.choice(COLORS)

        self.shape = random.choice([
            "box",
            "circle",
            "diamond"
        ])

        self.health = random.choice([1, 1, 1, 2])

    def draw(self):
        if self.shape == "box":
            pygame.draw.rect(
                screen,
                self.color,
                self.rect,
                border_radius=5
            )

        elif self.shape == "circle":
            pygame.draw.ellipse(
                screen,
                self.color,
                self.rect
            )

        else:
            points = [
                (self.rect.centerx, self.rect.top),
                (self.rect.right, self.rect.centery),
                (self.rect.centerx, self.rect.bottom),
                (self.rect.left, self.rect.centery)
            ]

            pygame.draw.polygon(
                screen,
                self.color,
                points
            )

        if self.health == 2:
            pygame.draw.rect(
                screen,
                WHITE,
                self.rect,
                2
            )


def create_blocks():
    blocks = []

    for row in range(5):
        for col in range(9):
            x = 30 + col * 72
            y = 70 + row * 40

            blocks.append(Block(x, y))

    return blocks

def game_over(score):
    while True:
        screen.fill(BLACK)

        text = font.render(
            "GAME OVER - Score: " + str(score),
            True,
            RED
        )

        info = font.render(
            "SPACE = Restart | ESC = Exit",
            True,
            WHITE
        )

        screen.blit(
            text,
            text.get_rect(center=(350, 240))
        )

        screen.blit(
            info,
            info.get_rect(center=(350, 290))
        )

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return True

                if event.key == pygame.K_ESCAPE:
                    return False