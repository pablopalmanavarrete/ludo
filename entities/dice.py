import random
import pygame

from utils import load_image


class Dice(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.value = 1
        self.rolling = False
        self.change_image()

    def start_roll(self):
        self.rolling = True

    def roll(self):
        if self.value > 6:
            self.value = 1
        self.change_image()
        self.value += 1

    def end_roll(self):
        self.rolling = False
        self.value = random.randint(1, 6)
        self.change_image()

    def change_image(self):
        self.image = load_image("resources/dado-" + str(self.value) + ".png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = 875
        self.rect.centery = 120
