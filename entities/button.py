import pygame

from utils import load_image


class Button(pygame.sprite.Sprite):
    def __init__(self, name_button, axis_x, axis_y):
        pygame.sprite.Sprite.__init__(self)
        self.name_button = name_button
        self.image = ""
        self.rect = ""
        self.axis_x = axis_x
        self.axis_y = axis_y
        self.enable = False
        self.change_image(name_button, "disable")

    def enable_button(self):
        self.enable = True
        self.change_image(self.name_button, "enable")

    def disable_button(self):
        self.enable = False
        self.change_image(self.name_button, "disable")

    def change_image(self, name_button, state):
        self.image = load_image("resources/btn-" + name_button + "-" + state + ".png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.axis_x
        self.rect.centery = self.axis_y
