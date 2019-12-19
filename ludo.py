from tkinter import *

from entities.board import Board
from entities.button import Button
from entities.dice import Dice
from entities.pawn import Pawn
from utils import *


def habilitar_peones_no_libres(player):
    success = False
    for pawn in player.pawns:
        if not pawn.free and not pawn.winner:
            pawn.set_click(True)
            success = True

    if success:
        return font.render('Elija su peon a liberar', True, LETRA_VERDE, FONDO_VERDE), draw_pawn_turn()
    else:
        return font.render('No hay peones para liberar', True, LETRA_ROJO, FONDO_ROJO), draw_pawn_turn()


def habilitar_peones_libres(player):
    success = False
    for pawn in player.pawns:
        if pawn.free and not pawn.winner:
            pawn.set_click(True)
            success = True

    if success:
        return font.render('Elija su peon a mover', True, LETRA_VERDE, FONDO_VERDE), draw_pawn_turn()
    else:
        return font.render('No hay peones para mover', True, LETRA_ROJO, FONDO_ROJO), change_turn()


def liberar_peon(pawn, entry_cell):
    if not pawn.free:
        pawn = verify_overlapping(entry_cell, pawn)

        pawn.liberar()
        pawn.update_position(entry_cell)
        pawn.set_axis(board.cells[pawn.get_position()].axis_x, board.cells[pawn.get_position()].axis_y)
        return font.render('Peon ' + pawn.color + ' Liberado', True, LETRA_VERDE, FONDO_VERDE), draw_pawn_turn()

    return font.render('No se puede liberar peon', True, LETRA_ROJO, FONDO_ROJO), draw_pawn_turn()


def mover_peon(pawn, dice_value):
    if pawn.free:
        if board.get_last_cell() >= pawn.get_position() + dice_value:
            new_position = pawn.get_position() + dice_value
        else:
            new_position = (pawn.get_position() + dice_value) - (board.get_last_cell() + 1)

        pawn = verify_overlapping(new_position, pawn)

        pawn.update_position(new_position)
        pawn.set_axis(board.cells[pawn.get_position()].axis_x, board.cells[pawn.get_position()].axis_y)

        if repeat_turn:
            return font.render('Juega Otra Vez!', True, LETRA_VERDE, FONDO_VERDE), draw_pawn_turn()
        else:
            return font.render('Turno Terminado', True, LETRA_VERDE, FONDO_VERDE), change_turn()

    return font.render('No Hay mas peones para mover', True, LETRA_ROJO, FONDO_ROJO), change_turn()


def verify_overlapping(new_position, pawn):
    for player in board.players:
        for other_pawn in player.pawns:
            if new_position == other_pawn.get_position():
                if pawn.color != other_pawn.color:
                    if other_pawn.get_level() > 1:
                        other_pawn.separate_pawn()

                    other_pawn.jailing()
                else:
                    if pawn.id == other_pawn.id:
                        continue

                    pawn.set_invisible()
                    other_pawn.join_pawn(pawn)
                    return other_pawn

    return pawn


def change_turn():
    board.change_turn(board.get_player_of_turn().get_turn_position())
    return draw_pawn_turn()


def draw_pawn_turn():
    return Pawn(10, board.get_player_of_turn().color, 925, 50)


def main():
    clock = pygame.time.Clock()
    pygame.display.set_caption("Ludo By Babas")
    dice_roll_start = pygame.time.get_ticks()

    text = font.render('Comienza a jugar!', True, (6, 136, 61), (82, 190, 128))

    # GAME
    while True:
        screen.fill((255, 255, 255))
        dice_roll_start, text, turn_pawn = events(dice_roll_start, text, draw_pawn_turn())

        dice_time = pygame.time.get_ticks() - dice_roll_start
        if dice_time < 500 and dice.rolling:
            dice.roll()
            pygame.time.delay(50)
        elif dice_time >= 500 and dice.rolling:
            dice.end_roll()
            if not dice.rolling and dice.value == 6:
                repeat_turn = True
                btn_move.enable_button()
                btn_free.enable_button()
            elif not dice.rolling and dice.value > 0:
                repeat_turn = False
                btn_move.enable_button()

        display_images(text, turn_pawn)
        clock.tick(30)
    return 0


def display_images(text, turn_pawn):
    screen.blit(background_image, (0, 0))
    screen.blit(dice.image, dice.rect)

    text_turn = font.render('Turno de', True, LETRA_VERDE, FONDO_BLANCO)

    turnRect = text_turn.get_rect()
    turnRect.centerx = 855
    turnRect.centery = 50

    screen.blit(text_turn, turnRect)
    screen.blit(turn_pawn.image, turn_pawn.rect)

    screen.blit(btn_free.image, btn_free.rect)
    screen.blit(btn_move.image, btn_move.rect)

    textRect = text.get_rect()
    textRect.centerx = 875
    textRect.centery = 12
    screen.blit(text, textRect)

    for player in board.players:
        for pawn in player.pawns:
            if pawn.get_render():
                screen.blit(pawn.image, pawn.rect)
    pygame.display.flip()


def events(dice_roll_start, text, turn_pawn):
    for eventos in pygame.event.get():
        if eventos.type == QUIT:
            sys.exit(0)
        if eventos.type == MOUSEBUTTONDOWN:
            mouse = eventos.pos
            if dice.rect.colliderect([mouse[0], mouse[1], 1, 1]):
                dice_roll_start = pygame.time.get_ticks()
                dice.start_roll()
            elif btn_free.rect.colliderect([mouse[0], mouse[1], 1, 1]) and btn_free.enable:
                text, turn_pawn = habilitar_peones_no_libres(board.get_player_of_turn())
            elif btn_move.rect.colliderect([mouse[0], mouse[1], 1, 1]) and btn_move.enable:
                text, turn_pawn = habilitar_peones_libres(board.get_player_of_turn())
            else:
                for player in board.players:
                    for pawn in player.pawns:
                        if pawn.rect.colliderect([mouse[0], mouse[1], 1, 1]) and pawn.click and not pawn.winner:
                            if pawn.free:
                                text, turn_pawn = mover_peon(pawn, dice.value)
                            else:
                                text, turn_pawn = liberar_peon(pawn, player.entry_board_cell)

        if eventos.type == MOUSEBUTTONUP:
            mouse = eventos.pos
            if dice.rect.colliderect([mouse[0], mouse[1], 1, 1]):
                btn_move.disable_button()
                btn_free.disable_button()
            elif btn_free.rect.colliderect([mouse[0], mouse[1], 1, 1]) and btn_free.enable:
                btn_free.disable_button()
                btn_move.disable_button()
            elif btn_move.rect.colliderect([mouse[0], mouse[1], 1, 1]) and btn_move.enable:
                btn_free.disable_button()
                btn_move.disable_button()
            else:
                for player in board.players:
                    for pawn in player.pawns:
                        pawn.set_click(False)

    return dice_roll_start, text, turn_pawn


screen = pygame.display.set_mode((WIDTH + 200, HEIGHT))
repeat_turn = False
board = Board()
font = None
text = ""
textRect = None
FONDO_ROJO = (236, 112, 99)
LETRA_ROJO = (160, 32, 19)
LETRA_VERDE = (6, 136, 61)
FONDO_VERDE = (82, 190, 128)
FONDO_BLANCO = (255, 255, 255)

if __name__ == '__main__':
    pygame.init()
    background_image = load_image('./resources/board.png')
    font = pygame.font.Font('resources/calibri.ttf', 26)
    dice = Dice()
    btn_free = Button("liberar", 875, 220)
    btn_move = Button("mover", 875, 320)
    main()
