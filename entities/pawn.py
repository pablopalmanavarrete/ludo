import pygame

from utils import load_image


class Pawn(pygame.sprite.Sprite):
    def __init__(self, id, color, axis_x, axis_y):
        pygame.sprite.Sprite.__init__(self)
        self.id = id
        self.position = -1
        self.free = False
        self.winner = False
        self.render = True
        self.moving = False
        self.color = color
        self.linked_pawns = []
        self.initial_axis_x = axis_x
        self.initial_axis_y = axis_y
        self.axis_x = axis_x
        self.axis_y = axis_y

        self.load_image(color)

        self.click = False

    def set_axis(self, axis_x, axis_y):
        self.rect.centerx = axis_x
        self.rect.centery = axis_y

    def liberar(self):
        self.free = True

    def jailing(self):
        self.free = False
        self.render = True
        self.update_position(-1)
        self.set_axis(self.initial_axis_x, self.initial_axis_y)

    def update_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def get_level(self):
        return len(self.linked_pawns) + 1

    def get_render(self):
        return self.render

    def set_click(self, click):
        self.click = click

    def load_image(self, color):
        self.image = load_image("resources/pawn/" + color + "/" + str(len(self.linked_pawns) + 1) + ".png", True)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.axis_x
        self.rect.centery = self.axis_y

    def join_pawn(self, pawn):
        self.linked_pawns.append(pawn)
        self.load_image(self.color)

    def separate_pawn(self):
        for linked_pawn in self.linked_pawns:
            linked_pawn.jailing()

        self.linked_pawns = []
        self.load_image(self.color)

    def set_invisible(self):
        self.render = False

    def start_moving(self):
        self.moving = True
