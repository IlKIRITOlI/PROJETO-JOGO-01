from pygame import Surface, Rect
from pygame.font import Font

from code.MENU import MENU

import pygame

from code.const import WIN_WIDTH, WIN_HEIGHT


class GAME:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            menu = MENU(self.window)
            menu.run()
    pass