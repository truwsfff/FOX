import pygame

from src.window import Window


class Registration(Window):
    def __init__(self, screen):
        super().__init__(screen)
        pygame.display.set_caption('Регистрация')
