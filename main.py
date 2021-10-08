import pygame
import random

from config import *
from Stone import *
from Hero import *
from Dragon import *
from res_sprit import *

random.seed(version = 2)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
all_sprites = pygame.sprite.Group()
clock = pygame.time.Clock()

background = get_img('b.png')
background_rect = background.get_rect()

hero = Hero()
dragon = Dragon()
all_sprites.add(hero)
all_sprites.add(dragon)

while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill(BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)

    pygame.display.flip()


pygame.quit()