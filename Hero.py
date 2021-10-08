import pygame
import random
import time

from config import *
from res_sprit import *


class Hero(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = get_img('hero.png')
        self.rect = self.image.get_rect()
        self.rect.center = (self.random_pos(WIDTH), self.random_pos(HEIGHT))

    @staticmethod
    def random_pos(n):
        pos=0
        while pos % 2 == 0:
            pos=random.randint(1, n / 30)
        return pos * 30

    def update(self):

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= STEP
            D_MOVE = False
        if pressed[pygame.K_s] and self.rect.y < HEIGHT - STEP:
            self.rect.y += STEP
            D_MOVE = False
        if pressed[pygame.K_d] and self.rect.x < WIDTH - STEP:
            self.rect.x += STEP
            D_MOVE = False
        if pressed[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= STEP
            D_MOVE = False


