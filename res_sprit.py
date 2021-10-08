import os
import pygame


def get_img(name_img):
    game_folder = os.path.dirname(__file__)
    img_folder = os.path.join(game_folder, 'res')
    return pygame.image.load(os.path.join(img_folder, name_img)).convert()
