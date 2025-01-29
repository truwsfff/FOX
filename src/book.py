import pygame

from window import Window


class Book(Window):
    def __init__(self, screen, manager):
        super().__init__(screen, manager)
        pygame.display.set_caption('Книга')

        self.words = ['FOX', 'FOXY', 'FOXTROT']
        self.rects = {
            'exit': pygame.Rect(30, 30, 107, 107),
            'bg': pygame.Rect(0, 0, 1920, 1080)
        }

        self.image_1 = pygame.image.load('../data/x_exit.png')
        pygame.transform.scale(self.image_1, (
            self.rects.get('exit').width, self.rects.get('exit').height))

        self.image_2 = pygame.image.load('../data/bg.png')
        pygame.transform.scale(self.image_2, (
            self.rects.get('bg').width, self.rects.get('bg').height))

        self.font = pygame.font.Font('../data/HomeVideo-Regular.otf', 120)
        self.font_1 = pygame.font.Font('../data/HomeVideo-Regular.otf', 60)

        self.title = self.font.render('Книга', True,
                                      pygame.Color(255, 255, 255))

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rects.get('exit').collidepoint(event.pos):
                self.window_man.set_window('menu')
                self.window_man.run()

    def draw(self):
        self.screen.blit(self.image_2, self.rects.get('bg').topleft)
        self.screen.blit(self.image_1, self.rects.get('exit').topleft)
        self.screen.blit(self.title, (self.screen.get_width() // 2 - 172, 50))

        y_coord = 200
        for i in self.words:
            self.screen.blit(self.font.render(i, True, pygame.Color('white')),
                             (100, y_coord))
            y_coord += 130
