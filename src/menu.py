import pygame
from window import Window


class Menu(Window):
    def __init__(self, screen, manager):
        super().__init__(screen, manager)
        pygame.display.set_caption('Меню')

        self.rects = {
            'music_1': pygame.Rect(500, 500, 300, 35)
        }
