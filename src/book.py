import pygame
from window import Window


class BookScreen(Window):
    def __init__(self, screen, manager):
        super().__init__(screen, manager)
        pygame.display.set_caption("Book")

        self.bg_color = (10, 20, 50)
        self.text_color = (255, 255, 255)
        self.button_color = (150, 150, 150)

        self.font = pygame.font.Font('../data/HomeVideo-Regular.otf', 80)
        self.small_font = pygame.font.Font('../data/HomeVideo-Regular.otf', 60)

        self.rects = {
            'exit': pygame.Rect(30, 30, 80, 80)
        }

        self.exit_button = pygame.image.load("../data/x_exit.png")
        pygame.transform.scale(self.exit_button, (80, 80))

        self.title_text = "BOOK"
        self.words = ["FOX", "FOXY", "FOXTROT"]

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rects.get('exit').collidepoint(event.pos):
                self.window_man.set_window('menu')
                self.window_man.run()

    def draw(self):
        self.screen.fill(self.bg_color)

        title = self.font.render(self.title_text, True, self.text_color)
        self.screen.blit(title, (self.screen.get_width() // 2 - 100, 50))

        y_offset = 200
        for word in self.words:
            text_surface = self.small_font.render(word, True, self.text_color)
            self.screen.blit(text_surface, (100, y_offset))
            y_offset += 100

        self.screen.blit(self.exit_button, self.rects.get('exit').topleft)
