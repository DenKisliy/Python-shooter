import pygame
import sys

import defaultValues
from fighter import Fighter
from ball import Ball
from alien import Alien

class Game:
    def __init__(self):
        self.game_is_running = True
        self.fighter = Fighter()
        self.ball = Ball(self.fighter)
        self.alien = Alien()
        self.screen = pygame.display.set_mode((defaultValues.SCREEN_WIDTH, defaultValues.SCREEN_HEIGHT))
        self.game_score = 0
        self.game_font = pygame.font.Font(None, 30)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.fighter.set_right_move()
                if event.key == pygame.K_LEFT:
                    self.fighter.set_left_move()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == pygame.BUTTON_LEFT:
                    self.ball.start_move()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    self.fighter.stop_moving()

    def game_lost(self):
        game_over_text = self.game_font.render("Game Over", True, 'white')
        game_over_rectangle = game_over_text.get_rect()
        game_over_rectangle.center = (defaultValues.SCREEN_WIDTH / 2, defaultValues.SCREEN_HEIGHT / 2)
        self.screen.blit(game_over_text, game_over_rectangle)

        pygame.display.update()
        pygame.time.wait(5000)

    def update_score(self):
        game_over_text = self.game_font.render(f"Your score is: {self.game_score}", True, 'white')
        self.screen.blit(game_over_text, (20, 20))

    def run(self):
        while self.game_is_running:
            self.check_events()

            self.screen.fill(defaultValues.SCREEN_COLOR)

            self.update_positions()

            self.draw_on_screen()
            self.update_score()
            self.update_states()

            pygame.display.update()

        self.game_lost()

    def update_positions(self):
        self.fighter.update_position()

        if self.ball.is_move:
            self.ball.update_position()

        self.alien.update_position()

    def update_states(self):
        if self.alien.is_get_hit(self.ball):
            self.game_score += 1

        if self.alien.y > self.fighter.y - self.alien.height:
            self.game_is_running = False

    def draw_on_screen(self):
        self.screen.blit(self.fighter.image, self.fighter.get_position())
        self.screen.blit(self.alien.image, self.alien.get_position())

        if self.ball.is_move:
            self.screen.blit(self.ball.image, self.ball.get_position())
