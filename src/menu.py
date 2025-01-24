import pygame
from src.window import Window


class Menu(Window):
    def __init__(self, screen, manager):
        super().__init__(screen, manager)
        pygame.display.set_caption('Меню')
