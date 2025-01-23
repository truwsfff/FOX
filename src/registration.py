import pygame

from src.window import Window


class Registration(Window):
    def __init__(self, screen):
        super().__init__(screen)
        pygame.display.set_caption('Регистрация')

        self.flag_input_login = False
        self.flag_input_passw = False
        self.status_in_or_up = False  # человек регистрируется или входит

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
                      }

        self.image_1 = pygame.image.load('../data/window_login.png')
        pygame.transform.scale(self.image_1, (
            self.rects.get('surf').width, self.rects.get('surf').height))

        self.image_2 = pygame.image.load('../data/fox.png')
        pygame.transform.scale(self.image_1, (
            self.rects.get('surf').width, self.rects.get('surf').height))

        self.image_3 = pygame.image.load('../data/surf_for_text.png')
        pygame.transform.scale(self.image_3, (
            self.rects.get('text_surf_login').width,
            self.rects.get('text_surf_login').height))

        self.image_4 = pygame.image.load('../data/surf_for_text.png')
        pygame.transform.scale(self.image_4, (
            self.rects.get('text_surf_passw').width,
            self.rects.get('text_surf_passw').height))

        self.image_5 = pygame.image.load('../data/input.png')
        pygame.transform.scale(self.image_5, (
            self.rects.get('text_input_login').width,
            self.rects.get('text_input_login').height))

        self.image_6 = pygame.image.load('../data/input.png')
        pygame.transform.scale(self.image_6, (
            self.rects.get('text_input_passw').width,
            self.rects.get('text_input_passw').height))

        self.image_7 = pygame.image.load('../data/button.png')
        pygame.transform.scale(self.image_7, (
            self.rects.get('button_next').width,
            self.rects.get('button_next').height))

        self.image_8 = pygame.image.load('../data/surf_for_text.png')
        pygame.transform.scale(self.image_8, (
            self.rects.get('type_sign_in').width,
            self.rects.get('type_sign_in').height))

        self.image_9 = pygame.image.load('../data/surf_for_text.png')
        pygame.transform.scale(self.image_9, (
            self.rects.get('type_sign_up').width,
            self.rects.get('type_sign_up').height))

        self.font = pygame.font.Font('../data/HomeVideo-Regular.otf', 36)
        self.font_button = pygame.font.Font('../data/HomeVideo-Regular.otf',
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

        self.text_position_login = (575, 435)
        self.text_position_passw = (570, 635)
        self.text_position_next = (885, 850)
        self.text_type_in_position = (1145, 150)
        self.text_type_up_position = (1417, 150)
        self.text_login_inp = (506, 534)
        self.text_passw_inp = (500, 729)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rects.get('button_next').collidepoint(event.pos):
                print('переход в меню')
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
            if self.rects.get('type_sign_up').collidepoint(event.pos):
                print('режим регистрации')
                self.text_surface_next = self.font_button.render('Регистрация',
                                                                 True,
                                                                 pygame.Color(
                                                                     'white'))
                self.text_position_next = (735, 850)
        if event.type == pygame.KEYDOWN:
            if pygame.key.name(event.key) in self.validator or pygame.key.name(
                    event.key) == 'backspace' or pygame.key.name(
                    event.key) == 'space':
                if self.flag_input_login:
                    print(pygame.key.name(event.key))
                    if pygame.key.name(event.key) == 'backspace':
                        if self.login != '':
                            self.login = self.login[0:-1]
                    elif pygame.key.name(event.key) == 'space':
                        self.login += ' '
                    else:
                        self.login += pygame.key.name(event.key)
                    self.text_login = self.font.render(self.login, True,
                                                       pygame.Color('white'))

                if self.flag_input_passw:
                    self.password += pygame.key.name(event.key)

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

        self.screen.blit(self.text_surface_login, self.text_position_login)
        self.screen.blit(self.text_surface_passw, self.text_position_passw)
        self.screen.blit(self.text_surface_next, self.text_position_next)
        self.screen.blit(self.text_type_in, self.text_type_in_position)
        self.screen.blit(self.text_type_up, self.text_type_up_position)
        self.screen.blit(self.text_login, self.text_login_inp)
        self.screen.blit(self.text_passw, self.text_passw_inp)

        if self.flag_input_login:
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (self.login_x1, 529),
                             (self.login_x2, 575), 5)
        if self.flag_input_passw:
            pygame.draw.line(self.screen, pygame.Color('black'),
                             (self.passw_x1, 729),
                             (self.passw_x2, 775), 5)

    def validator_check(self, login):
        # логин должен быть также не менее 4 символов и не более 15
        if len(login) < 4 or len(login) > 15:
            return False
        for i in login:
            if i.lower() not in self.validator:
                return False
        return True
