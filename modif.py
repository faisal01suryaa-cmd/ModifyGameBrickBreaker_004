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