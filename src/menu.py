import pygame
import sys
import os

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

        pygame.mixer.music.load('../data/sounds/fon.mp3')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.0)

        self.bg_image = pygame.image.load('../data/images/bg.png')
        pygame.transform.scale(self.bg_image, (
            self.rects.get('bg').width, self.rects.get('bg').height))

        self.fox_image = pygame.image.load('../data/images/fox.png')
        pygame.transform.scale(self.fox_image, (
            self.rects.get('fox').width, self.rects.get('fox').height))

        self.bg_text = pygame.image.load('../data/images/bg_fox_text.png')
        pygame.transform.scale(self.bg_text, (
            self.rects.get('text').width, self.rects.get('text').height))

        self.settings_button_img = pygame.image.load('../data/images/btn_text.png')
        pygame.transform.scale(self.settings_button_img, (
            self.rects.get('settings').width,
            self.rects.get('settings').height))

        self.book_button_img = pygame.image.load('../data/images/btn_text.png')
        pygame.transform.scale(self.book_button_img, (
            self.rects.get('book').width, self.rects.get('book').height))

        self.description_button_img = pygame.image.load('../data/images/btn_text.png')
        pygame.transform.scale(self.description_button_img, (
            self.rects.get('description').width,
            self.rects.get('description').height))

        self.play_button_img = pygame.image.load('../data/images/btn_play.png')
        pygame.transform.scale(self.play_button_img, (
            self.rects.get('play_but').width,
            self.rects.get('play_but').height))

        self.font = pygame.font.Font('../data/font/HomeVideo-Regular.otf', 47)
        self.font_1 = pygame.font.Font('../data/font/HomeVideo-Regular.otf', 384)
        self.font_2 = pygame.font.Font('../data/font/HomeVideo-Regular.otf', 128)
        self.font_3 = pygame.font.Font('../data/font/HomeVideo-Regular.otf', 64)

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

        self.all_sprites = pygame.sprite.Group()
        self.dragon = AnimatedSprite(self.load_image("../data/images/fox-NESW2.png"), 3,
                                     1,
                                     1200,
                                     750, self.all_sprites)

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
            if self.rects.get('play_but').collidepoint(event.pos):
                self.window_man.set_window('startwin')
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

        pygame.time.delay(100)
        self.all_sprites.draw(self.screen)
        self.all_sprites.update()

    def load_image(self, name, colorkey=-1):
        fullname = os.path.join('../data', name)
        # если файл не существует, то выходим
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, grp):
        super().__init__(grp)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]
