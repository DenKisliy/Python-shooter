import pygame
import defaultValues


class Ball:
    def __init__(self, fighter):
        self.image = pygame.image.load('images/rocket.png')
        self.width, self.height = self.image.get_size()
        self.step = 0.3
        self.x = defaultValues.SCREEN_WIDTH / 2 - self.width / 2
        self.y = defaultValues.SCREEN_HEIGHT - self.height
        self.is_move = False
        self.fighter = fighter

    def set_collapsed(self):
        self.is_move = False

    def start_move(self):
        self.is_move = True
        self.y = defaultValues.SCREEN_HEIGHT - self.fighter.height - self.height / 2 - self.step
        self.x = self.fighter.x + self.fighter.width / 2 - self.width / 2

    def update_position(self):
        self.y -= self.step
        if self.y + self.height / 2 <= 0:
            self.set_collapsed()

    def get_position(self):
        return (self.x, self.y)