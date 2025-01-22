import pygame

from src.window import Window


class Registration(Window):
    def __init__(self, screen):
        super().__init__(screen)
        pygame.display.set_caption('Регистрация')
        self.rects = {'surf': pygame.Rect(0, 0, 1920, 1080),
                      'fox': pygame.Rect(240, 140, 256, 285),
                      'text_surf_login': pygame.Rect(480, 420, 312, 67),
                      'text_surf_passw': pygame.Rect(480, 620, 312, 67),
                      'text_input_login': pygame.Rect(480, 520, 993, 66),
                      'text_input_passw': pygame.Rect(480, 720, 993, 66),
                      'button_next': pygame.Rect(715, 805, 500, 150),
                      'type_sign_in': pygame.Rect(1030, 135, 312, 67),
                      'type_sign_up': pygame.Rect(1380, 135, 312, 67)
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
        self.text_surface_next = self.font_button.render('Далее', True,
                                                         pygame.Color('white'))
        self.text_type_in = self.font_button.render('Войти', True,
                                                    pygame.Color('white'))
        self.text_text_up = self.font_button.render('Зарегистрироваться',
                                                    True,
                                                    pygame.Color('white'))

        self.text_position_login = (575, 435)
        self.text_position_passw = (570, 635)
        self.text_position_next = (858, 850)

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
