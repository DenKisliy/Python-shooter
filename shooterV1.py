from random import randint
import pygame
import sys

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = pygame.Color('grey')

GAME_FONT = pygame.font.Font(None, 30)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Cosmic shooter game")

FIGHTER_IMAGE = pygame.image.load('images/fighter.png')
FIGHTER_WIDTH, FIGHTER_HEIGHT = FIGHTER_IMAGE.get_size()
FIGHTER_STEP = 0.3

ALIEN_IMAGE = pygame.image.load('images/alien.png')
ALIEN_WIDTH, ALIEN_HEIGHT = ALIEN_IMAGE.get_size()
ALIEN_INCREASE_SPEED = 0.01
alien_spead = 0.1

BALL_IMAGE = pygame.image.load('images/rocket.png')
BALL_WIDTH, BALL_HEIGHT = BALL_IMAGE.get_size()
BALL_STEP = 0.5

fighter_x = SCREEN_WIDTH / 2 - FIGHTER_WIDTH / 2
fighter_y = SCREEN_HEIGHT - FIGHTER_HEIGHT

ball_x = fighter_x
ball_y = SCREEN_HEIGHT - FIGHTER_HEIGHT - BALL_HEIGHT / 2

alien_x = randint(0 , SCREEN_WIDTH - ALIEN_WIDTH)
alien_y = 0

right_move = False
left_move = False

fire_ball = False
ball_move = False

game_is_running = True
game_score = 0

def calculate_fighter_position():
    global fighter_x
    if right_move and fighter_x <= SCREEN_WIDTH - FIGHTER_WIDTH - FIGHTER_STEP:
        fighter_x += FIGHTER_STEP

    if left_move and fighter_x >= FIGHTER_STEP:
        fighter_x -= FIGHTER_STEP

def calculate_ball_position():
    global fighter_x
    global ball_x
    global ball_y
    global fire_ball
    global ball_move

    if ball_move and ball_y >= BALL_STEP:
        ball_y -= BALL_STEP

    if fire_ball:
        ball_y = SCREEN_HEIGHT - FIGHTER_HEIGHT - BALL_HEIGHT / 2 - BALL_STEP
        ball_x = fighter_x + FIGHTER_WIDTH / 2 - BALL_WIDTH / 2
        fire_ball = False
        ball_move = True

    if ball_y == 0:
        fire_ball = False
        ball_move = False

def calculate_alien_position():
    global alien_y
    global alien_x
    global fire_ball
    global ball_move
    global alien_spead
    global game_score

    alien_y += alien_spead

    if (alien_x - BALL_WIDTH / 2 <= ball_x <= alien_x + ALIEN_WIDTH + BALL_WIDTH / 2
            and alien_y - BALL_HEIGHT / 2 <= ball_y <= alien_y + ALIEN_HEIGHT + BALL_HEIGHT / 2 and ball_move):
        alien_x = randint(0, SCREEN_WIDTH - ALIEN_WIDTH)
        alien_y = 0
        fire_ball = False
        ball_move = False
        alien_spead += ALIEN_INCREASE_SPEED
        game_score += 1

while game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                right_move = True
            if event.key == pygame.K_LEFT:
                left_move = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                fire_ball = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right_move = False
            if event.key == pygame.K_LEFT:
                left_move = False

    calculate_fighter_position()
    calculate_ball_position()
    calculate_alien_position()

    screen.fill(SCREEN_COLOR)
    screen.blit(FIGHTER_IMAGE, (fighter_x, fighter_y))

    if ball_move:
        screen.blit(BALL_IMAGE, (ball_x, ball_y))

    screen.blit(ALIEN_IMAGE, (alien_x, alien_y))

    if alien_y > fighter_y - ALIEN_HEIGHT:
        game_is_running = False

    game_over_text = GAME_FONT.render(f"Your score is: { game_score }", True, 'white')

    screen.blit(game_over_text, (20, 20))

    pygame.display.update()

game_over_text = GAME_FONT.render("Game Over", True, 'white')
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
screen.blit(game_over_text, game_over_rectangle)

pygame.display.update()
pygame.time.wait(5000)
pygame.quit()