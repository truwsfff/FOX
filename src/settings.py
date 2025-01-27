import pygame

from window import Window


class Settings(Window):
    def __init__(self, screen, manager):
        super().__init__(screen, manager)
        pygame.display.set_caption('Настройки')

        self.rects = {
            'line': pygame.Rect(500, 500, 450, 15),
            'circle': pygame.Rect(500, 491, 30, 30)
        }

        self.moving = False
        self.x = self.rects.get('circle').topleft[0]
        self.x_n = 0

        self.image_1 = pygame.image.load('../data/line_pg1.png')
        pygame.transform.scale(self.image_1, (
            self.rects.get('line').width, self.rects.get('line').height))

        self.image_2 = pygame.image.load('../data/circle_pg.png')
        pygame.transform.scale(self.image_2, (
            self.rects.get('circle').width, self.rects.get('circle').height))

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rects.get('circle').collidepoint(event.pos):
                self.moving = True
        if event.type == pygame.MOUSEMOTION:
            if self.moving:
                self.x_n = event.rel[0]
                if 485 <= self.x + self.x_n <= 935:
                    self.x = self.x + self.x_n
                    self.rects['circle'] = pygame.Rect(self.x, 491, 30, 30)
        if event.type == pygame.MOUSEBUTTONUP:
            self.moving = False

    def draw(self):
        self.screen.blit(self.image_1, self.rects.get('line').topleft)
        self.screen.blit(self.image_2, self.rects.get('circle').topleft)
