import pygame
from design import Design


class StandaloneMenu:
    def __init__(self):
        pygame.init()

        # Создание окна 1920x1080
        self.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption("Standalone Menu")

        # Дизайн (загрузка изображений и шрифтов)
        self.design = Design()

        # Кнопки
        self.buttons = {
            'Play': self.design.play_button,
            'Setting': self.design.side_buttons['SETTING'],
            'Book': self.design.side_buttons['BOOK'],
            'Game Description': self.design.side_buttons['GAME DESCRIPTION']
        }

    def draw(self):
        """ Отрисовка меню """
        self.design.draw(self.screen)
        pygame.display.flip()

    def handle_event(self, event):
        """ Обработка событий """
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for action, rect in self.buttons.items():
                if rect.collidepoint(event.pos):
                    self.perform_action(action)

    def perform_action(self, action):
        """ Выполнение действий по кнопкам """
        if action == 'Play':
            print("Запуск игры (заглушка)")
        elif action == 'Setting':
            print("Открываем настройки (заглушка)")
        elif action == 'Book':
            print("Открываем книгу (заглушка)")
        elif action == 'Game Description':
            print("Открываем описание игры (заглушка)")

    def run(self):
        """ Запуск главного цикла меню """
        running = True
        while running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.draw()


if __name__ == "__main__":
    menu = StandaloneMenu()
    menu.run()
