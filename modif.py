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