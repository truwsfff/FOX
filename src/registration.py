import pygame

from src.window import Window


class Registration(Window):
    def __init__(self, screen):
        super().__init__(screen)
        pygame.display.set_caption('Регистрация')
        self.rects = {'surf': pygame.Rect(0, 0, 1920, 1080),
                      'fox': pygame.Rect(225, 140, 256, 285)
                      }

        self.image_1 = pygame.image.load('../data/window_login.png')
        pygame.transform.scale(self.image_1, (
            self.rects.get('surf').width, self.rects.get('surf').height))
        self.image_2 = pygame.image.load('../data/fox.png')
        pygame.transform.scale(self.image_1, (
            self.rects.get('surf').width, self.rects.get('surf').height))

    def draw(self):
        self.screen.blit(self.image_1, self.rects.get('surf').topleft)
        self.screen.blit(self.image_2, self.rects.get('fox').topleft)
