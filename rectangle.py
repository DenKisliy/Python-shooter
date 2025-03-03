import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = pygame.Color('white')

RECT_WIDTH = 200
RECT_HEIGHT = 100
RECT_STEP = 10

rect_x = SCREEN_WIDTH / 2 - RECT_WIDTH / 2
rect_y = SCREEN_HEIGHT / 2 - RECT_HEIGHT / 2
rect_color = pygame.Color('blue')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My first game")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP and rect_y >= RECT_STEP:
                rect_y -= RECT_STEP
            if event.key == pygame.K_DOWN and rect_y <= SCREEN_HEIGHT - RECT_HEIGHT - RECT_STEP:
                rect_y += RECT_STEP
            if event.key == pygame.K_RIGHT and rect_x <= SCREEN_WIDTH - RECT_WIDTH - RECT_STEP:
                rect_x += RECT_STEP
            if event.key == pygame.K_LEFT and rect_x >= RECT_STEP:
                rect_x -= RECT_STEP

        screen.fill(SCREEN_COLOR)
        pygame.draw.rect(screen, rect_color, (rect_x, rect_y, RECT_WIDTH, RECT_HEIGHT))
        pygame.display.update()