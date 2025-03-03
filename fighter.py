import pygame
import defaultValues

class Fighter:
    def __init__(self):
        self.image = pygame.image.load('images/fighter.png')
        self.width, self.height = self.image.get_size()
        self.step = 0.3
        self.x = defaultValues.SCREEN_WIDTH / 2 - self.width / 2
        self.y = defaultValues.SCREEN_HEIGHT - self.height
        self.is_right_move = False
        self.is_left_move = False

    def set_right_move(self):
        self.is_right_move = True

    def set_left_move(self):
        self.is_left_move = True

    def stop_moving(self):
        self.is_right_move = False
        self.is_left_move = False

    def update_position(self):
        if self.is_right_move and self.x <= defaultValues.SCREEN_WIDTH - self.width - self.step:
            self.x += self.step

        if self.is_left_move and self.x >= self.step:
            self.x -= self.step

    def get_position(self):
        return (self.x, self.y)