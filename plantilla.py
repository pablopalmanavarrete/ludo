# Módulos
import sys, pygame
from utils import *

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ludo")

    background_image = load_image('resources/board.png')

    while True:
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)

        screen.blit(background_image, (0, 0))
        pygame.display.flip()
    return 0


if __name__ == '__main__':
    pygame.init()
    main()