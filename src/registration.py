import pygame
from src.window import Window


class Registration(Window):
    def __init__(self, screen):
        super().__init__(screen)
        pygame.display.set_caption('Регистрация')
        self.surf = pygame.Rect(0, 0, 1920, 1080)

        self.image = pygame.image.load('../data/window_login.png')

    def draw(self):
        self.screen.blit(self.image)
