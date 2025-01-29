import pygame
from book_desing import BookDesign


class BookScreen:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption("Book")
        self.running = True
        self.design = BookDesign()

        # Кнопка выхода
        self.exit_button = pygame.image.load("../data/x_exit.png")
        self.exit_button_rect = self.exit_button.get_rect(topleft=(50, 50))

    def draw(self):
        self.screen.blit(self.exit_button, self.exit_button_rect)
        pygame.display.flip()
        self.design.draw(self.screen)

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.exit_button_rect.collidepoint(event.pos):
                self.running = False

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.draw()


if __name__ == "__main__":
    book = BookScreen()
    book.run()
