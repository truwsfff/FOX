import pygame
from design import Design
from window import Window
from design_game import PlayGame


class StandaloneMenu(Window):
    def __init__(self, screen, manager):
        super().__init__(screen, manager)
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        pygame.display.set_caption("Standalone Menu")
        self.design = Design()
        self.buttons = {
            'Play': self.design.play_button,
            'Settings': self.design.side_buttons['SETTINGS']['rect'],
            'Book': self.design.side_buttons['BOOK']['rect'],
            'Game Description': self.design.side_buttons['GAME DESCRIPTION']['rect']
        }
        print(type(self.design.side_buttons), self.design.side_buttons)

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
            self.window_man.add_window('play', PlayGame(self.screen, self.window_man))
            self.window_man.set_window('play')
            self.window_man.run()
        elif action == 'Settings':
            self.window_man.set_window('settings')
            self.window_man.run()
        elif action == 'Book':
            self.window_man.set_window('book')
            self.window_man.run()
        elif action == 'Game Description':
            pass

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                self.handle_events(event)
            self.draw()
