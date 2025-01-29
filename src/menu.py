import pygame
from window import Window


class Menu(Window):
    def __init__(self, screen, manager):
        super().__init__(screen, manager)
        pygame.display.set_caption('Меню')

        self.rects = {
            'book': pygame.Rect(1510, 248, 400, 113),
            'settings': pygame.Rect(1510, 400, 400, 113),
            'description': pygame.Rect(1510, 557, 400, 113),
            'play_but': pygame.Rect(598, 816, 750, 235),
            'fox': pygame.Rect(50, 50, 281, 283),
            'text': pygame.Rect(480, 216, 100, 500),
            'bg': pygame.Rect(0, 0, 1920, 1080)
        }

        self.bg_image = pygame.image.load('../data/bg.png')
        pygame.transform.scale(self.bg_image, (
            self.rects.get('bg').width, self.rects.get('bg').height))

        self.fox_image = pygame.image.load('../data/fox.png')
        pygame.transform.scale(self.fox_image, (
            self.rects.get('fox').width, self.rects.get('fox').height))

        self.bg_text = pygame.image.load('../data/bg_fox_text.png')
        pygame.transform.scale(self.bg_text, (
            self.rects.get('text').width, self.rects.get('text').height))

        self.settings_button_img = pygame.image.load('../data/btn_text.png')
        pygame.transform.scale(self.settings_button_img, (
            self.rects.get('settings').width,
            self.rects.get('settings').height))

        self.book_button_img = pygame.image.load('../data/btn_text.png')
        pygame.transform.scale(self.book_button_img, (
            self.rects.get('book').width, self.rects.get('book').height))

        self.description_button_img = pygame.image.load('../data/btn_text.png')
        pygame.transform.scale(self.description_button_img, (
            self.rects.get('description').width,
            self.rects.get('description').height))

        self.play_button_img = pygame.image.load('../data/btn_play.png')
        pygame.transform.scale(self.play_button_img, (
            self.rects.get('play_but').width,
            self.rects.get('play_but').height))

        self.font = pygame.font.Font('../data/HomeVideo-Regular.otf', 47)
        self.font_1 = pygame.font.Font('../data/HomeVideo-Regular.otf', 384)
        self.font_2 = pygame.font.Font('../data/HomeVideo-Regular.otf', 128)
        self.font_3 = pygame.font.Font('../data/HomeVideo-Regular.otf', 64)

        self.text_book = self.font_3.render('Книга', True,
                                            pygame.Color('white'))

        self.text_settings = self.font_3.render('Настройки', True,
                                                pygame.Color('white'))

        self.text_description = self.font.render('Описание игры', True,
                                                 pygame.Color('white'))

        self.text_fox = self.font_1.render('FOX', True,
                                           pygame.Color('white'))

        self.text_play = self.font_2.render('Играть', True,
                                            pygame.Color('white'))

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rects.get('book').collidepoint(event.pos):
                self.window_man.set_window('book')
                self.window_man.run()
            if self.rects.get('settings').collidepoint(event.pos):
                self.window_man.set_window('settings')
                self.window_man.run()
            if self.rects.get('description').collidepoint(event.pos):
                self.window_man.set_window('description')
                self.window_man.run()

    def draw(self):
        self.screen.blit(self.bg_image, (0, 0))
        self.screen.blit(self.fox_image, self.rects.get('fox').topleft)
        self.screen.blit(self.bg_text, self.rects.get('text').topleft)
        self.screen.blit(self.play_button_img,
                         self.rects.get('play_but').topleft)
        self.screen.blit(self.book_button_img,
                         self.rects.get('book').topleft)
        self.screen.blit(self.settings_button_img,
                         self.rects.get('settings').topleft)
        self.screen.blit(self.description_button_img,
                         self.rects.get('description').topleft)

        self.screen.blit(self.text_fox, (630, 290))
        self.screen.blit(self.text_play, (744, 870))
        self.screen.blit(self.text_book, (1612, 275))
        self.screen.blit(self.text_settings, (1540, 425))
        self.screen.blit(self.text_description, (1527, 590))
