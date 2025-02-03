import pygame
import sqlite3

from game1 import PlayGame1
from window import Window
from settings import Settings
from description import Description
from game import PlayGame
from book import BookScreen
from start_window import StartWin
from menu import Menu


class LoginError(Exception):
    pass


class PasswordError(Exception):
    pass


class Registration(Window):
    def __init__(self, screen, manager):
        super().__init__(screen, manager)
        pygame.display.set_caption('Регистрация')
        self.con = sqlite3.connect('../FoxDB.db')
        self.cur = self.con.cursor()

        self.flag_input_login = False
        self.flag_input_passw = False
        self.status_in_or_up = False  # False - вход, True - регистрация
        self.status_passw = True

        self.validator = '\
        abcdefghijklmnopqrstuvwxyz0123456789'
        self.password = ''
        self.login = ''

        self.login_x1, self.login_x2 = 500, 500
        self.passw_x1, self.passw_x2 = 500, 500

        self.rects = {'surf': pygame.Rect(0, 0, 1920, 1080),
                      'fox': pygame.Rect(240, 140, 256, 285),
                      'text_surf_login': pygame.Rect(480, 420, 312, 67),
                      'text_surf_passw': pygame.Rect(480, 620, 312, 67),
                      'text_input_login': pygame.Rect(480, 520, 993, 66),
                      'text_input_passw': pygame.Rect(480, 720, 993, 66),
                      'button_next': pygame.Rect(715, 805, 500, 150),
                      'type_sign_in': pygame.Rect(1030, 135, 312, 67),
                      'type_sign_up': pygame.Rect(1380, 135, 312, 67),
                      'show_passw': pygame.Rect(830, 620, 312, 67)
                      }

        self.image_1 = pygame.image.load('../data/images/window_login.png')
        pygame.transform.scale(self.image_1, (
            self.rects.get('surf').width, self.rects.get('surf').height))

        self.image_2 = pygame.image.load('../data/images/fox.png')
        pygame.transform.scale(self.image_1, (
            self.rects.get('surf').width, self.rects.get('surf').height))

        self.image_3 = pygame.image.load('../data/images/surf_for_text.png')
        pygame.transform.scale(self.image_3, (
            self.rects.get('text_surf_login').width,
            self.rects.get('text_surf_login').height))

        self.image_4 = pygame.image.load('../data/images/surf_for_text.png')
        pygame.transform.scale(self.image_4, (
            self.rects.get('text_surf_passw').width,
            self.rects.get('text_surf_passw').height))

        self.image_5 = pygame.image.load('../data/images/input.png')
        pygame.transform.scale(self.image_5, (
            self.rects.get('text_input_login').width,
            self.rects.get('text_input_login').height))

        self.image_6 = pygame.image.load('../data/images/input.png')
        pygame.transform.scale(self.image_6, (
            self.rects.get('text_input_passw').width,
            self.rects.get('text_input_passw').height))

        self.image_7 = pygame.image.load('../data/images/button.png')
        pygame.transform.scale(self.image_7, (
            self.rects.get('button_next').width,
            self.rects.get('button_next').height))

        self.image_8 = pygame.image.load('../data/images/surf_for_text.png')
        pygame.transform.scale(self.image_8, (
            self.rects.get('type_sign_in').width,
            self.rects.get('type_sign_in').height))

        self.image_9 = pygame.image.load('../data/images/surf_for_text.png')
        pygame.transform.scale(self.image_9, (
            self.rects.get('type_sign_up').width,
            self.rects.get('type_sign_up').height))

        self.image_10 = pygame.image.load('../data/images/surf_for_text.png')
        pygame.transform.scale(self.image_10, (
            self.rects.get('show_passw').width,
            self.rects.get('show_passw').height))

        self.font = pygame.font.Font('../data/font/HomeVideo-Regular.otf', 36)
        self.font_button = pygame.font.Font(
            '../data/font/HomeVideo-Regular.otf',
            70)

        self.text_surface_login = self.font.render('Логин', True,
                                                   pygame.Color('white'))
        self.text_surface_passw = self.font.render('Пароль', True,
                                                   pygame.Color('white'))
        self.text_surface_next = self.font_button.render('Вход', True,
                                                         pygame.Color('white'))
        self.text_type_in = self.font.render('Вход', True,
                                             pygame.Color('white'))
        self.text_type_up = self.font.render('Регистрация',
                                             True,
                                             pygame.Color('white'))
        self.text_login = self.font.render('', True,
                                           pygame.Color('white'))
        self.text_passw = self.font.render('', True,
                                           pygame.Color('white'))
        self.text_show_passw = self.font.render('Показать', True,
                                                pygame.Color('white'))
        self.text_error = self.font.render('', True,
                                           pygame.Color('red'))

        self.text_position_login = (575, 435)
        self.text_position_passw = (570, 635)
        self.text_position_next = (885, 850)
        self.text_type_in_position = (1145, 150)
        self.text_type_up_position = (1417, 150)
        self.text_login_inp = (506, 534)
        self.text_passw_inp = (500, 729)
        self.text_show = (895, 635)
        self.text_error_pos = (0, 0)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rects.get('button_next').collidepoint(event.pos):
                try:
                    if self.login == '' or not self.validator_check(
                            self.login):
                        raise LoginError
                    if self.password == '' or len(self.password) < 5:
                        raise PasswordError
                except LoginError:
                    self.text_error = self.font.render('\
В логине русские буквы/не в диапазоне 4 <= x <= 15',
                                                       True,
                                                       pygame.Color('red'))
                    return
                except PasswordError:
                    self.text_error = self.font.render('\
Пароль содержит менее 5 символов',
                                                       True,
                                                       pygame.Color('red'))
                    return

                if self.status_in_or_up:
                    try:
                        self.cur.execute(
                            '''\
INSERT INTO users(login, password, easy, hard) VALUES(?, ?, ?, ?)''',
                            (self.login.upper(), self.password.upper(), 0, 0))
                    except sqlite3.IntegrityError:
                        self.text_error = self.font.render('\
Данный логин уже существует', True, pygame.Color('red'))
                        return
                else:
                    info = self.cur.execute('''\
SELECT login, password FROM users 
WHERE login = ?''', (self.login.upper(),)).fetchone()
                    if info is None:
                        self.text_error = self.font.render('\
Аккаунт не найден', True, pygame.Color('red'))
                        return
                    if info[1] != self.password.upper():
                        self.text_error = self.font.render('\
Неверный пароль', True, pygame.Color('red'))
                        return
                self.window_man.add_window('menu',
                                           Menu(self.screen, self.window_man))
                self.window_man.add_window('settings', Settings(self.screen,
                                                                self.window_man))
                self.window_man.add_window('book', BookScreen(self.screen,
                                                              self.window_man))
                self.window_man.add_window('description',
                                           Description(self.screen,
                                                       self.window_man))
                self.window_man.add_window('game', PlayGame(self.screen,
                                                            self.window_man,
                                                            self.login.upper()))
                self.window_man.add_window('startwin', StartWin(self.screen,
                                                                self.window_man,
                                                                self.login.upper()))
                self.window_man.add_window('game1', PlayGame1(self.screen,
                                                              self.window_man,
                                                              self.login.upper()))
                self.window_man.set_window('menu')
                self.con.commit()
                self.window_man.run()

            if self.rects.get('text_input_login').collidepoint(event.pos):
                print('кнопка ввода логина')
                if self.flag_input_passw:
                    self.flag_input_passw = False
                self.flag_input_login = True
            else:
                self.flag_input_login = False

            if self.rects.get('text_input_passw').collidepoint(event.pos):
                print('кнопка ввода пароля')
                if self.flag_input_login:
                    self.flag_input_login = False
                self.flag_input_passw = True
            else:
                self.flag_input_passw = False

            if self.rects.get('type_sign_in').collidepoint(event.pos):
                print('режим входа')
                self.text_surface_next = self.font_button.render('Вход', True,
                                                                 pygame.Color(
                                                                     'white'))
                self.text_position_next = (885, 850)
                self.status_in_or_up = False

            if self.rects.get('type_sign_up').collidepoint(event.pos):
                print('режим регистрации')
                self.text_surface_next = self.font_button.render('Регистрация',
                                                                 True,
                                                                 pygame.Color(
                                                                     'white'))
                self.text_position_next = (735, 850)
                self.status_in_or_up = True

            if self.rects.get('show_passw').collidepoint(event.pos):
                if self.status_passw:
                    self.status_passw = False
                else:
                    self.status_passw = True

        if event.type == pygame.KEYDOWN:
            if self.flag_input_login:
                if pygame.key.name(event.key) == 'backspace':
                    self.login = self.login[:-1]
                else:
                    if len(self.login) < 40:
                        self.login += event.unicode
                self.text_login = self.font.render(self.login, True,
                                                   pygame.Color('white'))

            if self.flag_input_passw:
                if pygame.key.name(event.key) == 'backspace':
                    self.password = self.password[:-1]
                else:
                    if len(self.password) < 40:
                        self.password += event.unicode

            if event.key == pygame.K_ESCAPE:
                self.show_exit_dialog(self.screen)

    def draw(self):
        self.screen.blit(self.image_1, self.rects.get('surf').topleft)
        self.screen.blit(self.image_2, self.rects.get('fox').topleft)
        self.screen.blit(self.image_3,
                         self.rects.get('text_surf_login').topleft)
        self.screen.blit(self.image_4,
                         self.rects.get('text_surf_passw').topleft)
        self.screen.blit(self.image_5,
                         self.rects.get('text_input_login').topleft)
        self.screen.blit(self.image_6,
                         self.rects.get('text_input_passw').topleft)
        self.screen.blit(self.image_7,
                         self.rects.get('button_next').topleft)
        self.screen.blit(self.image_8,
                         self.rects.get('type_sign_in').topleft)
        self.screen.blit(self.image_9,
                         self.rects.get('type_sign_up').topleft)
        self.screen.blit(self.image_10,
                         self.rects.get('show_passw').topleft)

        self.screen.blit(self.text_surface_login, self.text_position_login)
        self.screen.blit(self.text_surface_passw, self.text_position_passw)
        self.screen.blit(self.text_surface_next, self.text_position_next)
        self.screen.blit(self.text_type_in, self.text_type_in_position)
        self.screen.blit(self.text_type_up, self.text_type_up_position)
        self.screen.blit(self.text_login, self.text_login_inp)
        self.screen.blit(self.text_passw, self.text_passw_inp)
        self.screen.blit(self.text_show_passw, self.text_show)
        self.screen.blit(self.text_error, self.text_error_pos)

        if self.flag_input_login:
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (self.login_x1, 529),
                             (self.login_x2, 575), 5)
        if self.flag_input_passw:
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (self.passw_x1, 729),
                             (self.passw_x2, 775), 5)

        if self.status_passw:
            self.text_show_passw = self.font.render('Показать', True,
                                                    pygame.Color('white'))
            self.text_show = (895, 635)
            self.text_passw = self.font.render('*' * len(self.password),
                                               True,
                                               pygame.Color('white'))
        if not self.status_passw:
            self.text_show_passw = self.font.render('Скрыть', True,
                                                    pygame.Color('white'))
            self.text_show = (920, 635)
            self.text_passw = self.font.render(self.password, True,
                                               pygame.Color('white'))

    def validator_check(self, login):
        if len(login) < 4 or len(login) > 15:
            return False
        for i in login:
            if i.lower() not in self.validator:
                return False
        return True
