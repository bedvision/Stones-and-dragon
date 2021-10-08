import pygame
import random

from config import *
from res_sprit import *


class Dragon(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = get_img('dragon.png')
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (self.random_pos(WIDTH), self.random_pos(HEIGHT))

    @staticmethod
    def random_pos(n):
        pos = 0
        while pos % 2 == 0:
            pos = random.randint(1, n / 30)
        return pos * 30

    def update(self):

        res = random.randint(0, 3)

        if not D_MOVE:
            if res == 0 and self.rect.y > 0:
                self.rect.y -= STEP
                pygame.time.wait(WAIT)

            if res == 1 and self.rect.y < HEIGHT - STEP:
                self.rect.y += STEP
                pygame.time.wait(WAIT)

            if res == 2 and self.rect.x < WIDTH - STEP:
                self.rect.x += STEP
                pygame.time.wait(WAIT)

            if res == 3 and self.rect.x > 0:
                self.rect.x -= STEP
                pygame.time.wait(WAIT)

            D_MOVE = True
