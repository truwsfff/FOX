import pygame
from design import Design
from window import Window


class StandaloneMenu(Window):
    def __init__(self, screen, manager):
        super().__init__(screen, manager)
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption("Standalone Menu")
        self.design = Design()
        self.buttons = {
            'Play': self.design.play_button,
            'Settings': self.design.side_buttons['SETTINGS'],
            'Book': self.design.side_buttons['BOOK'],
            'Game Description': self.design.side_buttons['GAME DESCRIPTION']
        }

    def draw(self):
        self.design.draw(self.screen)
        pygame.display.flip()

    def handle_events(self, event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for action, rect in self.buttons.items():
                if rect.collidepoint(event.pos):
                    self.perform_action(action)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            self.show_exit_dialog(self.screen)

    def perform_action(self, action):
        if action == 'Play':
            print("Запуск игры (заглушка)")
        elif action == 'Settings':
            print("Открываем настройки (заглушка)")
        elif action == 'Book':
            print("Открываем книгу (заглушка)")
        elif action == 'Game Description':
            print("Открываем описание игры (заглушка)")

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                self.handle_events(event)
            self.draw()


if __name__ == "__main__":
    menu = StandaloneMenu()
    menu.run()
