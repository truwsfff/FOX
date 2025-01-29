import pygame

class BookDesign:
    def __init__(self):
        self.bg_color = (10, 20, 50)  # Тёмно-синий фон
        self.text_color = (255, 255, 255)  # Белый текст
        self.button_color = (150, 150, 150)  # Серый цвет кнопки выхода
        self.font = pygame.font.Font('../data/HomeVideo-Regular.otf', 80)
        self.small_font = pygame.font.Font('../data/HomeVideo-Regular.otf', 60)

        # Кнопка выхода
        self.exit_button = pygame.Rect(30, 30, 80, 80)

        # Заголовок и список слов
        self.title_text = "BOOK"
        self.words = ["FOX", "FOXY", "FOXTROT"]

    def draw(self, screen):
        screen.fill(self.bg_color)
        # Отображаем заголовок
        title = self.font.render(self.title_text, True, self.text_color)
        screen.blit(title, (screen.get_width() // 2 - 100, 50))
        y_offset = 200
        for word in self.words:
            text_surface = self.small_font.render(word, True, self.text_color)
            screen.blit(text_surface, (100, y_offset))
            y_offset += 100
