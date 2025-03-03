from random import randint
import pygame
import defaultValues

class Alien:
    def __init__(self):
        self.image = pygame.image.load('images/alien.png')
        self.width, self.height = self.image.get_size()
        self.step = 0.1
        self.increase_step = 0.01
        self.x = 0
        self.y = 0
        self.restart_position()

    def restart_position(self):
        self.x = randint(0, defaultValues.SCREEN_WIDTH - self.width)
        self.y = 0

    def update_speed(self):
        self.step += self.increase_step
        print("Alien: speed ", self.step)

    def update_position(self):
        self.y += self.step

    def is_get_hit(self, ball):
        if (ball.is_move and self.x - ball.width / 2 <= ball.x <= self.x + self.width + ball.width / 2
                and self.y - ball.height / 2 <= ball.y <= self.y + self.height + ball.height / 2):
            ball.set_collapsed()
            self.update_speed()
            self.restart_position()
            return True

        return False


    def get_position(self):
        return (self.x, self.y)