import pygame
import sqlite3

from window import Window


class StartWin(Window):
    def __init__(self, screen, manager, login):
        super().__init__(screen, manager)
        pygame.display.set_caption('Стартовое окно')
        self.con = sqlite3.connect('../FoxDB.db')
        self.cur = self.con.cursor()
        self.login = login
        self.easy = None
        self.hard = None

        self.rects = {
            'exit': pygame.Rect(30, 30, 107, 107),
            'bg': pygame.Rect(0, 0, 1920, 1080),
            'easy': pygame.Rect(192, 357, 500, 150),
            'hard': pygame.Rect(1227, 357, 500, 150)
        }

        self.image_1 = pygame.image.load('../data/images/startwin.png')
        pygame.transform.scale(self.image_1, (
            self.rects.get('bg').width, self.rects.get('bg').height))

        self.image_2 = pygame.image.load('../data/images/x_exit.png')
        pygame.transform.scale(self.image_2, (
            self.rects.get('exit').width, self.rects.get('exit').height))

        self.font = pygame.font.Font('../data/font/HomeVideo-Regular.otf', 47)

        self.text_easy = self.font.render(f'Лучший результат {self.easy}',
                                          True,
                                          pygame.Color(
                                              'white'))

        self.text_hard = self.font.render(f'Лучший результат {self.hard}',
                                          True,
                                          pygame.Color(
                                              'white'))

    def res(self):
        self.data = self.cur.execute('''SELECT easy, hard FROM USERS
                    WHERE login = ?''', (self.login,)).fetchone()
        self.easy = self.data[0]
        self.hard = self.data[1]

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rects.get('exit').collidepoint(event.pos):
                self.window_man.set_window('menu')
                self.window_man.run()
            if self.rects.get('easy').collidepoint(event.pos):
                self.window_man.set_window('game')
                self.window_man.run()
            if self.rects.get('hard').collidepoint(event.pos):
                self.window_man.set_window('game1')
                self.window_man.run()

    def draw(self):
        self.res()
        self.text_easy = self.font.render(f'Лучший результат {self.easy}',
                                          True,
                                          pygame.Color(
                                              'white'))

        self.text_hard = self.font.render(f'Лучший результат {self.hard}',
                                          True,
                                          pygame.Color(
                                              'white'))
        self.screen.blit(self.image_1, self.rects.get('bg').topleft)
        self.screen.blit(self.image_2, self.rects.get('exit').topleft)
        self.screen.blit(self.text_easy, (200, 300))
        self.screen.blit(self.text_hard, (1240, 300))
